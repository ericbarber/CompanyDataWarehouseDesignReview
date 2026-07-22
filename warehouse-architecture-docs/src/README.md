# DW2023 Warehouse Architecture

This book is the design and architecture record for the DW2023 Databricks data warehouse. Its purpose is to make the warehouse understandable at enterprise, system, pipeline, dataset, notebook, and function levels.

The documentation supports two related goals:

1. Reconstruct and validate the current architecture from source code, deployed metadata, and architecture-team knowledge.
2. Design a controlled migration toward streaming and micro-batch ingestion, an operational data store, BI star schemas, data science and AI-ready lakehouse products, and a governed API layer.

## Architectural direction

```text
Batch | Micro-batch | CDC | Events
                 |
                 v
        Ingestion and Landing
                 |
                 v
      Operational Data Store (ODS)
                 |
       +---------+----------+
       |                    |
       v                    v
 BI Warehouse         AI-ready Lakehouse
 Star Schemas         Data/ML Products
       |                    |
       +---------+----------+
                 |
                 v
         Governed API Layer
                 |
                 v
 Applications | Analytics | AI Agents | Partners
```

## Documentation status vocabulary

Every documented claim uses one of these states:

- **Observed** — verified directly in source code or deployed metadata.
- **Validated** — confirmed by a responsible subject-matter expert.
- **Proposed** — part of the target design but not approved.
- **Approved** — accepted through an architecture decision.
- **Unknown** — discovery is incomplete and requires an owner.

This distinction prevents inferred behavior from being presented as production fact.

