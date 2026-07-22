# CompanyDataWarehouseDesignReview

This repository contains the DW2023 warehouse architecture documentation and the first Architecture Lens metadata tooling.

## Development

This repo pins Python in `.tool-versions` for the generated inventory tooling.

Generate repository evidence and rebuild the mdBook site:

```bash
make validate
```

The inventory generator reads `DW2023-Databricks.zip` and `DW2023-DataFactory/`, updates generated catalog pages under `warehouse-architecture-docs/src/`, and writes machine-readable metadata to `architecture-lens/metadata/inventory.json`, `architecture-lens/metadata/flow-graph.json`, and `architecture-lens/metadata/metadata-dependencies.json`.
