# ADF Migration Waves

Generated from current-state flow graph evidence on 2026-07-22.

These waves are an initial planning aid. They group ADF-triggered flows by orchestration complexity and migration blockers. Final migration sequencing requires owner, runtime, data-volume, CUI, and consumer-impact validation.

## Wave definitions

| Wave | Initial meaning | Exit criteria |
|---|---|---|
| Wave 0 - foundations | Shared Databricks orchestration standards, logging, alerting, identity, permissions, deployment, and evidence model | New Databricks jobs can be created, deployed, observed, and audited consistently |
| Wave 1 - schedule and notebook task migration | Flows without detected ADF copy replacement work; dynamic paths, metadata fan-out, and notification behavior may still require resolution | Databricks schedule and task graph reproduces trigger cadence, parameters, dependencies, retries, and notifications |
| Wave 2 - ingestion replacement | Flows with ADF copy activities but no detected filesystem/SFTP blocker | Databricks-native ingestion pattern is implemented with replay, quality, and observability |
| Wave 3 - connector and network replacement | Flows using filesystem, SFTP, self-hosted integration runtime, or other network-sensitive access | Replacement connectivity, credentials, and private network paths are validated |

## Generated wave candidates

### Wave 1 - schedule and notebook task migration

| Trigger | State | Complexity | Pipelines | Activities | Blockers |
|---|---|---|---:|---:|---|
| `DEV_TEXTURA` | Started | Medium | 5 | 56 | dynamic_notebook_path, web_activity |
| `PROD_TEXTURA` | Stopped | Medium | 5 | 56 | dynamic_notebook_path, web_activity |
| `TEST_TEXTURA` | Stopped | Medium | 5 | 56 | dynamic_notebook_path, web_activity |
| `DEV_Bridgit_Reporting` | Started | Medium | 6 | 47 | dynamic_notebook_path, web_activity |
| `PROD_Bridgit_Reporting` | Stopped | Medium | 6 | 47 | dynamic_notebook_path, web_activity |
| `TEST_Bridgit_Reporting` | Stopped | Medium | 6 | 47 | dynamic_notebook_path, web_activity |
| `DEV_cslb_weekly` | Started | Medium | 4 | 40 | dynamic_notebook_path, web_activity |
| `PROD_cslb_weekly` | Stopped | Medium | 4 | 40 | dynamic_notebook_path, web_activity |
| `TEST_cslb_weekly` | Stopped | Medium | 4 | 40 | dynamic_notebook_path, web_activity |
| `DEV_MonthlyMaintenance` | Started | Medium | 2 | 12 | web_activity |
| `PROD_MonthlyMaintenance` | Stopped | Medium | 2 | 12 | web_activity |
| `TEST_MonthlyMaintenance` | Stopped | Medium | 2 | 12 | web_activity |

### Wave 2 - ingestion replacement

| Trigger | State | Complexity | Pipelines | Activities | Blockers |
|---|---|---|---:|---:|---|
| `DEV_Weekly` | Started | High | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_Daily` | Stopped | High | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_Weekly` | Stopped | High | 48 | 747 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_Security` | Stopped | High | 18 | 237 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_AM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_PM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_AM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_PM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_AM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_PM` | Stopped | High | 12 | 203 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_dailyHeavyJob` | Stopped | Medium | 8 | 101 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_DOCS_AM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_INEIGHT_DOCS_PM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_DOCS_AM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_INEIGHT_DOCS_PM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_DOCS_AM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_INEIGHT_DOCS_PM` | Stopped | Medium | 7 | 81 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_WeldOffice_weekly` | Stopped | Medium | 6 | 76 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_WeldOffice_weekly` | Stopped | Medium | 6 | 76 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_WeldOffice_weekly` | Stopped | Medium | 6 | 76 | copy_activity, dynamic_notebook_path, web_activity |
| `DEV_zip_monthly` | Started | Medium | 5 | 50 | copy_activity, dynamic_notebook_path, web_activity |
| `PROD_zip_monthly` | Stopped | Medium | 5 | 50 | copy_activity, dynamic_notebook_path, web_activity |
| `TEST_zip_monthly` | Stopped | Medium | 5 | 50 | copy_activity, dynamic_notebook_path, web_activity |

## Validation checklist per flow

- Confirm deployed trigger state, schedule, time zone, and business owner.
- Resolve dynamic metadata-driven notebook paths and Databricks job IDs.
- Document all source and sink datasets, linked services, secrets, and network paths.
- Reproduce dependency conditions, retries, timeout behavior, alerts, and logging in Databricks.
- Define parallel-run reconciliation and rollback before cutover.
- Confirm decommission actions for ADF triggers, pipelines, linked services, datasets, and support runbooks.
