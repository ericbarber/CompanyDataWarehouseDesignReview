#!/usr/bin/env python3
"""Generate architecture inventory from the DW2023 Databricks source archive."""

from __future__ import annotations

import ast
import json
import re
import zipfile
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ZIP = ROOT / "DW2023-Databricks.zip"
ADF_SOURCE_DIR = ROOT / "DW2023-DataFactory"
BOOK_SRC = ROOT / "warehouse-architecture-docs" / "src"
LENS_METADATA = ROOT / "architecture-lens" / "metadata"

SOURCE_PREFIX = "DW2023-Databricks/"
NOTEBOOK_PREFIX = SOURCE_PREFIX + "notebooks/"
JOB_PREFIX = SOURCE_PREFIX + "jobs/"


@dataclass(frozen=True)
class FunctionRecord:
    id: str
    name: str
    path: str
    line: int
    signature: str
    notebook_id: str
    group: str


@dataclass(frozen=True)
class NotebookRecord:
    id: str
    name: str
    path: str
    layer: str
    domain: str
    line_count: int
    widgets: list[str]
    functions: list[str]
    table_references: list[str]
    secret_references: int
    notebook_runs: list[str]


@dataclass(frozen=True)
class JobTaskRecord:
    task_key: str
    notebook_path: str
    parameters: list[str]


@dataclass(frozen=True)
class JobRecord:
    id: str
    name: str
    path: str
    task_count: int
    tasks: list[JobTaskRecord]
    parameters: list[str]
    run_as: str


@dataclass(frozen=True)
class AdfActivityRecord:
    name: str
    type: str
    path: str
    depends_on: list[str]
    pipeline_references: list[str]
    notebook_paths: list[str]
    databricks_job_ids: list[str]
    linked_services: list[str]
    datasets: list[str]


@dataclass(frozen=True)
class AdfPipelineRecord:
    id: str
    name: str
    path: str
    description: str
    parameters: list[str]
    variables: list[str]
    activity_count: int
    activity_types: dict[str, int]
    pipeline_references: list[str]
    notebook_paths: list[str]
    linked_services: list[str]
    datasets: list[str]
    activities: list[AdfActivityRecord]


@dataclass(frozen=True)
class AdfTriggerRecord:
    id: str
    name: str
    path: str
    runtime_state: str
    trigger_type: str
    frequency: str
    interval: str
    start_time: str
    time_zone: str
    pipelines: list[str]


@dataclass(frozen=True)
class AdfResourceRecord:
    id: str
    name: str
    path: str
    resource_kind: str
    resource_type: str


@dataclass(frozen=True)
class MetadataQueryRecord:
    id: str
    pipeline: str
    json_path: str
    property_name: str
    query_text: str
    is_expression: bool
    tables: list[str]
    metadata_tables: list[str]
    data_source_types: list[str]
    item_fields: list[str]
    pipeline_parameters: list[str]
    category: str


@dataclass(frozen=True)
class MetadataFieldUsageRecord:
    field: str
    use_count: int
    pipeline_count: int
    pipelines: list[str]
    sample_expressions: list[str]


def main() -> None:
    if not SOURCE_ZIP.exists():
        raise SystemExit(f"Source archive not found: {SOURCE_ZIP}")

    inventory = build_inventory(SOURCE_ZIP)
    write_outputs(inventory)


def build_inventory(source_zip: Path) -> dict:
    with zipfile.ZipFile(source_zip) as archive:
        names = sorted(info.filename for info in archive.infolist() if not info.is_dir())
        notebooks = build_notebook_records(archive, names)
        functions = build_function_records(archive, notebooks)
        jobs = build_job_records(archive, names)
        bundle = parse_bundle_config(archive, names)
    adf = build_adf_inventory(ADF_SOURCE_DIR)
    flow_graph = build_flow_graph(adf["pipelines"], adf["triggers"], adf["resources"], jobs, notebooks)

    notebook_by_id = {record.id: record for record in notebooks}
    function_counts_by_notebook: dict[str, int] = Counter(record.notebook_id for record in functions)
    notebooks_with_functions = [
        record for record in notebooks if function_counts_by_notebook.get(record.id, 0) > 0
    ]

    return {
        "generated_on": date.today().isoformat(),
        "source": str(source_zip.relative_to(ROOT)),
        "summary": {
            "python_files_under_notebooks": len(notebooks),
            "explicit_python_functions": len(functions),
            "notebooks_with_functions": len(notebooks_with_functions),
            "databricks_job_json_files": len(jobs),
            "databricks_bundle_targets": len(bundle["targets"]),
            "adf_pipelines": len(adf["pipelines"]),
            "adf_triggers": len(adf["triggers"]),
            "adf_datasets": sum(
                1 for record in adf["resources"] if record.resource_kind == "dataset"
            ),
            "adf_linked_services": sum(
                1 for record in adf["resources"] if record.resource_kind == "linkedService"
            ),
            "adf_integration_runtimes": sum(
                1 for record in adf["resources"] if record.resource_kind == "integrationRuntime"
            ),
            "adf_metadata_queries": len(adf["metadata_queries"]),
            "adf_metadata_field_usages": len(adf["metadata_field_usages"]),
            "notebooks_with_widgets": sum(1 for record in notebooks if record.widgets),
            "notebooks_with_table_references": sum(
                1 for record in notebooks if record.table_references
            ),
            "notebooks_with_secret_references": sum(
                1 for record in notebooks if record.secret_references
            ),
            "notebooks_with_notebook_runs": sum(1 for record in notebooks if record.notebook_runs),
        },
        "counts": {
            "by_layer": Counter(record.layer for record in notebooks),
            "by_domain": Counter(record.domain for record in notebooks),
            "functions_by_group": Counter(record.group for record in functions),
            "adf_activity_types": adf["activity_types"],
            "adf_resource_types": adf["resource_types"],
            "adf_metadata_tables": Counter(
                table for query in adf["metadata_queries"] for table in query.metadata_tables
            ),
            "adf_metadata_query_categories": Counter(
                query.category for query in adf["metadata_queries"]
            ),
        },
        "bundle": bundle,
        "notebooks": [asdict(record) for record in notebooks],
        "functions": [asdict(record) for record in functions],
        "jobs": [job_to_dict(record) for record in jobs],
        "adf": {
            "source": adf["source"],
            "pipelines": [adf_pipeline_to_dict(record) for record in adf["pipelines"]],
            "triggers": [asdict(record) for record in adf["triggers"]],
            "resources": [asdict(record) for record in adf["resources"]],
            "metadata_queries": [asdict(record) for record in adf["metadata_queries"]],
            "metadata_field_usages": [
                asdict(record) for record in adf["metadata_field_usages"]
            ],
        },
        "flow_graph": flow_graph,
        "relationships": {
            "job_to_notebook_paths": build_job_notebook_relationships(jobs),
            "adf_trigger_to_pipelines": {
                trigger.id: trigger.pipelines for trigger in adf["triggers"]
            },
            "adf_pipeline_to_pipelines": {
                pipeline.id: pipeline.pipeline_references
                for pipeline in adf["pipelines"]
                if pipeline.pipeline_references
            },
            "adf_pipeline_to_notebook_paths": {
                pipeline.id: pipeline.notebook_paths
                for pipeline in adf["pipelines"]
                if pipeline.notebook_paths
            },
            "adf_trigger_flow_summaries": {
                summary["trigger_id"]: summary for summary in flow_graph["flow_summaries"]
            },
            "notebook_to_functions": {
                notebook_id: sorted(
                    function.name for function in functions if function.notebook_id == notebook_id
                )
                for notebook_id in notebook_by_id
                if function_counts_by_notebook.get(notebook_id, 0) > 0
            },
        },
    }


def build_notebook_records(
    archive: zipfile.ZipFile, names: Iterable[str]
) -> list[NotebookRecord]:
    records: list[NotebookRecord] = []
    notebook_paths = [
        name
        for name in names
        if name.startswith(NOTEBOOK_PREFIX) and name.endswith(".py")
    ]

    for index, path in enumerate(notebook_paths, start=1):
        source = read_text(archive, path)
        relative_path = strip_source_prefix(path)
        layer = infer_layer(relative_path)
        domain = infer_domain(relative_path, layer)
        functions = extract_function_names(source)
        widgets = sorted(set(extract_widgets(source)))
        table_references = sorted(set(extract_table_references(source)))
        notebook_runs = sorted(set(extract_notebook_runs(source)))
        secret_references = len(extract_secret_references(source))

        records.append(
            NotebookRecord(
                id=f"NB-{index:05d}",
                name=Path(path).stem,
                path=relative_path,
                layer=layer,
                domain=domain,
                line_count=len(source.splitlines()),
                widgets=widgets,
                functions=functions,
                table_references=table_references,
                secret_references=secret_references,
                notebook_runs=notebook_runs,
            )
        )

    return records


def build_function_records(
    archive: zipfile.ZipFile, notebooks: list[NotebookRecord]
) -> list[FunctionRecord]:
    records: list[FunctionRecord] = []

    for notebook in notebooks:
        source = read_text(archive, SOURCE_PREFIX + notebook.path)
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                records.append(
                    FunctionRecord(
                        id=f"FUN-{len(records) + 1:05d}",
                        name=node.name,
                        path=notebook.path,
                        line=node.lineno,
                        signature=format_signature(source, node),
                        notebook_id=notebook.id,
                        group=classify_function(node.name),
                    )
                )

    return records


