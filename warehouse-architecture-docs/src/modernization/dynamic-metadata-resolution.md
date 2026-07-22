# Dynamic Metadata Resolution Plan

Generated from ADF metadata dependency evidence on 2026-07-22.

The current ADF design relies on metadata-driven fan-out. Dynamic values such as `@item().dataProcessPathOrProcedure`, object schema/name, source query, data-source type, job ID, and process dependencies must be resolved before the ADF flow graph can become concrete Databricks job/task definitions.

## Required metadata extracts

| Metadata table | Why it is required |
|---|---|
| `adf.DataSource` | Source system, object, connector, query, path, incremental, watermark, and landing behavior |
| `adf.DataProcess` | Notebook/procedure path, destination object, silver/gold processing, job/task parameters, and process enablement |
| `adf.DataProcessDependency` | Ordering rules between source, bronze, silver, and gold processing steps |
| `adf.operationMetricLog` | Current logging and row-count validation contract that must be reproduced or replaced |
| `adf.azureResources` | Logic App, Data Factory, and notification endpoints referenced by support workflows |

## Observed metadata query coverage

| Table | Query count |
|---|---:|
| `adf.DataSource` | 62 |
| `adf.operationMetricLog` | 14 |
| `adf.azureResources` | 11 |
| `adf.powerBiDataset` | 2 |
| `adf.DataProcess` | 1 |
| `adf.DataProcessDependency` | 1 |

## Dynamic field priorities

| Priority | Field | Migration purpose |
|---|---|---|
| High | `dataProcessPathOrProcedure` | Resolve Databricks notebook/procedure path for task creation |
| High | `dataSourceName` | Group source objects and derive landing paths |
| High | `destinationObjectName` | Resolve target object names for bronze/silver/gold tasks |
| High | `destinationObjectSchema` | Resolve target schemas for bronze/silver/gold tasks |
| High | `objectName` | Resolve source object and landing object names |
| High | `objectSchema` | Resolve source schema and query scope |

## Resolution workflow

1. Export governed snapshots of the required ADF metadata tables from each environment.
2. Store sanitized snapshots as controlled evidence or load them through a secure connector; do not commit secrets or sensitive connection strings.
3. Join ADF lookup queries to metadata rows to resolve object-level fan-out.
4. Replace dynamic notebook expressions with concrete Databricks notebook task references where possible.
5. Convert process dependencies into Databricks task dependencies or generated job definitions.
6. Recompute the flow graph with resolved nodes for source object, target object, notebook, job, and task.
7. Use the resolved graph to select pilot migrations and parallel-run reconciliation windows.

## Databricks target model

| Current metadata behavior | Databricks-native replacement |
|---|---|
| ADF lookup over `adf.DataSource` | Versioned source contract table or generated job config in Unity Catalog/Repo |
| ADF `ForEach` over metadata rows | Databricks job tasks, generated workflows, or driver notebook with explicit task values |
| `dataProcessPathOrProcedure` | Notebook task path or Python wheel task entry point |
| `DataProcessDependency` | Databricks task dependency graph |
| `operationMetricLog` stored procedures | Delta operational log plus Databricks run/task system tables, or retained metadata DB writes during transition |
| Logic App email notifications | Databricks notifications, alerting integration, or governed incident workflow |

## Open questions

- Which environment has the authoritative production metadata rows?
- Which metadata rows are active versus retained for historical or manual processing?
- Which `dataProcessPathOrProcedure` values map to notebooks, SQL procedures, or obsolete implementations?
- Should Databricks jobs be generated from metadata at deployment time or should metadata be read at runtime by driver tasks?
- Which operational logs must remain in Azure SQL during transition for audit or support continuity?

## Query category summary

| Category | Query count |
|---|---:|
| Source metadata lookup | 62 |
| Per-object runtime query | 48 |
| Operational metrics lookup | 14 |
| Azure resource lookup | 11 |
| Other metadata query | 3 |
| Process metadata lookup | 1 |
| Process dependency lookup | 1 |
