# Orchestration

**Status:** Initial discovery

The repository contains Databricks job JSON definitions and a Databricks Asset Bundle configuration for development, test, and production. Some notebooks also interact directly with the Databricks Jobs API. Azure Data Factory appears in naming and deployment metadata, but its complete pipeline definitions are not present in the inspected repository.

## Documentation objectives

For every production workflow, record:

- Trigger and schedule
- Upstream prerequisites
- Job and task graph
- Parameters and defaults
- Compute policy and execution identity
- Concurrency, timeout, and retry settings
- Success and failure outputs
- Operational logging
- Recovery and replay procedure
- Environment promotion path

## Initial job pattern

The bronze-to-silver job invokes a shared processing notebook and supplies object name, schema, key columns, incremental/full-load flags, PII columns, snapshot behavior, project identifier, partitioning, and processing timestamps. This parameter set is a valuable source for automated documentation and standards checks.

