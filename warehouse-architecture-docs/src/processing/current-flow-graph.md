# Current-State Flow Graph

Generated from Databricks and ADF evidence on 2026-07-22.

This graph is the current-state execution map used to understand whole data flows before migration. It records orchestration relationships as evidence; runtime behavior still requires validation against platform run history.

## Graph summary

| Metric | Count |
|---|---:|
| Nodes | 2427 |
| Edges | 7634 |
| ADF triggers | 35 |
| ADF pipelines | 118 |
| Started trigger records | 6 |

## Edge semantics

| Edge type | Meaning |
|---|---|
| `schedules` | A trigger starts a root pipeline |
| `contains_activity` | A pipeline contains an ADF activity |
| `depends_on` | An ADF activity depends on another activity in the same pipeline |
| `executes_pipeline` / `calls_pipeline` | An activity or pipeline invokes a child pipeline |
| `runs_notebook` / `invokes_notebook` | An activity or pipeline invokes a Databricks notebook path |
| `runs_databricks_job` / `invokes_databricks_job` | An activity or pipeline invokes a Databricks job reference |
| `uses_dataset` / `uses_linked_service` | ADF execution uses a dataset or linked service |

## Trigger flow summaries

| Trigger | State | Root pipelines | Reachable pipelines | Activities | Notebooks | Job refs | Datasets | Services | Complexity | Recommended wave |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| `DEV_Bridgit_Reporting` | Started | 3 | 6 | 47 | 4 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `DEV_INEIGHT_AM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `DEV_INEIGHT_DOCS_AM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `DEV_INEIGHT_DOCS_PM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `DEV_INEIGHT_PM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `DEV_MonthlyMaintenance` | Started | 1 | 2 | 12 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `DEV_Security` | Stopped | 1 | 18 | 237 | 5 | 0 | 7 | 3 | High | Wave 2 - ingestion replacement |
| `DEV_TEXTURA` | Started | 1 | 5 | 56 | 3 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `DEV_Weekly` | Started | 1 | 48 | 747 | 19 | 0 | 10 | 3 | High | Wave 2 - ingestion replacement |
| `DEV_WeldOffice_weekly` | Stopped | 1 | 6 | 76 | 4 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `DEV_cslb_weekly` | Started | 1 | 4 | 40 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `DEV_zip_monthly` | Started | 1 | 5 | 50 | 2 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `PROD_Bridgit_Reporting` | Stopped | 3 | 6 | 47 | 4 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `PROD_Daily` | Stopped | 1 | 48 | 747 | 19 | 0 | 10 | 3 | High | Wave 2 - ingestion replacement |
| `PROD_INEIGHT_AM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `PROD_INEIGHT_DOCS_AM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `PROD_INEIGHT_DOCS_PM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `PROD_INEIGHT_PM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `PROD_MonthlyMaintenance` | Stopped | 1 | 2 | 12 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `PROD_TEXTURA` | Stopped | 1 | 5 | 56 | 3 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `PROD_WeldOffice_weekly` | Stopped | 1 | 6 | 76 | 4 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `PROD_cslb_weekly` | Stopped | 1 | 4 | 40 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `PROD_dailyHeavyJob` | Stopped | 1 | 8 | 101 | 3 | 0 | 5 | 3 | Medium | Wave 2 - ingestion replacement |
| `PROD_zip_monthly` | Stopped | 1 | 5 | 50 | 2 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `TEST_Bridgit_Reporting` | Stopped | 3 | 6 | 47 | 4 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `TEST_INEIGHT_AM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `TEST_INEIGHT_DOCS_AM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `TEST_INEIGHT_DOCS_PM` | Stopped | 1 | 7 | 81 | 3 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `TEST_INEIGHT_PM` | Stopped | 1 | 12 | 203 | 5 | 0 | 4 | 3 | High | Wave 2 - ingestion replacement |
| `TEST_MonthlyMaintenance` | Stopped | 1 | 2 | 12 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `TEST_TEXTURA` | Stopped | 1 | 5 | 56 | 3 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `TEST_Weekly` | Stopped | 1 | 48 | 747 | 19 | 0 | 10 | 3 | High | Wave 2 - ingestion replacement |
| `TEST_WeldOffice_weekly` | Stopped | 1 | 6 | 76 | 4 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |
| `TEST_cslb_weekly` | Stopped | 1 | 4 | 40 | 2 | 0 | 1 | 3 | Medium | Wave 1 - schedule and notebook task migration |
| `TEST_zip_monthly` | Stopped | 1 | 5 | 50 | 2 | 0 | 3 | 3 | Medium | Wave 2 - ingestion replacement |

## Largest trigger flows

| Trigger | State | Pipelines | Activities | Key blockers |
|---|---|---:|---:|---|
| `DEV_Weekly` | Started | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_Daily` | Stopped | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_Weekly` | Stopped | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_Security` | Stopped | 18 | 237 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_AM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_PM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_AM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_PM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_AM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_PM` | Stopped | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_dailyHeavyJob` | Stopped | 8 | 101 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_DOCS_AM` | Stopped | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_DOCS_PM` | Stopped | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_DOCS_AM` | Stopped | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_DOCS_PM` | Stopped | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |

## Known limitations

- Dynamic notebook paths such as `@item().dataProcessPathOrProcedure` are preserved as expressions until metadata-table evidence is loaded.
- Repository trigger `runtimeState` may not match deployed production state.
- ADF `Copy` activity source and sink semantics require dataset and linked-service parameter resolution before final data movement records are generated.
- The graph captures orchestration topology, not row-level lineage or business transformation rules.

The machine-readable graph is `architecture-lens/metadata/flow-graph.json`.
