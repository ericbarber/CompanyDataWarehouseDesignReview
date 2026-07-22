# Architecture Lens

Architecture Lens is the planned tool layer for the DW2023 architecture review. Its first increment is a generated metadata inventory that turns repository evidence into stable records for notebooks, functions, Databricks jobs, ADF orchestration, and relationships.

## Current increment

Run the inventory generator from the repository root:

```bash
python3.11 tools/generate_inventory.py
```

The generator reads `DW2023-Databricks.zip` and the local `DW2023-DataFactory/` repository evidence, then writes:

- `architecture-lens/metadata/inventory.json`
- `architecture-lens/metadata/flow-graph.json`
- `architecture-lens/metadata/metadata-dependencies.json`
- `warehouse-architecture-docs/src/appendices/repository-inventory.md`
- `warehouse-architecture-docs/src/processing/notebook-catalog.md`
- `warehouse-architecture-docs/src/processing/function-catalog.md`
- `warehouse-architecture-docs/src/processing/job-catalog.md`
- `warehouse-architecture-docs/src/processing/adf-orchestration-catalog.md`
- `warehouse-architecture-docs/src/processing/current-flow-graph.md`
- `warehouse-architecture-docs/src/data/metadata-dependency-catalog.md`
- `warehouse-architecture-docs/src/modernization/adf-to-databricks-orchestration.md`
- `warehouse-architecture-docs/src/modernization/dynamic-metadata-resolution.md`
- `warehouse-architecture-docs/src/modernization/adf-migration-waves.md`

The generated records are evidence, not approved production truth. They must be reconciled with deployed Databricks, Unity Catalog, Azure Data Factory, Azure infrastructure, and Power BI metadata.
