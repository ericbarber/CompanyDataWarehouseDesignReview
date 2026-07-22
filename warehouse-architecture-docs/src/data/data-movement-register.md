# Data Movement Register

This register will be populated by repository discovery, Databricks metadata, and architecture-team validation.

| ID | Source | Destination | Mode | Executor | Status |
|---|---|---|---|---|---|
| MOV-00001 | External source object | Raw landing | Unknown | Source-to-raw notebook | Discovery |
| MOV-00002 | Raw landing | Bronze Delta table | Batch | Raw-to-bronze notebook | Discovery |
| MOV-00003 | Bronze Delta table | Silver Delta table | Incremental/batch | `bronze_to_silver` | Observed |
| MOV-00004 | Silver tables | Gold fact/dimension | Batch | Domain gold notebook | Discovery |
| MOV-00005 | Gold product | Power BI/application | Query/extract | Consumer connection | Unknown |

These starter records describe patterns, not individual production movements. They will be replaced by asset-specific records during discovery.

