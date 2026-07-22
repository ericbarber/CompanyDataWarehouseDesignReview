# ADF to Databricks Orchestration Migration

Generated from current-state ADF evidence on 2026-07-22.

ADF is the current-state orchestration reference. It should be used to reconstruct the full flow graph, trigger cadence, parameters, dependency conditions, error handling, and platform touchpoints. It is not the target orchestration platform for modernization.

## Current-state migration inventory

| Signal | Count | Migration meaning |
|---|---:|---|
| ADF schedule triggers | 35 | Candidate Databricks schedules or external event triggers |
| ADF pipelines | 118 | Candidate Databricks job definitions, job tasks, or reusable task groups |
| Pipelines invoking Databricks notebooks | 45 | Direct candidates for Databricks job task migration |
| ExecutePipeline activities | 558 | Current dependency graph that must become job-task dependencies or job chaining |
| Copy activities | 73 | Connector movement requiring replacement with Databricks ingestion, Auto Loader, volumes, or source-specific loaders |

## Migration principles

- Preserve current business flow semantics before optimizing implementation.
- Convert ADF triggers into explicit Databricks schedules, event triggers, or upstream dependency contracts.
- Convert `ExecutePipeline` chains into Databricks job task dependencies where the execution boundary is still useful.
- Collapse orchestration-only wrapper pipelines when they add no retry, branching, logging, or ownership behavior.
- Replace ADF copy activities with Databricks-native ingestion patterns only after source connectivity, identity, replay, and observability are designed.
- Keep metadata-driven batch behavior, but move metadata reads, fan-out, logging, and status updates into a governed Databricks orchestration pattern.
- Treat self-hosted integration runtime and private endpoint dependencies as migration blockers until replacement network paths are validated.

## Target mapping

| Current ADF construct | Databricks target construct | Validation required |
|---|---|---|
| Schedule trigger | Databricks job schedule or event trigger | Time zone, disabled/enabled state, calendar rules, missed-run behavior |
| Pipeline | Databricks job or reusable workflow pattern | Owner, parameters, retry policy, notifications, permissions |
| ExecutePipeline | Job task dependency or explicit downstream job trigger | Dependency conditions, wait behavior, failure propagation |
| DatabricksNotebook activity | Databricks notebook task | Notebook path, parameters, cluster/serverless target, run identity |
| Lookup / ForEach metadata fan-out | Databricks task values, dynamic jobs, or metadata-driven driver notebook | Concurrency, ordering, partial retry, audit events |
| Copy activity | Databricks ingestion task | Connector parity, credentials, checkpointing, schema drift, replay |
| Stored procedure logging | Databricks system tables, Delta operational log, or retained metadata DB logging | Run correlation, alert routing, audit retention |
| Linked service / dataset | Unity Catalog external location, secret scope, connection, or source contract | Authentication, network path, secret ownership, classification |

## Phased approach

1. Generate and validate the ADF flow graph from trigger to terminal pipeline activity.
2. Select one low-risk scheduled flow and one complex metadata-driven flow as migration pilots.
3. Create Databricks job definitions that reproduce the ADF trigger, parameters, task dependencies, retries, and notifications.
4. Run ADF and Databricks orchestration in parallel against controlled data windows.
5. Reconcile row counts, data quality checks, runtime metrics, and consumer-visible outputs.
6. Cut over scheduling only after rollback, monitoring, support ownership, and security evidence are approved.
7. Retire ADF triggers, pipelines, linked services, datasets, and support procedures for migrated flows.

## Open decisions

- Confirm the target Databricks orchestration surface and naming standard for jobs, tasks, schedules, and reusable workflow components.
- Decide whether metadata-driven fan-out remains a driver-notebook pattern or becomes generated job/task configuration.
- Decide which ADF copy patterns should become Databricks ingestion code versus separate source-system integration services.
- Define the production cutover gate for each migrated flow.
