# System Context

**Status:** Initial discovery

DW2023 is a Databricks-centered data platform that ingests information from enterprise applications, APIs, relational databases, and file sources. It transforms source-aligned data through raw, bronze, silver, and gold stages and makes curated products available to Power BI and application integrations.

## Current known environments

The Databricks Asset Bundle configuration declares separate development, test, and production workspaces. Workspace URLs are configuration evidence; deployed network, identity, catalog, and storage boundaries remain to be validated.

## Context diagram

```text
                         +----------------------+
                         | Enterprise Identity  |
                         | and Secret Services  |
                         +----------+-----------+
                                    |
                                    v
+----------------+       +----------+-----------+       +----------------+
| Source Systems |------>| ADF / Databricks     |------>| Power BI       |
| DB, API, Files |       | Ingestion and Jobs   |       | Applications   |
+----------------+       +----------+-----------+       | Extracts       |
                                    |                   +----------------+
                                    v
                         +----------+-----------+
                         | Delta Data Platform  |
                         | Raw/Bronze/Silver/   |
                         | Gold                 |
                         +----------+-----------+
                                    |
                                    v
                         +----------+-----------+
                         | Audit, Metrics, and  |
                         | Operational Support  |
                         +----------------------+
```

## Discovery gaps

- Source-system inventory and system owners
- ADF pipeline definitions and triggers
- Storage accounts, containers, and retention rules
- Unity Catalog topology and catalog bindings
- Network and private connectivity
- Power BI workspaces, semantic models, and reports
- CUI categories and authoritative marking sources
- External interfaces and data-sharing agreements