def build_job_records(archive: zipfile.ZipFile, names: Iterable[str]) -> list[JobRecord]:
    records: list[JobRecord] = []
    job_paths = [
        name
        for name in names
        if name.startswith(JOB_PREFIX) and name.endswith(".json")
    ]

    for index, path in enumerate(job_paths, start=1):
        raw = read_text(archive, path)
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            continue

        tasks: list[JobTaskRecord] = []
        for task in payload.get("tasks", []):
            notebook_task = task.get("notebook_task", {})
            base_parameters = notebook_task.get("base_parameters", {})
            tasks.append(
                JobTaskRecord(
                    task_key=str(task.get("task_key", "")),
                    notebook_path=str(notebook_task.get("notebook_path", "")),
                    parameters=sorted(base_parameters.keys()),
                )
            )

        parameters = sorted(
            str(parameter.get("name", ""))
            for parameter in payload.get("parameters", [])
            if parameter.get("name")
        )
        run_as = payload.get("run_as", {})
        run_as_value = run_as.get("service_principal_name") or run_as.get("user_name") or ""

        records.append(
            JobRecord(
                id=f"JOB-{index:05d}",
                name=str(payload.get("name", Path(path).stem)),
                path=strip_source_prefix(path),
                task_count=len(tasks),
                tasks=tasks,
                parameters=parameters,
                run_as=str(run_as_value),
            )
        )

    return records


def parse_bundle_config(archive: zipfile.ZipFile, names: Iterable[str]) -> dict:
    if SOURCE_PREFIX + "databricks.yml" not in names:
        return {"path": "", "targets": []}

    text = read_text(archive, SOURCE_PREFIX + "databricks.yml")
    targets: list[dict[str, str]] = []
    in_targets = False
    current_target = ""

    for line in text.splitlines():
        if re.match(r"^targets:\s*$", line):
            in_targets = True
            continue
        if in_targets and re.match(r"^[a-zA-Z_][\w-]*:\s*$", line):
            break
        target_match = re.match(r"^  ([\w-]+):\s*$", line)
        if in_targets and target_match:
            current_target = target_match.group(1)
            targets.append({"name": current_target, "host": ""})
            continue
        host_match = re.match(r"^\s+host:\s*(\S+)\s*$", line)
        if in_targets and current_target and host_match:
            targets[-1]["host"] = host_match.group(1)

    return {"path": "DW2023-Databricks/databricks.yml", "targets": targets}


def build_adf_inventory(source_dir: Path) -> dict:
    if not source_dir.exists():
        return {
            "source": "",
            "pipelines": [],
            "triggers": [],
            "resources": [],
            "metadata_queries": [],
            "metadata_field_usages": [],
            "activity_types": Counter(),
            "resource_types": Counter(),
        }

    pipelines = build_adf_pipeline_records(source_dir)
    triggers = build_adf_trigger_records(source_dir)
    resources = build_adf_resource_records(source_dir)
    metadata_queries = build_metadata_query_records(source_dir)
    metadata_field_usages = build_metadata_field_usage_records(source_dir)

    activity_types: Counter[str] = Counter()
    for pipeline in pipelines:
        activity_types.update(pipeline.activity_types)

    resource_types: Counter[str] = Counter(
        f"{record.resource_kind}:{record.resource_type}" for record in resources
    )

    return {
        "source": str(source_dir.relative_to(ROOT)),
        "pipelines": pipelines,
        "triggers": triggers,
        "resources": resources,
        "metadata_queries": metadata_queries,
        "metadata_field_usages": metadata_field_usages,
        "activity_types": activity_types,
        "resource_types": resource_types,
    }


def build_adf_pipeline_records(source_dir: Path) -> list[AdfPipelineRecord]:
    records: list[AdfPipelineRecord] = []
    for index, path in enumerate(sorted((source_dir / "pipeline").glob("*.json")), start=1):
        payload = read_json_file(path)
        properties = payload.get("properties", {})
        activities = flatten_adf_activities(properties.get("activities", []))
        activity_types = Counter(activity.type for activity in activities)

        records.append(
            AdfPipelineRecord(
                id=f"ADF-PL-{index:05d}",
                name=str(payload.get("name", path.stem)),
                path=str(path.relative_to(ROOT)),
                description=str(properties.get("description", "")),
                parameters=sorted((properties.get("parameters") or {}).keys()),
                variables=sorted((properties.get("variables") or {}).keys()),
                activity_count=len(activities),
                activity_types=dict(sorted(activity_types.items())),
                pipeline_references=sorted(
                    set(ref for activity in activities for ref in activity.pipeline_references)
                ),
                notebook_paths=sorted(
                    set(ref for activity in activities for ref in activity.notebook_paths)
                ),
                linked_services=sorted(
                    set(ref for activity in activities for ref in activity.linked_services)
                ),
                datasets=sorted(set(ref for activity in activities for ref in activity.datasets)),
                activities=activities,
            )
        )

    return records


def build_adf_trigger_records(source_dir: Path) -> list[AdfTriggerRecord]:
    records: list[AdfTriggerRecord] = []
    for index, path in enumerate(sorted((source_dir / "trigger").glob("*.json")), start=1):
        payload = read_json_file(path)
        properties = payload.get("properties", {})
        recurrence = properties.get("typeProperties", {}).get("recurrence", {})
        pipelines = [
            pipeline.get("pipelineReference", {}).get("referenceName", "")
            for pipeline in properties.get("pipelines", [])
        ]

        records.append(
            AdfTriggerRecord(
                id=f"ADF-TRG-{index:05d}",
                name=str(payload.get("name", path.stem)),
                path=str(path.relative_to(ROOT)),
                runtime_state=str(properties.get("runtimeState", "")),
                trigger_type=str(properties.get("type", "")),
                frequency=str(recurrence.get("frequency", "")),
                interval=str(recurrence.get("interval", "")),
                start_time=str(recurrence.get("startTime", "")),
                time_zone=str(recurrence.get("timeZone", "")),
                pipelines=sorted(pipeline for pipeline in pipelines if pipeline),
            )
        )

    return records


def build_adf_resource_records(source_dir: Path) -> list[AdfResourceRecord]:
    records: list[AdfResourceRecord] = []
    resource_dirs = ["dataset", "linkedService", "integrationRuntime", "credential"]

    for resource_kind in resource_dirs:
        for path in sorted((source_dir / resource_kind).glob("*.json")):
            payload = read_json_file(path)
            properties = payload.get("properties", {})
            records.append(
                AdfResourceRecord(
                    id=f"ADF-{resource_kind.upper()}-{len(records) + 1:05d}",
                    name=str(payload.get("name", path.stem)),
                    path=str(path.relative_to(ROOT)),
                    resource_kind=resource_kind,
                    resource_type=str(properties.get("type", "unknown")),
                )
            )

    return records


def build_metadata_query_records(source_dir: Path) -> list[MetadataQueryRecord]:
    records: list[MetadataQueryRecord] = []
    for pipeline_path in sorted((source_dir / "pipeline").glob("*.json")):
        payload = read_json_file(pipeline_path)
        pipeline_name = str(payload.get("name", pipeline_path.stem))
        for json_path, property_name, raw_value in collect_query_properties(payload):
            query_text = expression_to_string(raw_value)
            if not query_text.strip():
                continue
            tables = extract_sql_tables(query_text)
            metadata_tables = sorted(
                table for table in tables if table.lower().startswith(("adf.", "[adf]."))
            )
            if not metadata_tables and "item()." not in query_text and "pipeline().parameters" not in query_text:
                continue
            records.append(
                MetadataQueryRecord(
                    id=f"META-QRY-{len(records) + 1:05d}",
                    pipeline=pipeline_name,
                    json_path=json_path,
                    property_name=property_name,
                    query_text=compact_text(query_text, 500),
                    is_expression=is_dynamic_expression(query_text)
                    or (isinstance(raw_value, dict) and raw_value.get("type") == "Expression"),
                    tables=tables,
                    metadata_tables=metadata_tables,
                    data_source_types=extract_data_source_types(query_text),
                    item_fields=extract_item_fields(query_text),
                    pipeline_parameters=extract_pipeline_parameters(query_text),
                    category=classify_metadata_query(query_text, metadata_tables),
                )
            )
    return records


def build_metadata_field_usage_records(source_dir: Path) -> list[MetadataFieldUsageRecord]:
    field_to_pipelines: dict[str, set[str]] = defaultdict(set)
    field_to_expressions: dict[str, list[str]] = defaultdict(list)
    field_counts: Counter[str] = Counter()

    for pipeline_path in sorted((source_dir / "pipeline").glob("*.json")):
        payload = read_json_file(pipeline_path)
        pipeline_name = str(payload.get("name", pipeline_path.stem))
        for expression in collect_strings(payload):
            fields = extract_item_fields(expression)
            for field in fields:
                field_counts[field] += 1
                field_to_pipelines[field].add(pipeline_name)
                samples = field_to_expressions[field]
                compact = compact_text(expression, 160)
                if compact not in samples and len(samples) < 3:
                    samples.append(compact)

    return [
        MetadataFieldUsageRecord(
            field=field,
            use_count=count,
            pipeline_count=len(field_to_pipelines[field]),
            pipelines=sorted(field_to_pipelines[field])[:20],
            sample_expressions=field_to_expressions[field],
        )
        for field, count in sorted(field_counts.items(), key=lambda item: (-item[1], item[0]))
    ]


