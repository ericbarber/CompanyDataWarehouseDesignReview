# Target-State Overview

**Status:** Proposed

The target state separates ingestion, operational integration, analytical modeling, reusable data products, and governed delivery while maintaining end-to-end lineage and policy enforcement.

## Target flow

```text
Sources
  |-- Events and streams
  |-- Database CDC
  |-- Micro-batch APIs and files
  `-- Scheduled batch
             |
             v
  Controlled ingestion and durable landing
             |
             v
  Operational Data Store
             |
       +-----+----------------+
       |                      |
       v                      v
  BI Warehouse          AI-ready Lakehouse
  Facts/dimensions      Governed data products
  Semantic models      Features and model inputs
       |                      |
       +----------+-----------+
                  |
                  v
          Governed API Layer
                  |
        +---------+---------+
        |         |         |
        v         v         v
    Internal   Partners   AI/Automation
      Apps
```

## Target capabilities

- Event-time and processing-time semantics for streaming workloads
- Checkpointed, restartable, and idempotent ingestion
- Explicit data contracts and controlled schema evolution
- ODS models for current operational state and integration
- Dimensional BI models with declared grain and conformed dimensions
- Independently owned, versioned data products
- Data quality enforcement with measurable service objectives
- Unity Catalog governance and lineage
- Policy-driven data access and CUI isolation
- API contracts that prevent consumers from coupling directly to physical tables
- Infrastructure, jobs, policies, and permissions deployed as code

