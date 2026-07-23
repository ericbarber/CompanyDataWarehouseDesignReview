# Architecture Lens

Architecture Lens is the planned tool layer for the DW2023 architecture review. Its first increment is a generated metadata inventory that turns repository evidence into stable records for notebooks, functions, Databricks jobs, ADF orchestration, and relationships.

## Current increment

Run the inventory generator from the repository root:

```bash
python3.11 tools/generate_inventory.py
```

Run generated workflow structural checks as part of normal validation:

```bash
make validate
```

Run the strict deploy-readiness preflight before moving a generated candidate into a Databricks bundle:

```bash
make workflow-preflight
```

The strict preflight fails while generated dev bundle candidates still contain `TODO_` placeholders.
Copy `architecture-lens/config/workflow-overrides.example.json` to `architecture-lens/config/workflow-overrides.json` and replace the local dev values to generate candidates that can pass strict preflight.

The generator reads `DW2023-Databricks.zip` and the local `DW2023-DataFactory/` repository evidence, then writes:

- `architecture-lens/metadata/inventory.json`
- `architecture-lens/metadata/flow-graph.json`
- `architecture-lens/metadata/metadata-dependencies.json`
- `architecture-lens/metadata/metadata-exports.json`
- `architecture-lens/metadata/databricks-workflow-candidates.json`
- `architecture-lens/config/workflow-overrides.example.json`
- `architecture-lens/workflow-specs/databricks-workflow-task-specs.json`
- `architecture-lens/workflow-specs/dw2023_daily_silver_pilot.job-resource.json`
- `architecture-lens/workflow-specs/dw2023_daily_silver_pilot.dev.bundle-resource.yml`
- `architecture-lens/workflow-specs/dw2023_daily_silver_smoke.job-resource.json`
- `architecture-lens/workflow-specs/dw2023_daily_silver_smoke.dev.bundle-resource.yml`
- `warehouse-architecture-docs/src/appendices/repository-inventory.md`
- `warehouse-architecture-docs/src/processing/notebook-catalog.md`
- `warehouse-architecture-docs/src/processing/function-catalog.md`
- `warehouse-architecture-docs/src/processing/job-catalog.md`
- `warehouse-architecture-docs/src/processing/adf-orchestration-catalog.md`
- `warehouse-architecture-docs/src/processing/current-flow-graph.md`
- `warehouse-architecture-docs/src/data/metadata-dependency-catalog.md`
- `warehouse-architecture-docs/src/data/resolved-metadata-catalog.md`
- `warehouse-architecture-docs/src/data/metadata-process-dependencies.md`
- `warehouse-architecture-docs/src/modernization/adf-to-databricks-orchestration.md`
- `warehouse-architecture-docs/src/modernization/dynamic-metadata-resolution.md`
- `warehouse-architecture-docs/src/modernization/adf-migration-waves.md`
- `warehouse-architecture-docs/src/modernization/databricks-workflow-candidates.md`
- `warehouse-architecture-docs/src/modernization/daily-silver-databricks-pilot.md`

The generated records are evidence, not approved production truth. They must be reconciled with deployed Databricks, Unity Catalog, Azure Data Factory, Azure infrastructure, and Power BI metadata.