def collect_query_properties(value, path: str = "") -> list[tuple[str, str, object]]:
    records: list[tuple[str, str, object]] = []
    query_keys = {"sqlReaderQuery", "query"}
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}/{key}" if path else key
            if key in query_keys:
                records.append((child_path, key, child))
            records.extend(collect_query_properties(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            records.extend(collect_query_properties(child, f"{path}[{index}]"))
    return records


def collect_strings(value) -> list[str]:
    strings: list[str] = []
    if isinstance(value, str):
        strings.append(value)
    elif isinstance(value, dict):
        for child in value.values():
            strings.extend(collect_strings(child))
    elif isinstance(value, list):
        for child in value:
            strings.extend(collect_strings(child))
    return strings


def extract_sql_tables(query_text: str) -> list[str]:
    normalized = re.sub(
        r"\[([A-Za-z0-9_]+)\]\.\[([A-Za-z0-9_]+)\]",
        r"\1.\2",
        query_text,
    )
    pattern = re.compile(
        r"\b(?:FROM|JOIN|MERGE\s+INTO|UPDATE|INTO)\s+([A-Za-z0-9_.]+)",
        flags=re.IGNORECASE,
    )
    return sorted(set(normalize_sql_identifier(match.strip(".")) for match in pattern.findall(normalized)))


def normalize_sql_identifier(value: str) -> str:
    parts = value.split(".")
    if len(parts) == 2 and parts[0].lower() == "adf":
        known_tables = {
            "azureresources": "azureResources",
            "dataprocess": "DataProcess",
            "dataprocessdependency": "DataProcessDependency",
            "datasource": "DataSource",
            "operationmetriclog": "operationMetricLog",
            "powerbidataset": "powerBiDataset",
        }
        table = known_tables.get(parts[1].lower(), parts[1])
        return f"adf.{table}"
    return value


def extract_data_source_types(query_text: str) -> list[str]:
    pattern = re.compile(
        r"(?:upper\()?dataSourceType(?:\))?\s*=\s*'([^']+)'",
        flags=re.IGNORECASE,
    )
    return sorted(set(pattern.findall(query_text)))


def extract_item_fields(value: str) -> list[str]:
    return sorted(set(re.findall(r"item\(\)\.([A-Za-z_][A-Za-z0-9_]*)", str(value))))


def extract_pipeline_parameters(value: str) -> list[str]:
    return sorted(
        set(re.findall(r"pipeline\(\)\.parameters\.([A-Za-z_][A-Za-z0-9_]*)", str(value)))
    )


def classify_metadata_query(query_text: str, metadata_tables: list[str]) -> str:
    lowered = query_text.lower()
    metadata_table_text = " ".join(table.lower() for table in metadata_tables)
    if "dataprocessdependency" in metadata_table_text:
        return "Process dependency lookup"
    if "dataprocess" in metadata_table_text:
        return "Process metadata lookup"
    if "datasource" in metadata_table_text:
        return "Source metadata lookup"
    if "operationmetriclog" in metadata_table_text:
        return "Operational metrics lookup"
    if "azureresources" in metadata_table_text:
        return "Azure resource lookup"
    if "item()." in lowered:
        return "Per-object runtime query"
    return "Other metadata query"


def compact_text(value: str, max_length: int) -> str:
    compact = re.sub(r"\s+", " ", str(value)).strip()
    if len(compact) <= max_length:
        return compact
    return compact[: max_length - 3].rstrip() + "..."


def flatten_adf_activities(
    activities: list[dict], parent_path: str = ""
) -> list[AdfActivityRecord]:
    records: list[AdfActivityRecord] = []
    for activity in activities:
        name = str(activity.get("name", ""))
        activity_path = f"{parent_path}/{name}" if parent_path else name
        type_properties = activity.get("typeProperties", {})
        nested = nested_adf_activities(activity)

        records.append(
            AdfActivityRecord(
                name=name,
                type=str(activity.get("type", "")),
                path=activity_path,
                depends_on=[
                    str(dep.get("activity", ""))
                    for dep in activity.get("dependsOn", [])
                    if dep.get("activity")
                ],
                pipeline_references=extract_reference_names(
                    type_properties, keys={"pipeline"}
                ),
                notebook_paths=extract_adf_notebook_paths(type_properties),
                databricks_job_ids=extract_adf_databricks_job_ids(type_properties),
                linked_services=extract_reference_names(
                    activity, keys={"linkedServiceName", "connectVia"}
                ),
                datasets=extract_dataset_references(activity),
            )
        )
        records.extend(flatten_adf_activities(nested, activity_path))

    return records


def nested_adf_activities(activity: dict) -> list[dict]:
    type_properties = activity.get("typeProperties", {})
    nested: list[dict] = []
    for key in ("activities", "ifTrueActivities", "ifFalseActivities", "defaultActivities"):
        value = type_properties.get(key)
        if isinstance(value, list):
            nested.extend(item for item in value if isinstance(item, dict))

    cases = type_properties.get("cases", [])
    if isinstance(cases, list):
        for case in cases:
            value = case.get("activities", []) if isinstance(case, dict) else []
            if isinstance(value, list):
                nested.extend(item for item in value if isinstance(item, dict))

    return nested


def extract_reference_names(value, keys: set[str] | None = None) -> list[str]:
    refs: list[str] = []

    def walk(item, parent_key: str = "") -> None:
        if isinstance(item, dict):
            reference_name = item.get("referenceName")
            if reference_name and (keys is None or parent_key in keys):
                refs.append(str(reference_name))
            for child_key, child_value in item.items():
                if keys is None or child_key in keys or isinstance(child_value, (dict, list)):
                    walk(child_value, child_key)
        elif isinstance(item, list):
            for child in item:
                walk(child, parent_key)

    walk(value)
    return sorted(set(refs))


def extract_dataset_references(activity: dict) -> list[str]:
    refs: list[str] = []

    def walk(item) -> None:
        if isinstance(item, dict):
            if item.get("type") == "DatasetReference" and item.get("referenceName"):
                refs.append(str(item["referenceName"]))
            for child in item.values():
                walk(child)
        elif isinstance(item, list):
            for child in item:
                walk(child)

    walk(activity)
    return sorted(set(refs))


def extract_adf_notebook_paths(type_properties: dict) -> list[str]:
    paths: list[str] = []

    def walk(item) -> None:
        if isinstance(item, dict):
            for key, value in item.items():
                if key == "notebookPath":
                    paths.append(expression_to_string(value))
                else:
                    walk(value)
        elif isinstance(item, list):
            for child in item:
                walk(child)

    walk(type_properties)
    return sorted(set(path for path in paths if path))


def extract_adf_databricks_job_ids(type_properties: dict) -> list[str]:
    job_id = type_properties.get("jobId")
    if job_id is None:
        return []
    return [expression_to_string(job_id)]


def expression_to_string(value) -> str:
    if isinstance(value, dict):
        inner = value.get("value")
        if inner is not None:
            return str(inner)
    if value is None:
        return ""
    return str(value)


def read_json_file(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_flow_graph(
    pipelines: list[AdfPipelineRecord],
    triggers: list[AdfTriggerRecord],
    resources: list[AdfResourceRecord],
    jobs: list[JobRecord],
    notebooks: list[NotebookRecord],
) -> dict:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    pipeline_by_name = {pipeline.name: pipeline for pipeline in pipelines}
    resource_by_name = {resource.name: resource for resource in resources}
    job_by_name = {job.name: job for job in jobs}
    notebook_by_workspace_path = {
        normalize_databricks_notebook_path("/Workspace/" + record.path.removeprefix("notebooks/")): record
        for record in notebooks
    }

    def add_node(node_id: str, node_type: str, label: str, **properties) -> None:
        nodes.setdefault(
            node_id,
            {
                "id": node_id,
                "type": node_type,
                "label": label,
                "properties": properties,
            },
        )

    def add_edge(source: str, target: str, edge_type: str, **properties) -> None:
        edges.append(
            {
                "source": source,
                "target": target,
                "type": edge_type,
                "properties": properties,
            }
        )

    for trigger in triggers:
        trigger_node = graph_id("adf_trigger", trigger.name)
        add_node(
            trigger_node,
            "adf_trigger",
            trigger.name,
            runtime_state=trigger.runtime_state,
            trigger_type=trigger.trigger_type,
            frequency=trigger.frequency,
            interval=trigger.interval,
            start_time=trigger.start_time,
            time_zone=trigger.time_zone,
        )
        for pipeline_name in trigger.pipelines:
            pipeline_node = graph_id("adf_pipeline", pipeline_name)
            add_node(pipeline_node, "adf_pipeline", pipeline_name)
            add_edge(trigger_node, pipeline_node, "schedules")

    for pipeline in pipelines:
        pipeline_node = graph_id("adf_pipeline", pipeline.name)
        add_node(
            pipeline_node,
            "adf_pipeline",
            pipeline.name,
            path=pipeline.path,
            activity_count=pipeline.activity_count,
            parameters=pipeline.parameters,
        )
        for activity in pipeline.activities:
            activity_node = graph_id("adf_activity", f"{pipeline.name}/{activity.path}")
            add_node(
                activity_node,
                "adf_activity",
                activity.name,
                pipeline=pipeline.name,
                activity_path=activity.path,
                activity_type=activity.type,
                depends_on=activity.depends_on,
            )
            add_edge(pipeline_node, activity_node, "contains_activity")

            for dependency_name in activity.depends_on:
                dependency_node = graph_id("adf_activity", f"{pipeline.name}/{dependency_name}")
                add_node(
                    dependency_node,
                    "adf_activity",
                    dependency_name,
                    pipeline=pipeline.name,
                    inferred=True,
                )
                add_edge(activity_node, dependency_node, "depends_on")

            for child_pipeline in activity.pipeline_references:
                child_node = graph_id("adf_pipeline", child_pipeline)
                add_node(child_node, "adf_pipeline", child_pipeline)
                add_edge(activity_node, child_node, "executes_pipeline")
                add_edge(pipeline_node, child_node, "calls_pipeline")

            for raw_notebook_path in activity.notebook_paths:
                normalized = normalize_databricks_notebook_path(raw_notebook_path)
                notebook = notebook_by_workspace_path.get(normalized)
                notebook_node = (
                    graph_id("databricks_notebook", notebook.id)
                    if notebook
                    else graph_id("databricks_notebook_path", normalized)
                )
                add_node(
                    notebook_node,
                    "databricks_notebook",
                    notebook.name if notebook else raw_notebook_path,
                    path=notebook.path if notebook else raw_notebook_path,
                    resolved=bool(notebook),
                    dynamic=is_dynamic_expression(raw_notebook_path),
                )
                add_edge(activity_node, notebook_node, "runs_notebook")
                add_edge(pipeline_node, notebook_node, "invokes_notebook")

            for databricks_job_id in activity.databricks_job_ids:
                job_node = graph_id("databricks_job_ref", databricks_job_id)
                matching_job = job_by_name.get(databricks_job_id)
                add_node(
                    job_node,
                    "databricks_job",
                    matching_job.name if matching_job else databricks_job_id,
                    resolved=bool(matching_job),
                    dynamic=is_dynamic_expression(databricks_job_id),
                )
                add_edge(activity_node, job_node, "runs_databricks_job")
                add_edge(pipeline_node, job_node, "invokes_databricks_job")

            for dataset_name in activity.datasets:
                dataset_node = graph_id("adf_dataset", dataset_name)
                dataset = resource_by_name.get(dataset_name)
                add_node(
                    dataset_node,
                    "adf_dataset",
                    dataset_name,
                    resource_type=dataset.resource_type if dataset else "unknown",
                    resolved=bool(dataset),
                )
                add_edge(activity_node, dataset_node, "uses_dataset")
                add_edge(pipeline_node, dataset_node, "uses_dataset")

            for linked_service_name in activity.linked_services:
                service_node = graph_id("adf_linked_service", linked_service_name)
                linked_service = resource_by_name.get(linked_service_name)
                add_node(
                    service_node,
                    "adf_linked_service",
                    linked_service_name,
                    resource_type=linked_service.resource_type if linked_service else "unknown",
                    resolved=bool(linked_service),
                )
                add_edge(activity_node, service_node, "uses_linked_service")
                add_edge(pipeline_node, service_node, "uses_linked_service")

    flow_summaries = [
        summarize_trigger_flow(trigger, pipeline_by_name, resource_by_name)
        for trigger in triggers
    ]

    return {
        "nodes": sorted(nodes.values(), key=lambda node: node["id"]),
        "edges": sorted(edges, key=lambda edge: (edge["source"], edge["target"], edge["type"])),
        "flow_summaries": flow_summaries,
        "summary": {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "trigger_count": len(triggers),
            "pipeline_count": len(pipelines),
        },
    }


def summarize_trigger_flow(
    trigger: AdfTriggerRecord,
    pipeline_by_name: dict[str, AdfPipelineRecord],
    resource_by_name: dict[str, AdfResourceRecord],
) -> dict:
    visited: set[str] = set()
    pending = list(trigger.pipelines)
    pipeline_names: set[str] = set()
    activity_types: Counter[str] = Counter()
    datasets: set[str] = set()
    linked_services: set[str] = set()
    notebook_paths: set[str] = set()
    databricks_job_ids: set[str] = set()

    while pending:
        pipeline_name = pending.pop(0)
        if pipeline_name in visited:
            continue
        visited.add(pipeline_name)
        pipeline = pipeline_by_name.get(pipeline_name)
        if not pipeline:
            continue

        pipeline_names.add(pipeline.name)
        activity_types.update(pipeline.activity_types)
        datasets.update(pipeline.datasets)
        linked_services.update(pipeline.linked_services)
        notebook_paths.update(pipeline.notebook_paths)
        for activity in pipeline.activities:
            databricks_job_ids.update(activity.databricks_job_ids)
        pending.extend(ref for ref in pipeline.pipeline_references if ref not in visited)

    linked_service_types = Counter(
        resource_by_name[name].resource_type
        for name in linked_services
        if name in resource_by_name
    )
    dataset_types = Counter(
        resource_by_name[name].resource_type for name in datasets if name in resource_by_name
    )
    blockers = []
    if activity_types.get("Copy", 0):
        blockers.append("copy_activity")
    if linked_service_types.get("FileServer", 0) or linked_service_types.get("Sftp", 0):
        blockers.append("filesystem_or_sftp")
    if linked_service_types.get("AzureKeyVault", 0):
        blockers.append("key_vault_dependency")
    if activity_types.get("WebActivity", 0):
        blockers.append("web_activity")
    if any(is_dynamic_expression(path) for path in notebook_paths):
        blockers.append("dynamic_notebook_path")

    complexity = "Low"
    if len(pipeline_names) > 20 or activity_types.get("Copy", 0) > 10 or activity_types.get("ExecutePipeline", 0) > 50:
        complexity = "High"
    elif len(pipeline_names) > 8 or blockers:
        complexity = "Medium"

    if not blockers and (not activity_types.get("Copy", 0)):
        recommended_wave = "Wave 1 - schedule and notebook task migration"
    elif "filesystem_or_sftp" in blockers:
        recommended_wave = "Wave 3 - connector and network replacement"
    elif activity_types.get("Copy", 0):
        recommended_wave = "Wave 2 - ingestion replacement"
    else:
        recommended_wave = "Wave 1 - schedule and notebook task migration"

    return {
        "trigger_id": trigger.id,
        "trigger_name": trigger.name,
        "runtime_state": trigger.runtime_state,
        "root_pipelines": trigger.pipelines,
        "pipeline_count": len(pipeline_names),
        "activity_count": sum(activity_types.values()),
        "activity_types": dict(sorted(activity_types.items())),
        "dataset_count": len(datasets),
        "dataset_types": dict(sorted(dataset_types.items())),
        "linked_service_count": len(linked_services),
        "linked_service_types": dict(sorted(linked_service_types.items())),
        "notebook_path_count": len(notebook_paths),
        "databricks_job_ref_count": len(databricks_job_ids),
        "blockers": sorted(set(blockers)),
        "complexity": complexity,
        "recommended_wave": recommended_wave,
    }


def graph_id(kind: str, value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9_.-]+", "-", str(value).strip()).strip("-")
    return f"{kind}:{normalized or 'unknown'}"


def normalize_databricks_notebook_path(value: str) -> str:
    value = clean_expression(str(value)).strip()
    value = value.removesuffix(".py")
    if value.startswith("/Workspace/"):
        return value
    if value.startswith("Workspace/"):
        return "/" + value
    return value


def is_dynamic_expression(value: str) -> bool:
    return str(value).strip().startswith("@")


def write_outputs(inventory: dict) -> None:
    LENS_METADATA.mkdir(parents=True, exist_ok=True)
    (LENS_METADATA / "inventory.json").write_text(
        json.dumps(make_json_safe(inventory), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (LENS_METADATA / "flow-graph.json").write_text(
        json.dumps(make_json_safe(inventory["flow_graph"]), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (LENS_METADATA / "metadata-dependencies.json").write_text(
        json.dumps(
            make_json_safe(
                {
                    "queries": inventory["adf"]["metadata_queries"],
                    "field_usages": inventory["adf"]["metadata_field_usages"],
                    "metadata_tables": inventory["counts"]["adf_metadata_tables"],
                    "query_categories": inventory["counts"]["adf_metadata_query_categories"],
                }
            ),
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    write_repository_inventory(inventory)
    write_notebook_catalog(inventory)
    write_function_catalog(inventory)
    write_job_catalog(inventory)
    write_adf_orchestration_catalog(inventory)
    write_metadata_dependency_catalog(inventory)
    write_current_flow_graph(inventory)
    write_orchestration_migration_plan(inventory)
    write_dynamic_resolution_plan(inventory)
    write_adf_migration_waves(inventory)


def write_repository_inventory(inventory: dict) -> None:
    summary = inventory["summary"]
    by_layer = inventory["counts"]["by_layer"]
    bundle = inventory["bundle"]
    targets = ", ".join(target["name"] for target in bundle["targets"]) or "None discovered"

    lines = [
        "# Repository Inventory",
        "",
        f"**Inventory date:** {inventory['generated_on']}  ",
        f"**Sources:** `{inventory['source']}` and `{inventory['adf']['source'] or 'DW2023-DataFactory not present'}` generated by `tools/generate_inventory.py`",
        "",
        "## Generated counts",
        "",
        "| Artifact | Count or observation |",
        "|---|---:|",
        f"| Python files under `notebooks/` | {summary['python_files_under_notebooks']} |",
        f"| Explicit Python function declarations | {summary['explicit_python_functions']} |",
        f"| Notebooks containing function declarations | {summary['notebooks_with_functions']} |",
        f"| Databricks job JSON files | {summary['databricks_job_json_files']} |",
        f"| Databricks bundle targets | {summary['databricks_bundle_targets']} |",
        f"| Declared workspace targets | {targets} |",
        f"| ADF pipelines | {summary['adf_pipelines']} |",
        f"| ADF schedule triggers | {summary['adf_triggers']} |",
        f"| ADF datasets | {summary['adf_datasets']} |",
        f"| ADF linked services | {summary['adf_linked_services']} |",
        f"| ADF integration runtimes | {summary['adf_integration_runtimes']} |",
        f"| ADF metadata queries | {summary['adf_metadata_queries']} |",
        f"| ADF metadata item fields | {summary['adf_metadata_field_usages']} |",
        f"| Flow graph nodes | {inventory['flow_graph']['summary']['node_count']} |",
        f"| Flow graph edges | {inventory['flow_graph']['summary']['edge_count']} |",
        "",
        "## Notebook counts by layer",
        "",
        "| Layer | Count |",
        "|---|---:|",
    ]

    for layer, count in sorted(by_layer.items()):
        lines.append(f"| {md(layer)} | {count} |")

    lines.extend(
        [
            "",
            "## Discovery signals",
            "",
            "| Signal | Notebook count |",
            "|---|---:|",
            f"| Widgets/parameters detected | {summary['notebooks_with_widgets']} |",
            f"| Table references detected | {summary['notebooks_with_table_references']} |",
            f"| Secret references detected | {summary['notebooks_with_secret_references']} |",
            f"| `dbutils.notebook.run` calls detected | {summary['notebooks_with_notebook_runs']} |",
            "",
            "## Important limitations",
            "",
            "- Counts are generated from repository/archive evidence and do not identify active, deployed, duplicated, or obsolete components.",
            "- Static parsing cannot fully resolve dynamic SQL, runtime-composed paths, platform lineage, or consumer behavior.",
            "- Production deployment state must be reconciled with Databricks, Unity Catalog, Azure Data Factory, Azure infrastructure, and Power BI metadata.",
            "- Sensitive references are counted and categorized; secret values are not extracted.",
            "",
            "The complete generated metadata file is `architecture-lens/metadata/inventory.json`.",
        ]
    )

    write_markdown(BOOK_SRC / "appendices" / "repository-inventory.md", lines)


def write_notebook_catalog(inventory: dict) -> None:
    notebooks = inventory["notebooks"]
    by_layer = inventory["counts"]["by_layer"]
    top_domains = Counter(inventory["counts"]["by_domain"]).most_common(20)

    lines = [
        "# Notebook Catalog",
        "",
        f"Generated from `{inventory['source']}` on {inventory['generated_on']}.",
        "",
        "The catalog contains every Python file under the Databricks `notebooks/` tree. It is an evidence index; each record still requires owner validation before it is treated as production truth.",
        "",
        "## Summary by layer",
        "",
        "| Layer | Notebook count |",
        "|---|---:|",
    ]

    for layer, count in sorted(by_layer.items()):
        lines.append(f"| {md(layer)} | {count} |")

    lines.extend(["", "## Top discovered domains", "", "| Domain | Notebook count |", "|---|---:|"])
    for domain, count in top_domains:
        lines.append(f"| {md(domain)} | {count} |")

    lines.extend(
        [
            "",
            "## Notebook index",
            "",
            "| ID | Layer | Domain | Notebook | Widgets | Tables | Secrets | Runs |",
            "|---|---|---|---|---:|---:|---:|---:|",
        ]
    )

    for record in notebooks:
        lines.append(
            "| "
            + " | ".join(
                [
                    md(record["id"]),
                    md(record["layer"]),
                    md(record["domain"]),
                    f"`{md(record['path'])}`",
                    str(len(record["widgets"])),
                    str(len(record["table_references"])),
                    str(record["secret_references"]),
                    str(len(record["notebook_runs"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Required validation",
            "",
            "- Confirm whether each notebook is deployed, scheduled, active, obsolete, or duplicate.",
            "- Reconcile generated table and path references with runtime lineage.",
            "- Assign owner, support group, classification, and modernization disposition.",
            "- Promote validated records into domain architecture packages.",
        ]
    )

    write_markdown(BOOK_SRC / "processing" / "notebook-catalog.md", lines)


def write_function_catalog(inventory: dict) -> None:
    functions = inventory["functions"]
    groups = inventory["counts"]["functions_by_group"]

    lines = [
        "# Function Catalog",
        "",
        f"Generated from `{inventory['source']}` on {inventory['generated_on']}.",
        "",
        "This catalog lists explicit Python function declarations discovered by static parsing. Dynamic functions, SQL objects, imported package behavior, and runtime monkey-patching require separate discovery.",
        "",
        "## Summary by group",
        "",
        "| Group | Function count |",
        "|---|---:|",
    ]

    for group, count in sorted(groups.items()):
        lines.append(f"| {md(group)} | {count} |")

    lines.extend(
        [
            "",
            "## Function index",
            "",
            "| ID | Group | Function | Path | Line |",
            "|---|---|---|---|---:|",
        ]
    )

    for record in functions:
        path_with_line = f"{record['path']}:{record['line']}"
        lines.append(
            "| "
            + " | ".join(
                [
                    md(record["id"]),
                    md(record["group"]),
                    f"`{md(record['signature'])}`",
                    f"`{md(path_with_line)}`",
                    str(record["line"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Required validation",
            "",
            "- Identify shared functions that are production-critical versus domain-local helpers.",
            "- Document inputs, outputs, side effects, failure behavior, security behavior, and modernization disposition using the function template.",
            "- Reconcile static call relationships with notebook execution paths and job parameters.",
        ]
    )

    write_markdown(BOOK_SRC / "processing" / "function-catalog.md", lines)


def write_job_catalog(inventory: dict) -> None:
    jobs = inventory["jobs"]

    lines = [
        "# Job Catalog",
        "",
        f"Generated from `{inventory['source']}` on {inventory['generated_on']}.",
        "",
        "This catalog lists Databricks job JSON definitions present in repository evidence. Deployment and schedule state must be reconciled with Databricks Jobs API output before use as production truth.",
        "",
        "| ID | Job | Tasks | Notebooks | Parameters | Run as |",
        "|---|---|---:|---|---:|---|",
    ]

    for record in jobs:
        notebook_paths = sorted(
            task["notebook_path"] for task in record["tasks"] if task["notebook_path"]
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    md(record["id"]),
                    f"`{md(record['name'])}`",
                    str(record["task_count"]),
                    "<br>".join(f"`{md(path)}`" for path in notebook_paths) or "None detected",
                    str(len(record["parameters"])),
                    md(record["run_as"] or "Not declared"),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Required validation",
            "",
            "- Reconcile repository job definitions with deployed Databricks jobs in development, test, and production.",
            "- Confirm schedules, triggers, retries, permissions, owners, alerts, and run identities.",
            "- Map each job task to notebook records, data movement records, and operational support procedures.",
        ]
    )

    write_markdown(BOOK_SRC / "processing" / "job-catalog.md", lines)


def write_adf_orchestration_catalog(inventory: dict) -> None:
    adf = inventory["adf"]
    pipelines = adf["pipelines"]
    triggers = adf["triggers"]
    resources = adf["resources"]
    activity_types = Counter(inventory["counts"]["adf_activity_types"])
    resource_types = Counter(inventory["counts"]["adf_resource_types"])

    lines = [
        "# ADF Orchestration Catalog",
        "",
        f"Generated from `{adf['source'] or 'not available'}` on {inventory['generated_on']}.",
        "",
        "This catalog treats Azure Data Factory as current-state orchestration evidence only. The target direction is to migrate orchestration into Databricks-native jobs while preserving the complete source-to-consumer flow semantics.",
        "",
        "## Summary",
        "",
        "| Artifact | Count |",
        "|---|---:|",
        f"| Pipelines | {len(pipelines)} |",
        f"| Schedule triggers | {len(triggers)} |",
        f"| Datasets | {sum(1 for record in resources if record['resource_kind'] == 'dataset')} |",
        f"| Linked services | {sum(1 for record in resources if record['resource_kind'] == 'linkedService')} |",
        f"| Integration runtimes | {sum(1 for record in resources if record['resource_kind'] == 'integrationRuntime')} |",
        "",
        "## Activity types",
        "",
        "| Activity type | Count |",
        "|---|---:|",
    ]

    for activity_type, count in activity_types.most_common():
        lines.append(f"| {md(activity_type)} | {count} |")

    lines.extend(["", "## Resource types", "", "| Resource type | Count |", "|---|---:|"])
    for resource_type, count in resource_types.most_common():
        lines.append(f"| {md(resource_type)} | {count} |")

    lines.extend(
        [
            "",
            "## Trigger index",
            "",
            "| ID | Trigger | State | Schedule | Pipelines |",
            "|---|---|---|---|---|",
        ]
    )
    for trigger in triggers:
        schedule = " ".join(
            part
            for part in [
                trigger["frequency"],
                f"every {trigger['interval']}" if trigger["interval"] else "",
                trigger["time_zone"],
            ]
            if part
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    md(trigger["id"]),
                    f"`{md(trigger['name'])}`",
                    md(trigger["runtime_state"] or "Unknown"),
                    md(schedule or "Not declared"),
                    "<br>".join(f"`{md(name)}`" for name in trigger["pipelines"])
                    or "None detected",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Pipeline index",
            "",
            "| ID | Pipeline | Activities | Key activity types | Calls pipelines | Databricks notebooks | Linked services | Datasets |",
            "|---|---|---:|---|---:|---:|---:|---:|",
        ]
    )
    for pipeline in pipelines:
        key_types = Counter(pipeline["activity_types"]).most_common(4)
        type_text = "<br>".join(f"{md(name)} ({count})" for name, count in key_types)
        lines.append(
            "| "
            + " | ".join(
                [
                    md(pipeline["id"]),
                    f"`{md(pipeline['name'])}`",
                    str(pipeline["activity_count"]),
                    type_text or "None detected",
                    str(len(pipeline["pipeline_references"])),
                    str(len(pipeline["notebook_paths"])),
                    str(len(pipeline["linked_services"])),
                    str(len(pipeline["datasets"])),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Required validation",
            "",
            "- Confirm which triggers are active in production; repository `runtimeState` alone is not sufficient.",
            "- Reconcile ADF pipeline definitions with Databricks Jobs, notebook paths, metadata tables, and runtime execution logs.",
            "- Preserve operational semantics during migration: trigger cadence, dependency conditions, retries, alerts, logging, and restart behavior.",
            "- Identify ADF-only connectors or integration runtimes that need a Databricks-native replacement pattern.",
        ]
    )

    write_markdown(BOOK_SRC / "processing" / "adf-orchestration-catalog.md", lines)


def write_metadata_dependency_catalog(inventory: dict) -> None:
    adf = inventory["adf"]
    metadata_queries = adf["metadata_queries"]
    field_usages = adf["metadata_field_usages"]
    metadata_tables = Counter(inventory["counts"]["adf_metadata_tables"])
    query_categories = Counter(inventory["counts"]["adf_metadata_query_categories"])

    lines = [
        "# Metadata Dependency Catalog",
        "",
        f"Generated from ADF pipeline query evidence on {inventory['generated_on']}.",
        "",
        "This catalog identifies the Azure SQL metadata tables, query patterns, and `item().field` values that currently drive ADF fan-out, notebook paths, job IDs, source queries, and object-level processing behavior.",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Metadata/query expressions | {len(metadata_queries)} |",
        f"| Distinct `item().field` references | {len(field_usages)} |",
        f"| Distinct metadata tables referenced | {len(metadata_tables)} |",
        "",
        "## Metadata tables",
        "",
        "| Table | Query count |",
        "|---|---:|",
    ]

    for table, count in metadata_tables.most_common():
        lines.append(f"| `{md(table)}` | {count} |")

    lines.extend(["", "## Query categories", "", "| Category | Query count |", "|---|---:|"])
    for category, count in query_categories.most_common():
        lines.append(f"| {md(category)} | {count} |")

    lines.extend(
        [
            "",
            "## High-use metadata fields",
            "",
            "| Field | Uses | Pipelines | Sample expressions |",
            "|---|---:|---:|---|",
        ]
    )
    for record in field_usages[:40]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{md(record['field'])}`",
                    str(record["use_count"]),
                    str(record["pipeline_count"]),
                    "<br>".join(f"`{md(sample)}`" for sample in record["sample_expressions"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Metadata query index",
            "",
            "| ID | Pipeline | Category | Metadata tables | Source type filters | Item fields |",
            "|---|---|---|---|---|---|",
        ]
    )
    for record in metadata_queries:
        lines.append(
            "| "
            + " | ".join(
                [
                    md(record["id"]),
                    f"`{md(record['pipeline'])}`",
                    md(record["category"]),
                    "<br>".join(f"`{md(table)}`" for table in record["metadata_tables"])
                    or "None detected",
                    "<br>".join(f"`{md(value)}`" for value in record["data_source_types"])
                    or "None detected",
                    "<br>".join(f"`{md(field)}`" for field in record["item_fields"][:8])
                    or "None detected",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Required validation",
            "",
            "- Export the actual metadata rows for `adf.DataSource`, `adf.DataProcess`, and `adf.DataProcessDependency` from the governed Azure SQL metadata database.",
            "- Confirm which metadata fields are authoritative versus legacy or unused.",
            "- Resolve dynamic notebook paths and Databricks job IDs before creating production Databricks task definitions.",
            "- Preserve process dependency, retry, logging, row-count validation, and notification semantics during migration.",
            "",
            "The machine-readable dependency file is `architecture-lens/metadata/metadata-dependencies.json`.",
        ]
    )

    write_markdown(BOOK_SRC / "data" / "metadata-dependency-catalog.md", lines)


def write_current_flow_graph(inventory: dict) -> None:
    graph = inventory["flow_graph"]
    flow_summaries = graph["flow_summaries"]
    active_flows = [
        summary for summary in flow_summaries if summary["runtime_state"].lower() == "started"
    ]
    top_by_activity = sorted(
        flow_summaries, key=lambda summary: summary["activity_count"], reverse=True
    )[:15]

    lines = [
        "# Current-State Flow Graph",
        "",
        f"Generated from Databricks and ADF evidence on {inventory['generated_on']}.",
        "",
        "This graph is the current-state execution map used to understand whole data flows before migration. It records orchestration relationships as evidence; runtime behavior still requires validation against platform run history.",
        "",
        "## Graph summary",
        "",
        "| Metric | Count |",
        "|---|---:|",
        f"| Nodes | {graph['summary']['node_count']} |",
        f"| Edges | {graph['summary']['edge_count']} |",
        f"| ADF triggers | {graph['summary']['trigger_count']} |",
        f"| ADF pipelines | {graph['summary']['pipeline_count']} |",
        f"| Started trigger records | {len(active_flows)} |",
        "",
        "## Edge semantics",
        "",
        "| Edge type | Meaning |",
        "|---|---|",
        "| `schedules` | A trigger starts a root pipeline |",
        "| `contains_activity` | A pipeline contains an ADF activity |",
        "| `depends_on` | An ADF activity depends on another activity in the same pipeline |",
        "| `executes_pipeline` / `calls_pipeline` | An activity or pipeline invokes a child pipeline |",
        "| `runs_notebook` / `invokes_notebook` | An activity or pipeline invokes a Databricks notebook path |",
        "| `runs_databricks_job` / `invokes_databricks_job` | An activity or pipeline invokes a Databricks job reference |",
        "| `uses_dataset` / `uses_linked_service` | ADF execution uses a dataset or linked service |",
        "",
        "## Trigger flow summaries",
        "",
        "| Trigger | State | Root pipelines | Reachable pipelines | Activities | Notebooks | Job refs | Datasets | Services | Complexity | Recommended wave |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]

    for summary in flow_summaries:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{md(summary['trigger_name'])}`",
                    md(summary["runtime_state"] or "Unknown"),
                    str(len(summary["root_pipelines"])),
                    str(summary["pipeline_count"]),
                    str(summary["activity_count"]),
                    str(summary["notebook_path_count"]),
                    str(summary["databricks_job_ref_count"]),
                    str(summary["dataset_count"]),
                    str(summary["linked_service_count"]),
                    md(summary["complexity"]),
                    md(summary["recommended_wave"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Largest trigger flows",
            "",
            "| Trigger | State | Pipelines | Activities | Key blockers |",
            "|---|---|---:|---:|---|",
        ]
    )
    for summary in top_by_activity:
        blockers = ", ".join(summary["blockers"]) if summary["blockers"] else "None detected"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{md(summary['trigger_name'])}`",
                    md(summary["runtime_state"] or "Unknown"),
                    str(summary["pipeline_count"]),
                    str(summary["activity_count"]),
                    md(blockers),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Known limitations",
            "",
            "- Dynamic notebook paths such as `@item().dataProcessPathOrProcedure` are preserved as expressions until metadata-table evidence is loaded.",
            "- Repository trigger `runtimeState` may not match deployed production state.",
            "- ADF `Copy` activity source and sink semantics require dataset and linked-service parameter resolution before final data movement records are generated.",
            "- The graph captures orchestration topology, not row-level lineage or business transformation rules.",
            "",
            "The machine-readable graph is `architecture-lens/metadata/flow-graph.json`.",
        ]
    )

    write_markdown(BOOK_SRC / "processing" / "current-flow-graph.md", lines)


def write_orchestration_migration_plan(inventory: dict) -> None:
    adf = inventory["adf"]
    pipelines = adf["pipelines"]
    triggers = adf["triggers"]
    activity_types = Counter(inventory["counts"]["adf_activity_types"])

    databricks_pipeline_count = sum(1 for pipeline in pipelines if pipeline["notebook_paths"])
    execute_pipeline_count = activity_types.get("ExecutePipeline", 0)
    copy_count = activity_types.get("Copy", 0)

    lines = [
        "# ADF to Databricks Orchestration Migration",
        "",
        f"Generated from current-state ADF evidence on {inventory['generated_on']}.",
        "",
        "ADF is the current-state orchestration reference. It should be used to reconstruct the full flow graph, trigger cadence, parameters, dependency conditions, error handling, and platform touchpoints. It is not the target orchestration platform for modernization.",
        "",
        "## Current-state migration inventory",
        "",
        "| Signal | Count | Migration meaning |",
        "|---|---:|---|",
        f"| ADF schedule triggers | {len(triggers)} | Candidate Databricks schedules or external event triggers |",
        f"| ADF pipelines | {len(pipelines)} | Candidate Databricks job definitions, job tasks, or reusable task groups |",
        f"| Pipelines invoking Databricks notebooks | {databricks_pipeline_count} | Direct candidates for Databricks job task migration |",
        f"| ExecutePipeline activities | {execute_pipeline_count} | Current dependency graph that must become job-task dependencies or job chaining |",
        f"| Copy activities | {copy_count} | Connector movement requiring replacement with Databricks ingestion, Auto Loader, volumes, or source-specific loaders |",
        "",
        "## Migration principles",
        "",
        "- Preserve current business flow semantics before optimizing implementation.",
        "- Convert ADF triggers into explicit Databricks schedules, event triggers, or upstream dependency contracts.",
        "- Convert `ExecutePipeline` chains into Databricks job task dependencies where the execution boundary is still useful.",
        "- Collapse orchestration-only wrapper pipelines when they add no retry, branching, logging, or ownership behavior.",
        "- Replace ADF copy activities with Databricks-native ingestion patterns only after source connectivity, identity, replay, and observability are designed.",
        "- Keep metadata-driven batch behavior, but move metadata reads, fan-out, logging, and status updates into a governed Databricks orchestration pattern.",
        "- Treat self-hosted integration runtime and private endpoint dependencies as migration blockers until replacement network paths are validated.",
        "",
        "## Target mapping",
        "",
        "| Current ADF construct | Databricks target construct | Validation required |",
        "|---|---|---|",
        "| Schedule trigger | Databricks job schedule or event trigger | Time zone, disabled/enabled state, calendar rules, missed-run behavior |",
        "| Pipeline | Databricks job or reusable workflow pattern | Owner, parameters, retry policy, notifications, permissions |",
        "| ExecutePipeline | Job task dependency or explicit downstream job trigger | Dependency conditions, wait behavior, failure propagation |",
        "| DatabricksNotebook activity | Databricks notebook task | Notebook path, parameters, cluster/serverless target, run identity |",
        "| Lookup / ForEach metadata fan-out | Databricks task values, dynamic jobs, or metadata-driven driver notebook | Concurrency, ordering, partial retry, audit events |",
        "| Copy activity | Databricks ingestion task | Connector parity, credentials, checkpointing, schema drift, replay |",
        "| Stored procedure logging | Databricks system tables, Delta operational log, or retained metadata DB logging | Run correlation, alert routing, audit retention |",
        "| Linked service / dataset | Unity Catalog external location, secret scope, connection, or source contract | Authentication, network path, secret ownership, classification |",
        "",
        "## Phased approach",
        "",
        "1. Generate and validate the ADF flow graph from trigger to terminal pipeline activity.",
        "2. Select one low-risk scheduled flow and one complex metadata-driven flow as migration pilots.",
        "3. Create Databricks job definitions that reproduce the ADF trigger, parameters, task dependencies, retries, and notifications.",
        "4. Run ADF and Databricks orchestration in parallel against controlled data windows.",
        "5. Reconcile row counts, data quality checks, runtime metrics, and consumer-visible outputs.",
        "6. Cut over scheduling only after rollback, monitoring, support ownership, and security evidence are approved.",
        "7. Retire ADF triggers, pipelines, linked services, datasets, and support procedures for migrated flows.",
        "",
        "## Open decisions",
        "",
        "- Confirm the target Databricks orchestration surface and naming standard for jobs, tasks, schedules, and reusable workflow components.",
        "- Decide whether metadata-driven fan-out remains a driver-notebook pattern or becomes generated job/task configuration.",
        "- Decide which ADF copy patterns should become Databricks ingestion code versus separate source-system integration services.",
        "- Define the production cutover gate for each migrated flow.",
    ]

    write_markdown(BOOK_SRC / "modernization" / "adf-to-databricks-orchestration.md", lines)


def write_dynamic_resolution_plan(inventory: dict) -> None:
    metadata_queries = inventory["adf"]["metadata_queries"]
    field_usages = inventory["adf"]["metadata_field_usages"]
    metadata_tables = Counter(inventory["counts"]["adf_metadata_tables"])
    required_fields = {record["field"] for record in field_usages}
    dynamic_path_fields = [
        field
        for field in sorted(required_fields)
        if field
        in {
            "dataProcessPathOrProcedure",
            "job_id",
            "dataSourceName",
            "objectName",
            "objectSchema",
            "destinationObjectName",
            "destinationObjectSchema",
        }
    ]

    lines = [
        "# Dynamic Metadata Resolution Plan",
        "",
        f"Generated from ADF metadata dependency evidence on {inventory['generated_on']}.",
        "",
        "The current ADF design relies on metadata-driven fan-out. Dynamic values such as `@item().dataProcessPathOrProcedure`, object schema/name, source query, data-source type, job ID, and process dependencies must be resolved before the ADF flow graph can become concrete Databricks job/task definitions.",
        "",
        "## Required metadata extracts",
        "",
        "| Metadata table | Why it is required |",
        "|---|---|",
        "| `adf.DataSource` | Source system, object, connector, query, path, incremental, watermark, and landing behavior |",
        "| `adf.DataProcess` | Notebook/procedure path, destination object, silver/gold processing, job/task parameters, and process enablement |",
        "| `adf.DataProcessDependency` | Ordering rules between source, bronze, silver, and gold processing steps |",
        "| `adf.operationMetricLog` | Current logging and row-count validation contract that must be reproduced or replaced |",
        "| `adf.azureResources` | Logic App, Data Factory, and notification endpoints referenced by support workflows |",
        "",
        "## Observed metadata query coverage",
        "",
        "| Table | Query count |",
        "|---|---:|",
    ]
    for table, count in metadata_tables.most_common():
        lines.append(f"| `{md(table)}` | {count} |")

    lines.extend(
        [
            "",
            "## Dynamic field priorities",
            "",
            "| Priority | Field | Migration purpose |",
            "|---|---|---|",
        ]
    )
    for field in dynamic_path_fields:
        purpose = {
            "dataProcessPathOrProcedure": "Resolve Databricks notebook/procedure path for task creation",
            "job_id": "Resolve Databricks job references used by serverless ADF activities",
            "dataSourceName": "Group source objects and derive landing paths",
            "objectName": "Resolve source object and landing object names",
            "objectSchema": "Resolve source schema and query scope",
            "destinationObjectName": "Resolve target object names for bronze/silver/gold tasks",
            "destinationObjectSchema": "Resolve target schemas for bronze/silver/gold tasks",
        }.get(field, "Resolve metadata-driven orchestration behavior")
        lines.append(f"| High | `{md(field)}` | {md(purpose)} |")

    lines.extend(
        [
            "",
            "## Resolution workflow",
            "",
            "1. Export governed snapshots of the required ADF metadata tables from each environment.",
            "2. Store sanitized snapshots as controlled evidence or load them through a secure connector; do not commit secrets or sensitive connection strings.",
            "3. Join ADF lookup queries to metadata rows to resolve object-level fan-out.",
            "4. Replace dynamic notebook expressions with concrete Databricks notebook task references where possible.",
            "5. Convert process dependencies into Databricks task dependencies or generated job definitions.",
            "6. Recompute the flow graph with resolved nodes for source object, target object, notebook, job, and task.",
            "7. Use the resolved graph to select pilot migrations and parallel-run reconciliation windows.",
            "",
            "## Databricks target model",
            "",
            "| Current metadata behavior | Databricks-native replacement |",
            "|---|---|",
            "| ADF lookup over `adf.DataSource` | Versioned source contract table or generated job config in Unity Catalog/Repo |",
            "| ADF `ForEach` over metadata rows | Databricks job tasks, generated workflows, or driver notebook with explicit task values |",
            "| `dataProcessPathOrProcedure` | Notebook task path or Python wheel task entry point |",
            "| `DataProcessDependency` | Databricks task dependency graph |",
            "| `operationMetricLog` stored procedures | Delta operational log plus Databricks run/task system tables, or retained metadata DB writes during transition |",
            "| Logic App email notifications | Databricks notifications, alerting integration, or governed incident workflow |",
            "",
            "## Open questions",
            "",
            "- Which environment has the authoritative production metadata rows?",
            "- Which metadata rows are active versus retained for historical or manual processing?",
            "- Which `dataProcessPathOrProcedure` values map to notebooks, SQL procedures, or obsolete implementations?",
            "- Should Databricks jobs be generated from metadata at deployment time or should metadata be read at runtime by driver tasks?",
            "- Which operational logs must remain in Azure SQL during transition for audit or support continuity?",
        ]
    )

    if metadata_queries:
        source_categories = Counter(record["category"] for record in metadata_queries)
        lines.extend(["", "## Query category summary", "", "| Category | Query count |", "|---|---:|"])
        for category, count in source_categories.most_common():
            lines.append(f"| {md(category)} | {count} |")

    write_markdown(BOOK_SRC / "modernization" / "dynamic-metadata-resolution.md", lines)


def write_adf_migration_waves(inventory: dict) -> None:
    flow_summaries = inventory["flow_graph"]["flow_summaries"]
    waves: dict[str, list[dict]] = defaultdict(list)
    for summary in flow_summaries:
        waves[summary["recommended_wave"]].append(summary)

    lines = [
        "# ADF Migration Waves",
        "",
        f"Generated from current-state flow graph evidence on {inventory['generated_on']}.",
        "",
        "These waves are an initial planning aid. They group ADF-triggered flows by orchestration complexity and migration blockers. Final migration sequencing requires owner, runtime, data-volume, CUI, and consumer-impact validation.",
        "",
        "## Wave definitions",
        "",
        "| Wave | Initial meaning | Exit criteria |",
        "|---|---|---|",
        "| Wave 0 - foundations | Shared Databricks orchestration standards, logging, alerting, identity, permissions, deployment, and evidence model | New Databricks jobs can be created, deployed, observed, and audited consistently |",
        "| Wave 1 - schedule and notebook task migration | Flows without detected ADF copy replacement work; dynamic paths, metadata fan-out, and notification behavior may still require resolution | Databricks schedule and task graph reproduces trigger cadence, parameters, dependencies, retries, and notifications |",
        "| Wave 2 - ingestion replacement | Flows with ADF copy activities but no detected filesystem/SFTP blocker | Databricks-native ingestion pattern is implemented with replay, quality, and observability |",
        "| Wave 3 - connector and network replacement | Flows using filesystem, SFTP, self-hosted integration runtime, or other network-sensitive access | Replacement connectivity, credentials, and private network paths are validated |",
        "",
        "## Generated wave candidates",
    ]

    for wave_name in sorted(waves):
        candidates = sorted(
            waves[wave_name],
            key=lambda summary: (summary["complexity"], -summary["activity_count"], summary["trigger_name"]),
        )
        lines.extend(
            [
                "",
                f"### {wave_name}",
                "",
                "| Trigger | State | Complexity | Pipelines | Activities | Blockers |",
                "|---|---|---|---:|---:|---|",
            ]
        )
        for summary in candidates:
            blockers = ", ".join(summary["blockers"]) if summary["blockers"] else "None detected"
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{md(summary['trigger_name'])}`",
                        md(summary["runtime_state"] or "Unknown"),
                        md(summary["complexity"]),
                        str(summary["pipeline_count"]),
                        str(summary["activity_count"]),
                        md(blockers),
                    ]
                )
                + " |"
            )

    lines.extend(
        [
            "",
            "## Validation checklist per flow",
            "",
            "- Confirm deployed trigger state, schedule, time zone, and business owner.",
            "- Resolve dynamic metadata-driven notebook paths and Databricks job IDs.",
            "- Document all source and sink datasets, linked services, secrets, and network paths.",
            "- Reproduce dependency conditions, retries, timeout behavior, alerts, and logging in Databricks.",
            "- Define parallel-run reconciliation and rollback before cutover.",
            "- Confirm decommission actions for ADF triggers, pipelines, linked services, datasets, and support runbooks.",
        ]
    )

    write_markdown(BOOK_SRC / "modernization" / "adf-migration-waves.md", lines)


def build_job_notebook_relationships(jobs: list[JobRecord]) -> dict[str, list[str]]:
    return {
        job.id: sorted(task.notebook_path for task in job.tasks if task.notebook_path)
        for job in jobs
    }


def job_to_dict(record: JobRecord) -> dict:
    payload = asdict(record)
    payload["tasks"] = [asdict(task) for task in record.tasks]
    return payload


def adf_pipeline_to_dict(record: AdfPipelineRecord) -> dict:
    payload = asdict(record)
    payload["activities"] = [asdict(activity) for activity in record.activities]
    return payload


def extract_function_names(source: str) -> list[str]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    return sorted(
        node.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )


def extract_widgets(source: str) -> list[str]:
    pattern = re.compile(r"dbutils\.widgets\.(?:text|dropdown|combobox|multiselect)\(\s*['\"]([^'\"]+)")
    return pattern.findall(source)


def extract_table_references(source: str) -> list[str]:
    patterns = [
        r"\bspark\.table\(\s*['\"]([^'\"]+)['\"]",
        r"\bsaveAsTable\(\s*['\"]([^'\"]+)['\"]",
        r"\b(?:FROM|JOIN|INTO|UPDATE|MERGE\s+INTO|TABLE)\s+([`A-Za-z0-9_.${}-]+)",
    ]
    refs: list[str] = []
    for pattern in patterns:
        refs.extend(match.strip("`") for match in re.findall(pattern, source, flags=re.IGNORECASE))
    return [ref for ref in refs if looks_like_table_reference(ref)]


def extract_secret_references(source: str) -> list[str]:
    return re.findall(r"dbutils\.secrets\.get\(", source)


def extract_notebook_runs(source: str) -> list[str]:
    pattern = re.compile(r"dbutils\.notebook\.run\(\s*([^,\n]+)")
    return [clean_expression(match) for match in pattern.findall(source)]


def looks_like_table_reference(value: str) -> bool:
    if not value or value.startswith(("$", "{")):
        return False
    if value.upper() in {"SELECT", "WHERE", "VALUES", "USING"}:
        return False
    return "." in value or "_" in value


def format_signature(source: str, node: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    args = []
    positional = list(node.args.posonlyargs) + list(node.args.args)
    defaults = [None] * (len(positional) - len(node.args.defaults)) + list(node.args.defaults)

    for arg, default in zip(positional, defaults):
        args.append(format_arg(source, arg, default))
    if node.args.vararg:
        args.append("*" + node.args.vararg.arg)
    for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
        args.append(format_arg(source, arg, default))
    if node.args.kwarg:
        args.append("**" + node.args.kwarg.arg)

    return f"{node.name}({', '.join(args)})"


def format_arg(source: str, arg: ast.arg, default: ast.expr | None) -> str:
    value = arg.arg
    if arg.annotation:
        annotation = ast.get_source_segment(source, arg.annotation) or "..."
        value += f": {annotation}"
    if default:
        default_text = ast.get_source_segment(source, default) or "..."
        value += f"={default_text}"
    return value


def classify_function(name: str) -> str:
    lowered = name.lower()
    if any(term in lowered for term in ("permission", "grant", "ownership", "pii", "rls", "access")):
        return "Security and access"
    if any(term in lowered for term in ("metric", "log", "audit", "operation")):
        return "Observability"
    if any(term in lowered for term in ("schema", "hash", "key", "column")):
        return "Schema and keys"
    if any(term in lowered for term in ("delta", "merge", "upsert", "dedup", "silver", "bronze")):
        return "Delta processing"
    if any(term in lowered for term in ("path", "file", "directory", "mount")):
        return "Filesystem"
    if any(term in lowered for term in ("environment", "workspace", "user", "notebook")):
        return "Runtime context"
    if any(term in lowered for term in ("flatten", "trim", "normalize", "clean")):
        return "Data normalization"
    return "Domain or utility"


def infer_layer(path: str) -> str:
    segments = path.split("/")
    for segment in segments:
        if re.match(r"^\d{3}_", segment):
            return segment
    if "data_engineering" in segments:
        data_engineering_index = segments.index("data_engineering")
        if data_engineering_index + 1 < len(segments) - 1:
            return segments[data_engineering_index + 1]
    return "unclassified"


def infer_domain(path: str, layer: str) -> str:
    segments = path.split("/")
    if layer in segments:
        layer_index = segments.index(layer)
        if layer_index + 1 < len(segments) - 1:
            return segments[layer_index + 1]
    stem = Path(path).stem
    stem = re.sub(r"^(source[-_]to[-_]raw|source[-_]to[-_]bronze|raw[-_]to[-_]bronze|bronze[-_]to[-_]silver|silver[-_]to[-_]gold)[-_]", "", stem)
    return stem.split("_")[0].split("-")[0] if stem else "unknown"


def read_text(archive: zipfile.ZipFile, path: str) -> str:
    return archive.read(path).decode("utf-8", errors="replace")


def strip_source_prefix(path: str) -> str:
    return path.removeprefix(SOURCE_PREFIX)


def clean_expression(value: str) -> str:
    value = value.strip()
    if (value.startswith("'") and value.endswith("'")) or (
        value.startswith('"') and value.endswith('"')
    ):
        return value[1:-1]
    return value


def md(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def make_json_safe(value):
    if isinstance(value, Counter):
        return dict(value)
    if isinstance(value, defaultdict):
        return dict(value)
    if isinstance(value, dict):
        return {key: make_json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [make_json_safe(item) for item in value]
    return value


def write_markdown(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
