# CompanyDataWarehouseDesignReview

This repository contains the DW2023 warehouse architecture documentation and the first Architecture Lens metadata tooling.

## Development

This repo pins Python in `.tool-versions` for the generated inventory tooling.

Generate repository evidence and rebuild the mdBook site:

```bash
make validate
```

The inventory generator reads `DW2023-Databricks.zip`, `DW2023-DataFactory/`, and CSV exports under `metadata/`, updates generated catalog and migration planning pages under `warehouse-architecture-docs/src/`, and writes machine-readable metadata and workflow specs under `architecture-lens/`.

Run the strict Databricks workflow candidate gate before copying a generated resource into a bundle:

```bash
make workflow-preflight
```

This gate intentionally fails while generated dev bundle candidates still contain `TODO_` placeholders.
Create `architecture-lens/config/workflow-overrides.json` from the tracked example file to provide local dev compute, owner, notification, schedule, and retry settings without committing environment-specific values.
