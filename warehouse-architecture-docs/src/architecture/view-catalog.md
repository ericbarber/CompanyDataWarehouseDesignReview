# Architecture View Catalog

The architecture is documented through multiple coordinated views rather than one oversized diagram.

| View | Purpose | Initial scope |
|---|---|---|
| A00 Enterprise context | Systems, actors, and external dependencies | DW2023 and surrounding enterprise services |
| A01 Logical data flow | Layer-to-layer movement | Source through consumers |
| A02 Physical deployment | Workspaces, storage, compute, and network | Dev, test, and production |
| A03 Orchestration | Scheduling, tasks, parameters, and failures | ADF and Databricks Jobs |
| A04 Domain flow | End-to-end implementation for one domain | One page per source/business domain |
| A05 Security | Identities, controls, and trust boundaries | CUI and non-CUI paths |
| A06 Processing patterns | Shared algorithms and functions | Incremental load, merge, security, metrics |
| A07 Target architecture | Approved modernization destination | Streaming, ODS, products, API layer |
| A08 Transition architecture | Intermediate migration states | Releases and dependency order |

Editable `.drawio` sources are stored in `diagrams/drawio/`. Reviewed SVG exports are stored in `src/assets/diagrams/` and embedded in the applicable page.

