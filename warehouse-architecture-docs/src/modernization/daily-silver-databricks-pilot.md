# Daily Silver Databricks Pilot Spec

Generated from resolved metadata exports on 2026-07-22.

This page is the first concrete Databricks-native workflow specification for migrating ADF metadata fan-out. It targets the `dw2023_daily_silver` workflow candidate and preserves the existing `bronze_to_silver` notebook parameter contract.

## Pilot shape

| Signal | Value |
|---|---:|
| Metadata rows | 457 |
| Shards | 24 |
| Max iterations per shard | 21 |
| Max shard payload characters | 8992 |
| Iteration concurrency per shard | 8 |

## Job resource

| Field | Value |
|---|---|
| Job name | `dw2023_daily_silver_pilot` |
| Candidate | `dw2023_daily_silver` |
| Notebook | `/Workspace/data_engineering/200_bronze_to_silver/bronze_to_silver` |
| Status | design_spec_not_deployed |
| Shard execution | sequential |

## Source type coverage

| Source type | Iterations |
|---|---:|
| Azure SQL Database | 208 |
| SQL Server | 184 |
| REST API | 39 |
| Sharepoint List | 14 |
| Azure SQL Database - SDAT Web App | 4 |
| SOAP API | 3 |
| File System | 3 |
| API | 1 |
| SFTP File | 1 |

## Incremental coverage

| Incremental flag | Iterations |
|---|---:|
| 0 | 447 |
| 1 | 10 |

## Shards

| Shard task | Iterations | Payload chars | First target | Last target |
|---|---:|---:|---|---|
| `for_each_daily_silver_shard_001` | 20 | 8938 | silver_azureactivedirectory.users | silver_cosential.Opportunity_Consultants |
| `for_each_daily_silver_shard_002` | 19 | 8939 | silver_cosential.Opportunity_ContractType | silver_cosential.Project_Consultants_Contacts |
| `for_each_daily_silver_shard_003` | 20 | 8889 | silver_cosential.Project_CostFee | silver_cosential.Projects_ext |
| `for_each_daily_silver_shard_004` | 19 | 8617 | silver_cosential.Roles | silver_destimator.EstimateFeeDataDetails_forDW |
| `for_each_daily_silver_shard_005` | 21 | 8961 | silver_destimator.EstimateSummaryDataDetails_forDW | silver_e1.F06156 |
| `for_each_daily_silver_shard_006` | 18 | 8739 | silver_e1.F0618 | silver_e1.F4801T |
| `for_each_daily_silver_shard_007` | 20 | 8646 | silver_e1.F5144 | silver_ineight.vwAdvancedWorkPackaging |
| `for_each_daily_silver_shard_008` | 19 | 8796 | silver_ineight.vwBIContractVendorDetail | silver_ineight.vwComplianceQuestionText |
| `for_each_daily_silver_shard_009` | 19 | 8753 | silver_ineight.vwComplianceResponseType | silver_ineight.vwContractPCODetail |
| `for_each_daily_silver_shard_010` | 19 | 8899 | silver_ineight.vwContractPackageCustomField | silver_ineight.vwControlCorporateForecastDetail |
| `for_each_daily_silver_shard_011` | 19 | 8992 | silver_ineight.vwControlCorporateForecastRemainingDetail | silver_ineight.vwCoreCommodity |
| `for_each_daily_silver_shard_012` | 19 | 8674 | silver_ineight.vwCoreContact | silver_ineight.vwCoreUnion |
| `for_each_daily_silver_shard_013` | 20 | 8866 | silver_ineight.vwCoreUnitOfMeasure | silver_ineight.vwPlanComponent |
| `for_each_daily_silver_shard_014` | 19 | 8824 | silver_ineight.vwPlanComponentCharacteristic | silver_ineight.vwScheduleScheduleActivityCodeValueAssignment |
| `for_each_daily_silver_shard_015` | 18 | 8671 | silver_ineight.vwScheduleScheduleActivityConstraintType | silver_ineight.vwScheduleScheduleResourceCategory |
| `for_each_daily_silver_shard_016` | 19 | 8865 | silver_ineight.vwScheduleScheduleResourceCode | silver_ineight_document.SubmittalLinks |
| `for_each_daily_silver_shard_017` | 20 | 8843 | silver_ineight_document.SubmittalMilestoneDates | silver_nccer.credentials |
| `for_each_daily_silver_shard_018` | 21 | 8972 | silver_p6.ACTVCODE | silver_powerbi.activityevents |
| `for_each_daily_silver_shard_019` | 20 | 8864 | silver_powerbi.groups | silver_prolog.v_SundtDatawarehouse_DailyWork |
| `for_each_daily_silver_shard_020` | 19 | 8978 | silver_prolog.v_SundtDatawarehouse_DwActiveDirectoryUsersOneRow | silver_qdr.E1_ActualCost |
| `for_each_daily_silver_shard_021` | 20 | 8648 | silver_qdr.E1_ActualUnits | silver_qdr.QDR_ROOTCAUSE |
| `for_each_daily_silver_shard_022` | 20 | 8850 | silver_qdr.QDR_STATUS | silver_textura.invoicelines |
| `for_each_daily_silver_shard_023` | 19 | 8528 | silver_textura.invoices | silver_tradetapp.financials |
| `for_each_daily_silver_shard_024` | 10 | 4564 | silver_tradetapp.qualifications | silver_zipcodes.Zipcode_Update_Standard |

## Smoke-test subset

The smoke resource is generated from the same metadata but limits the first dev validation run to 10 representative daily silver objects. It is also paused and must not be promoted as the production schedule.

