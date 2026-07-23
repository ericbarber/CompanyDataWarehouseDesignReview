#!/usr/bin/env python3
"""Preflight generated Databricks workflow bundle candidates."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_SPECS = ROOT / "architecture-lens" / "workflow-specs"
MAX_FOR_EACH_INPUT_CHARS = 10_000


@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


def main() -> int:
    args = parse_args()
    paths = sorted(WORKFLOW_SPECS.glob("*.dev.bundle-resource.yml"))
    findings: list[Finding] = []

    if not paths:
        findings.append(
            Finding(
                "error",
                str(WORKFLOW_SPECS.relative_to(ROOT)),
                "No generated dev bundle resource candidates were found.",
            )
        )
    for path in paths:
        findings.extend(validate_bundle_candidate(path, strict_placeholders=args.strict_placeholders))

    errors = [finding for finding in findings if finding.severity == "error"]
    warnings = [finding for finding in findings if finding.severity == "warning"]

    if args.format == "json":
        print(
            json.dumps(
                {
                    "checked_files": [str(path.relative_to(ROOT)) for path in paths],
                    "error_count": len(errors),
                    "warning_count": len(warnings),
                    "findings": [finding.__dict__ for finding in findings],
                },
                indent=2,
                sort_keys=True,
            )
        )
    else:
        print(f"Checked {len(paths)} generated dev bundle resource candidate(s).")
        for finding in findings:
            print(f"{finding.severity.upper()}: {finding.path}: {finding.message}")
        if errors:
            print(f"Preflight failed with {len(errors)} error(s).")
        else:
            print(f"Preflight passed with {len(warnings)} warning(s).")

    return 1 if errors else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate generated Databricks dev bundle resource candidates."
    )
    parser.add_argument(
        "--strict-placeholders",
        action="store_true",
        help="Fail when TODO placeholder values remain in generated candidates.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    return parser.parse_args()


def validate_bundle_candidate(path: Path, strict_placeholders: bool) -> list[Finding]:
    findings: list[Finding] = []
    relpath = str(path.relative_to(ROOT))
    try:
        import yaml
    except ImportError:
        return [
            Finding(
                "error",
                relpath,
                "PyYAML is required to parse generated bundle YAML candidates.",
            )
        ]

    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [Finding("error", relpath, f"Unable to parse YAML: {exc}")]

    if not isinstance(document, dict):
        return [Finding("error", relpath, "YAML document must be an object.")]

    placeholder_paths = find_placeholder_paths(document)
    if placeholder_paths:
        severity = "error" if strict_placeholders else "warning"
        findings.append(
            Finding(
                severity,
                relpath,
                "Unresolved TODO placeholders: " + ", ".join(placeholder_paths[:25]),
            )
        )

    jobs = document.get("resources", {}).get("jobs", {})
    if not isinstance(jobs, dict) or not jobs:
        findings.append(Finding("error", relpath, "Expected resources.jobs to contain jobs."))
        return findings

    for job_key, job in jobs.items():
        job_path = f"{relpath}:resources.jobs.{job_key}"
        if not isinstance(job, dict):
            findings.append(Finding("error", job_path, "Job definition must be an object."))
            continue
        findings.extend(validate_job(job_path, job))

    return findings


def validate_job(path: str, job: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    name = str(job.get("name", ""))
    if not name.endswith("_dev_candidate"):
        findings.append(Finding("error", path, "Job name must end with _dev_candidate."))
    if "prod" in name.lower():
        findings.append(Finding("error", path, "Dev candidate job name must not reference prod."))

    tags = job.get("tags", {})
    if not isinstance(tags, dict):
        findings.append(Finding("error", path, "Job tags must be an object."))
    else:
        if tags.get("target_environment") != "dev":
            findings.append(Finding("error", path, "Job tag target_environment must be dev."))
        if tags.get("migration_status") != "candidate_not_deployed":
            findings.append(
                Finding("error", path, "Job tag migration_status must be candidate_not_deployed.")
            )

    schedule = job.get("schedule", {})
    if not isinstance(schedule, dict):
        findings.append(Finding("error", path, "Schedule must be an object."))
    elif schedule.get("pause_status") != "PAUSED":
        findings.append(Finding("error", path, "Generated dev candidate schedule must be PAUSED."))

    if job.get("max_concurrent_runs") != 1:
        findings.append(Finding("error", path, "max_concurrent_runs must be 1 for dev candidates."))

    run_as = job.get("run_as", {})
    if not isinstance(run_as, dict) or not run_as.get("service_principal_name"):
        findings.append(Finding("error", path, "run_as.service_principal_name is required."))

    tasks = job.get("tasks", [])
    if not isinstance(tasks, list) or not tasks:
        findings.append(Finding("error", path, "Job must contain at least one task."))
        return findings

    task_keys: set[str] = set()
    total_iterations = 0
    for task in tasks:
        if not isinstance(task, dict):
            findings.append(Finding("error", path, "Every task must be an object."))
            continue
        task_key = str(task.get("task_key", ""))
        task_path = f"{path}.tasks.{task_key or 'unknown'}"
        if not task_key:
            findings.append(Finding("error", task_path, "task_key is required."))
        if task_key in task_keys:
            findings.append(Finding("error", task_path, "task_key must be unique."))
        task_keys.add(task_key)
        findings.extend(validate_for_each_task(task_path, task))
        total_iterations += count_for_each_inputs(task)

    if total_iterations <= 0:
        findings.append(Finding("error", path, "For each inputs must contain at least one iteration."))

    return findings


def validate_for_each_task(path: str, task: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for_each = task.get("for_each_task")
    if not isinstance(for_each, dict):
        findings.append(Finding("error", path, "Expected for_each_task."))
        return findings

    concurrency = for_each.get("concurrency")
    if not isinstance(concurrency, int) or concurrency < 1 or concurrency > 8:
        findings.append(Finding("error", path, "for_each_task.concurrency must be between 1 and 8."))

    inputs = for_each.get("inputs", "")
    if not isinstance(inputs, str) or not inputs:
        findings.append(Finding("error", path, "for_each_task.inputs must be a JSON string."))
    elif len(inputs) > MAX_FOR_EACH_INPUT_CHARS:
        findings.append(
            Finding(
                "error",
                path,
                f"for_each_task.inputs exceeds {MAX_FOR_EACH_INPUT_CHARS} characters.",
            )
        )
    else:
        try:
            parsed_inputs = json.loads(inputs)
        except json.JSONDecodeError as exc:
            findings.append(Finding("error", path, f"for_each_task.inputs is not valid JSON: {exc}"))
        else:
            if not isinstance(parsed_inputs, list) or not parsed_inputs:
                findings.append(
                    Finding("error", path, "for_each_task.inputs must parse to a non-empty list.")
                )

    nested = for_each.get("task", {})
    if not isinstance(nested, dict):
        findings.append(Finding("error", path, "for_each_task.task must be an object."))
        return findings

    notebook_task = nested.get("notebook_task", {})
    if not isinstance(notebook_task, dict):
        findings.append(Finding("error", path, "Nested notebook_task must be an object."))
        return findings

    notebook_path = str(notebook_task.get("notebook_path", ""))
    if not notebook_path.startswith("/Workspace/"):
        findings.append(Finding("error", path, "notebook_task.notebook_path must start with /Workspace/."))

    base_parameters = notebook_task.get("base_parameters", {})
    required_parameters = {
        "object_schema",
        "object_name",
        "primary_key_column_list",
        "is_incremental",
        "pii_columns",
        "etl_silver_timestamp",
        "project_id_column",
        "julian_date_columns",
        "is_full_load",
        "is_snapshot",
        "snapshot_period",
        "debug_flag",
        "partition_by",
    }
    if not isinstance(base_parameters, dict):
        findings.append(Finding("error", path, "notebook_task.base_parameters must be an object."))
    else:
        missing = sorted(required_parameters - set(base_parameters))
        if missing:
            findings.append(
                Finding(
                    "error",
                    path,
                    "Missing notebook base parameters: " + ", ".join(missing),
                )
            )

    return findings


def count_for_each_inputs(task: dict[str, Any]) -> int:
    try:
        parsed = json.loads(task["for_each_task"]["inputs"])
    except Exception:
        return 0
    return len(parsed) if isinstance(parsed, list) else 0


def find_placeholder_paths(value: Any, prefix: str = "$") -> list[str]:
    paths: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            paths.extend(find_placeholder_paths(child, f"{prefix}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            paths.extend(find_placeholder_paths(child, f"{prefix}[{index}]"))
    elif isinstance(value, str) and "TODO_" in value:
        paths.append(prefix)
    return paths


if __name__ == "__main__":
    sys.exit(main())
