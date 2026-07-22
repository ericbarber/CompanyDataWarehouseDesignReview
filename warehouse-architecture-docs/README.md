# DW2023 Warehouse Architecture Documentation

This mdBook project is the architecture record for the DW2023 Databricks warehouse. It documents the existing implementation, data movement, shared functions, security boundaries, and the target modernization architecture.

## Local development

Install mdBook once:

```bash
cargo install mdbook --locked
```

Build the site:

```bash
cd warehouse-architecture-docs
mdbook build
```

Run a local server with automatic rebuilds:

```bash
mdbook serve --open
```

Generated HTML is written to `book/` and is intentionally excluded from version control.

## Authoring rules

- Update `src/SUMMARY.md` whenever a page is added or moved.
- Use repository-relative links for source code references.
- Store editable draw.io files under `diagrams/drawio/`.
- Export reviewed diagrams as SVG into `src/assets/diagrams/` for the book.
- Give every architectural component and data movement a stable identifier.
- Separate observed current-state facts from proposals and decisions.