| Signal | Value |
|---|---:|
| Smoke rows | 10 |
| Smoke shards | 1 |
| Smoke iteration concurrency | 4 |
| Smoke max payload characters | 4349 |

### Smoke source coverage

| Source type | Iterations |
|---|---:|
| SQL Server | 2 |
| Azure SQL Database | 1 |
| REST API | 1 |
| Sharepoint List | 1 |
| Azure SQL Database - SDAT Web App | 1 |
| SOAP API | 1 |
| File System | 1 |
| API | 1 |
| SFTP File | 1 |

### Smoke targets

| Target | Source type | Incremental |
|---|---|---|
| silver_ineight.qry_complianceobsoleteuseremail | Azure SQL Database | 0 |
| silver_cosential.Companies | SQL Server | 0 |
| silver_azureactivedirectory.users | REST API | 0 |
| silver_b2g.B2G_XBE_Subcontractor_Commitments | Sharepoint List | 0 |
| silver_webapp.Audits | Azure SQL Database - SDAT Web App | 0 |
| silver_b2g.contract | SOAP API | 0 |
| silver_heavyjob.SCRDR_Equip | File System | 0 |
| silver_cslb.license_data | API | 0 |
| silver_zipcodes.Zipcode_Update_Standard | SFTP File | 0 |
| silver_e1.F0006 | SQL Server | 1 |

## Parameter mapping

| Existing notebook parameter | Pilot source |
|---|---|
| `object_schema` | `{{input.object_schema}}` |
| `object_name` | `{{input.object_name}}` |
| `primary_key_column_list` | `{{input.primary_key_column_list}}` |
| `is_incremental` | `{{input.is_incremental}}` |
| `pii_columns` | `{{input.pii_columns}}` |
| `etl_silver_timestamp` | `{{job.parameters.etl_silver_timestamp}}` |
| `project_id_column` | `{{input.project_id_column}}` |
| `julian_date_columns` | `{{input.julian_date_columns}}` |
| `is_full_load` | `{{job.parameters.is_full_load}}` |
| `is_snapshot` | `{{input.is_snapshot}}` |
| `snapshot_period` | `{{input.snapshot_period}}` |
| `debug_flag` | `{{job.parameters.debug_flag}}` |
| `partition_by` | `{{input.partition_by}}` |

## Design rationale

- Uses Databricks For each tasks to preserve object-level task visibility.
- Shards input arrays to stay below documented Databricks job parameter and For each input limits.
- Chains shards sequentially so total concurrent notebook iterations are bounded by the shard concurrency.
- Keeps the existing bronze_to_silver notebook parameter contract intact for the pilot.

## Validation gates

- Confirm deployed notebook path and source are valid in dev, test, and prod.
- Confirm cluster, serverless, policy, or warehouse settings before deployment.
- Confirm retry, timeout, notification, and run_as ownership with operations.
- Run a small subset shard in development before enabling all 457 metadata rows.
- Reconcile row counts and operation logs against the equivalent ADF daily silver run.

## Dev bundle candidate placeholders

| Placeholder | Required decision |
|---|---|
| `TODO_CONFIRM_DEV_COMPUTE_POLICY` | Confirm whether the pilot uses existing serverless behavior, a job cluster, or a governed dev compute policy |
| `TODO_CONFIRM_DEV_NOTIFICATION_DESTINATION` | Confirm the Databricks notification destination or support mailbox for failed pilot runs |
| `TODO_CONFIRM_WORKFLOW_OWNER` | Confirm the accountable support owner before the workflow is deployed |
| Paused schedule | Confirm the dev cron cadence and unpause only after the subset smoke run passes |
| Retry settings | Confirm whether one retry with five-minute spacing matches current ADF retry semantics |

Copy `architecture-lens/config/workflow-overrides.example.json` to `architecture-lens/config/workflow-overrides.json` and replace the local dev values to regenerate candidates without `TODO_` placeholders. The local override file is ignored by Git.

## Preflight commands

| Command | Purpose | Expected result now |
|---|---|---|
| `make validate` | Regenerate evidence, structurally check generated workflow specs, and build docs | Passes with placeholder warnings |
| `make workflow-preflight` | Run strict deploy-readiness checks on generated dev bundle candidates | Fails until `TODO_` placeholders are replaced |

## Evidence files

- `architecture-lens/workflow-specs/databricks-workflow-task-specs.json` contains the full generated task-spec evidence.
- `architecture-lens/workflow-specs/dw2023_daily_silver_pilot.job-resource.json` contains the generated Databricks job resource model for this pilot.
- `architecture-lens/workflow-specs/dw2023_daily_silver_pilot.dev.bundle-resource.yml` contains the dev-only Databricks Asset Bundle resource candidate.
- `architecture-lens/workflow-specs/dw2023_daily_silver_smoke.job-resource.json` contains the generated smoke-test job resource model.
- `architecture-lens/workflow-specs/dw2023_daily_silver_smoke.dev.bundle-resource.yml` contains the paused dev-only smoke-test bundle candidate.

## Databricks references

- Databricks Declarative Automation Bundles job task configuration: <https://docs.databricks.com/aws/en/dev-tools/bundles/job-task-types>
- Databricks For each task behavior and input limits: <https://docs.databricks.com/aws/en/jobs/tasks/for-each>
- Databricks dynamic value references for job and task parameters: <https://docs.databricks.com/aws/en/jobs/dynamic-value-references>

This is not deployment-ready until compute, identity, alerting, retry, timeout, schedule, and environment-specific governance settings are confirmed.
