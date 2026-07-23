# Databricks Workflow Candidates

Generated from resolved metadata exports on 2026-07-22.

This page translates active `DataProcess` and `DataProcessDependency` rows into initial Databricks workflow candidates. It is a design artifact for replacing ADF metadata fan-out with Databricks-native job/task orchestration.

## Summary

| Metric | Count |
|---|---:|
| Workflow candidates | 4 |
| Candidate tasks | 879 |
| Candidate dependency edges | 794 |
| Blocked candidates | 1 |

## Readiness

| Readiness | Candidates |
|---|---:|
| pilot_candidate | 3 |
| blocked_missing_notebooks | 1 |

## Candidate index

| Candidate | Batch | Process | Tasks | Resolved | Missing notebooks | Dependencies | Pattern | Readiness | Wave |
|---|---|---|---:|---:|---:|---:|---|---|---|
| `dw2023_daily_gold` | daily | gold | 403 | 373 | 30 | 794 | generated Databricks workflow task DAG | blocked_missing_notebooks | Wave 0 - artifact recovery |
| `dw2023_conformed_001_silver` | conformed-001 | silver | 18 | 18 | 0 | 0 | Databricks workflow with reusable notebook task | pilot_candidate | Wave 1 - metadata fan-out pilot |
| `dw2023_daily_silver` | daily | silver | 457 | 457 | 0 | 0 | metadata-driven driver with bounded fan-out | pilot_candidate | Wave 1 - metadata fan-out pilot |
| `dw2023_monthly_gold` | monthly | gold | 1 | 1 | 0 | 0 | Databricks workflow with reusable notebook task | pilot_candidate | Wave 1 - metadata fan-out pilot |

## Dependency shape

| Candidate | Internal dependencies | External dependencies | Root records | Missing target dependencies |
|---|---:|---:|---:|---:|
| `dw2023_daily_gold` | 478 | 4 | 312 | 0 |
| `dw2023_conformed_001_silver` | 0 | 0 | 0 | 0 |
| `dw2023_daily_silver` | 0 | 0 | 0 | 0 |
| `dw2023_monthly_gold` | 0 | 0 | 0 | 0 |

## Migration blockers

| Candidate | Missing notebook paths |
|---|---|
| `dw2023_daily_gold` | `300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_person`<br>`300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_project_bridgit`<br>`300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_role`<br>`300_silver_to_gold/bridgit_reporting/silver_to_gold_fact_allocations`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_dim_activity_code`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_dim_task`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_dim_wbs`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task_baseline`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_baseline_current`<br>`300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_current`<br>`300_silver_to_gold/operation_financials/silver_to_gold_fact_project_labor_cost`<br>`300_silver_to_gold/origami/silver_to_gold_origami_equipment`<br>`300_silver_to_gold/origami/silver_to_gold_origami_locations`<br>`300_silver_to_gold/textura/silver_to_gold_bridge_project_user_role`<br>`300_silver_to_gold/textura/silver_to_gold_dim_contract`<br>`300_silver_to_gold/textura/silver_to_gold_dim_draw`<br>`300_silver_to_gold/textura/silver_to_gold_dim_project`<br>`300_silver_to_gold/textura/silver_to_gold_dim_subcontractor`<br>`300_silver_to_gold/textura/silver_to_gold_dim_supplier_tracking`<br>`300_silver_to_gold/textura/silver_to_gold_dim_user`<br>`300_silver_to_gold/textura/silver_to_gold_fact_budgetline`<br>`300_silver_to_gold/textura/silver_to_gold_fact_change_order`<br>`300_silver_to_gold/textura/silver_to_gold_fact_invoice`<br>`300_silver_to_gold/textura/silver_to_gold_fact_invoice_approval`<br>`300_silver_to_gold/textura/silver_to_gold_fact_invoiceline`<br>`300_silver_to_gold/textura/silver_to_gold_fact_lien_waiver`<br>`300_silver_to_gold/textura/silver_to_gold_fact_payment`<br>`300_silver_to_gold/textura/silver_to_gold_fact_payment_hold`<br>`300_silver_to_gold/textura/silver_to_gold_fact_supplier_tracking` |

## Design use

- Use these candidates to decide whether each process layer becomes a generated Databricks workflow, a driver-notebook fan-out, or a smaller set of domain workflows.
- Resolve missing notebook artifacts before creating production job definitions.
- Validate Databricks workflow task limits, concurrency, retry behavior, notifications, and run-as identity before deployment.
- Keep ADF trigger-flow waves and metadata workflow candidates linked during planning; they answer different migration questions.

The machine-readable candidate file is `architecture-lens/metadata/databricks-workflow-candidates.json`.
