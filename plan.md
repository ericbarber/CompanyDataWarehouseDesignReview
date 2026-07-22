# DW2023 Warehouse Architecture Documentation and Modernization Plan

## 1. Purpose

This plan establishes the work required to reconstruct, validate, and publish the architecture of the existing DW2023 Databricks warehouse and to design its controlled modernization.

The immediate goal is to produce understandable, evidence-based documentation of:

- Every system, interface, job, notebook, function, and data asset in scope
- The movement and transformation of data from source to consumer
- Runtime, deployment, operational, and security dependencies
- Existing architectural risks, constraints, and undocumented behavior
- The transition toward streaming and micro-batch ingestion, an Operational Data Store (ODS), BI star schemas, governed data and AI products, and an API layer
- The system and data boundaries needed to support CMMC-aligned architecture evidence

The mdBook site is the version-controlled publication. Editable draw.io files are the diagram sources. The planned Architecture Lens web application will automate discovery, navigation, review, and impact analysis.

## 2. Outcomes

The program will deliver:

1. A validated current-state architecture baseline
2. An inventory of warehouse components and their relationships
3. End-to-end data-flow and data-transformation documentation
4. Function-level technical definitions
5. Domain architecture packages
6. Security, trust-boundary, and CUI-scope views
7. An approved target architecture and transition roadmap
8. A repeatable architecture-review standard
9. An Architecture Lens web-tool product backlog and implementation design

## 3. Guiding principles

- Distinguish observed facts from assumptions, proposals, and approved decisions.
- Generate inventories from code and platform metadata before requesting manual entry.
- Validate automated discoveries with business and technical owners.
- Document data movements as first-class architectural objects.
- Modernize complete business flows rather than isolated notebooks.
- Select streaming only when latency and event semantics justify it.
- Preserve replayability, lineage, auditability, and rollback throughout migration.
- Use explicit data contracts and controlled schema evolution.
- Keep CUI inside a deliberately defined, approved, and evidenced boundary.
- Treat documentation as a maintained product, not a one-time report.

## 4. Scope

### 4.1 Current-state discovery

- DW2023 Databricks notebooks and shared functions
- Databricks job definitions and task dependencies
- Databricks Asset Bundle configuration
- Azure Data Factory orchestration and triggers
- Raw, bronze, silver, and gold data assets
- Delta processing, schema evolution, and Change Data Feed behavior
- Unity Catalog catalogs, schemas, permissions, tags, and lineage
- Storage accounts, containers, external locations, and retention behavior
- Development, test, and production environments
- Power BI and other downstream consumers
- Operational metrics, audit records, alerts, and support procedures
- Human identities, service identities, secrets, and access-control paths

### 4.2 Target-state design

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
 BI Warehouse       AI-ready Lakehouse
 Star Schemas       Data/ML Products
       |                    |
       +---------+----------+
                 |
                 v
         Governed API Layer
                 |
                 v
 Applications | Analytics | AI Agents | Partners
```

### 4.3 Initial repository baseline

The initial scan identified:

- 581 Python notebook files
- Approximately 202 explicit Python function declarations
- 21 Databricks job JSON definitions
- Four primary processing stages: source-to-raw, raw-to-bronze, bronze-to-silver, and silver-to-gold
- Development, test, and production Databricks workspace targets

These counts are discovery inputs. They do not identify deployed, active, duplicated, or obsolete components.

## 5. Workstreams

### Workstream A — Architecture documentation standard

Define and maintain:

- Stable identifiers for systems, assets, movements, jobs, notebooks, functions, decisions, and findings
- Status vocabulary: Observed, Validated, Proposed, Approved, and Unknown
- Naming, ownership, evidence, and review requirements
- draw.io symbols, colors, boundaries, arrows, and labeling conventions
- Templates for systems, interfaces, domains, data assets, movements, functions, and decisions
- Documentation review and expiration policy

### Workstream B — Automated repository discovery

Build repeatable extraction for:

- Notebook paths, widgets, and imports
- Python functions, signatures, and call relationships
- Spark reads, writes, SQL statements, table references, and file paths
- API, JDBC, ODBC, and secret access
- Job tasks, parameters, schedules, dependencies, retries, and identities
- Permission, ownership, row-filter, and PII-view operations
- Duplicate and superseded implementations

Discovery output must include evidence locations and confidence levels.

### Workstream C — Runtime and platform discovery

Reconcile repository intent with deployed behavior using:

- Unity Catalog information schema
- Table and column lineage
- Databricks Jobs and Workspace APIs
- Audit and operational system tables
- Delta table history and properties
- Azure Data Factory metadata
- Power BI lineage and consumer metadata
- Azure infrastructure and network configuration

### Workstream D — Domain architecture

For each approved business or source-system domain:

- Identify owners and authoritative systems
- Trace all source-to-consumer movements
- Define transformation intent and business rules
- Document facts, dimensions, grain, keys, and semantics
- Identify reports, applications, extracts, and APIs
- Record security classifications and quality expectations
- Assess every component as Retain, Refactor, Replace, or Retire

### Workstream E — Security and CMMC-aligned evidence

Document:

- Systems that process, store, transmit, or protect FCI or CUI
- Authorization and trust boundaries
- Human and service identities
- Administrative, data, logging, backup, and recovery paths
- Encryption and key-management boundaries
- External connections and data transfers
- Audit generation, retention, monitoring, and review
- Control-to-component and evidence-owner mappings

The architecture documentation supports assessment readiness; it does not itself certify CMMC compliance.

### Workstream F — Target and transition architecture

Design:

- Ingestion patterns for events, CDC, micro-batch, APIs, files, and scheduled batch
- Durable landing, replay, quarantine, and schema-contract behavior
- ODS integration and current-state models
- BI warehouse facts, dimensions, semantic models, and conformed concepts
- Governed data science and AI-ready products
- Versioned API and event contracts
- Observability, quality objectives, and operational support
- Environment promotion and infrastructure-as-code patterns
- Intermediate transition states and dependency sequencing

### Workstream G — Architecture Lens web application

Define and implement capabilities for:

- Searchable component and data-asset inventory
- Interactive upstream and downstream lineage
- Function, notebook, job, and domain pages
- Architecture diagrams and draw.io source links
- Standards checks and documentation coverage
- Findings, decisions, exceptions, approvals, and review history
- Modernization disposition and dependency tracking
- Change impact analysis
- Controlled metadata reconciliation

## 6. Delivery phases

### Phase 0 — Mobilization and standards

**Target duration:** 1–2 weeks

#### Activities

- Confirm executive sponsor, architecture owner, technical leads, security representatives, and domain reviewers.
- Approve documentation states, stable identifiers, templates, and diagram conventions.
- Confirm accessible repositories, Databricks environments, Azure resources, ADF metadata, Unity Catalog, and Power BI metadata.
- Select one representative pilot domain and one complex pilot domain.
- Establish the decision, finding, and unknown-question registers.

#### Deliverables

- Approved documentation standard
- Stakeholder and responsibility matrix
- Discovery-access checklist
- Architecture view catalog
- Pilot selection and success criteria

#### Exit criteria

- Required stakeholders and evidence sources are identified.
- The architecture team approves the notation and validation process.
- Pilot scope has named owners and accessible evidence.

### Phase 1 — Automated inventory

**Target duration:** 2–4 weeks

#### Activities

- Extract repository components and code relationships.
- Import job and deployment configuration.
- Establish canonical component and relationship records.
- Reconcile the initial inventory with platform metadata.
- Flag unresolved dynamic SQL, runtime paths, and external dependencies.

#### Deliverables

- Notebook catalog
- Function catalog
- Job and task catalog
- Data-asset inventory
- Initial movement register
- Unknowns and evidence-quality report

#### Exit criteria

- Every discovered artifact has a stable identifier and source reference.
- Inventory generation is repeatable.
- Coverage and confidence are measurable.

### Phase 2 — Pilot current-state architecture

**Target duration:** 3–5 weeks

#### Activities

- Trace the pilot flow from authoritative source through every consumer.
- Document all shared functions used by the flow.
- Create logical, physical, orchestration, sequence, and security diagrams.
- Validate transformations, keys, incremental logic, errors, retries, and recovery.
- Record risks, decisions, and modernization disposition.

#### Deliverables

- A00 enterprise context diagram
- A01 logical data-flow diagram
- A02 physical deployment diagram
- A03 orchestration diagram
- A04 pilot domain diagram
- A05 security and trust-boundary diagram
- A06 shared processing-pattern diagrams
- Complete pilot domain architecture package

#### Exit criteria

- Business and technical owners validate the pilot flow.
- Every diagram arrow maps to a movement record.
- Every executing component maps to a definition and code location.
- Security reviewers validate the represented boundary and outstanding unknowns.

### Phase 3 — Portfolio current-state baseline

**Target duration:** 6–12 weeks, delivered incrementally by domain

#### Activities

- Apply the pilot method to remaining domains.
- Reconcile shared, duplicated, unused, and obsolete processing.
- Complete consumer and external-interface discovery.
- Publish coverage, ownership, and architecture-risk dashboards.

#### Deliverables

- Validated domain architecture packages
- Enterprise lineage and dependency views
- Shared-service and function definitions
- Current-state risk and technical-debt register
- Documentation coverage report

#### Exit criteria

- All production gold products have validated ownership and upstream lineage.
- Critical source-to-consumer paths are documented.
- CUI/FCI scope is explicitly classified or recorded as an unresolved finding.

### Phase 4 — Target and transition design

**Target duration:** 4–8 weeks

#### Activities

- Define workload-selection criteria for streaming, CDC, micro-batch, and batch.
- Define ODS, dimensional warehouse, lakehouse-product, and API standards.
- Design platform, identity, network, observability, quality, and deployment foundations.
- Produce transition architectures and migration waves.
- Estimate dependencies, effort, risk, and operational impact.

#### Deliverables

- Approved A07 target architecture
- A08 transition architecture set
- Data contract and interface standards
- Modernization assessment register
- Prioritized migration roadmap
- Architecture Decision Records

#### Exit criteria

- Architecture, security, operations, and product owners approve the target state.
- Every migration wave has prerequisites, rollback strategy, and acceptance criteria.
- The target design identifies how CUI remains within an assessed boundary.

### Phase 5 — Architecture Lens MVP

**Target duration:** 6–10 weeks

#### Activities

- Implement metadata ingestion and reconciliation.
- Build inventory, detail, lineage, search, and review views.
- Link published documentation and draw.io sources.
- Add coverage, findings, decisions, and modernization tracking.
- Pilot authentication, authorization, audit, backup, and deployment.

#### Deliverables

- Deployable Architecture Lens MVP
- Metadata model and ingestion jobs
- Architecture review workflow
- Operating guide and support model
- MVP security and acceptance-test evidence

#### Exit criteria

- Users can answer source, destination, owner, producer, consumer, security, and impact questions for pilot domains.
- Automated refresh detects material repository and platform drift.
- Access and audit behavior pass security review.

### Phase 6 — Modernization delivery

**Target duration:** Multi-release program

#### Activities

- Implement platform foundations.
- Migrate domain flows in dependency-aware waves.
- Parallel-run and reconcile old and new products.
- Migrate consumers and retire obsolete implementations.
- Update architecture evidence with each production release.

#### Exit criteria per migration wave

- Data contracts and quality objectives pass.
- Reconciliation demonstrates accepted completeness and correctness.
- Performance, latency, recovery, and security tests pass.
- Consumers approve migration.
- Rollback remains available until stabilization criteria are met.
- Retired paths are removed from schedules, permissions, monitoring, and support procedures.

## 7. Architecture deliverables

| ID | View | Purpose |
|---|---|---|
| A00 | Enterprise context | Systems, actors, external dependencies, and ownership |
| A01 | Logical data flow | Layer-to-layer data movement from source to consumers |
| A02 | Physical deployment | Workspaces, storage, compute, catalogs, and network topology |
| A03 | Orchestration | Triggers, jobs, tasks, parameters, dependencies, and failures |
| A04 | Domain flows | Asset-specific end-to-end implementation by domain |
| A05 | Security architecture | Identity, access, CUI, audit, and trust boundaries |
| A06 | Processing patterns | Incremental load, deduplication, merge, schema, security, and metrics |
| A07 | Target architecture | Approved future platform and delivery model |
| A08 | Transition architecture | Intermediate migration states and release dependencies |

Editable diagrams reside under `warehouse-architecture-docs/diagrams/drawio/`. Reviewed SVG exports reside under `warehouse-architecture-docs/src/assets/diagrams/`.

## 8. Roles and responsibilities

| Role | Primary responsibility |
|---|---|
| Executive sponsor | Program priority, funding, and cross-team escalation |
| Architecture owner | Standards, decisions, target architecture, and approval |
| Data engineering lead | Runtime behavior, processing patterns, and migration feasibility |
| Domain owner | Business meaning, authoritative sources, and product acceptance |
| Data steward | Definitions, classification, quality, and permitted use |
| Security/CMMC lead | Boundary, control, assessment, and evidence validation |
| Platform/Cloud lead | Azure, Databricks, identity, network, and deployment architecture |
| BI lead | Semantic models, reports, consumers, and migration validation |
| Application/API lead | Interface contracts and operational consumers |
| Documentation product owner | mdBook quality, review workflow, and publication cadence |

Named individuals and accountable approvers must be added during Phase 0.

## 9. Initial backlog

### Priority 0 — Establish control of the documentation

- [ ] Approve stable identifier allocation.
- [ ] Approve diagram notation and review states.
- [ ] Name architecture, domain, security, and platform reviewers.
- [ ] Create decision, finding, unknown, and evidence registers.
- [ ] Add documentation build validation to continuous integration.

### Priority 1 — Complete discovery foundations

- [ ] Generate the full notebook inventory.
- [ ] Generate the full function inventory and initial call graph.
- [ ] Parse all Databricks job definitions and task dependencies.
- [ ] Extract table, view, file, API, JDBC, ODBC, and secret references.
- [ ] Identify source and destination assets for every resolvable operation.
- [ ] Reconcile repository artifacts with deployed Databricks resources.
- [ ] Inventory ADF orchestration and Power BI consumers.

### Priority 2 — Document a pilot flow

- [ ] Select a common representative domain.
- [ ] Select a high-complexity or high-risk domain.
- [ ] Trace both flows from source through consumers.
- [ ] Define all shared functions used by the flows.
- [ ] Produce A00–A06 draw.io diagrams.
- [ ] Conduct architecture, domain, operations, and security validation workshops.

### Priority 3 — Define the target architecture

- [ ] Define ingestion-pattern selection criteria.
- [ ] Define ODS modeling and synchronization standards.
- [ ] Define BI dimensional-model and semantic-contract standards.
- [ ] Define data science and AI product requirements.
- [ ] Define API and event contract standards.
- [ ] Define CUI boundary and evidence requirements.
- [ ] Approve target and transition diagrams.

### Priority 4 — Build Architecture Lens

- [ ] Approve the canonical metadata model.
- [ ] Define MVP user journeys and authorization roles.
- [ ] Implement repository and Databricks ingestion.
- [ ] Implement inventory, search, detail, and lineage views.
- [ ] Implement review, decision, finding, and disposition workflows.
- [ ] Implement documentation drift and coverage reporting.

## 10. Measures of success

### Documentation coverage

- 100% of production jobs and notebooks have an inventory record.
- 95% of production data products have validated owner, purpose, grain, keys, classification, and refresh expectations.
- 90% of production assets have validated upstream and downstream lineage.
- 100% of critical functions have input, output, side-effect, failure, security, and modernization definitions.

### Architecture usability

- A reviewer can identify the producer and consumers of a data product within five minutes.
- Impact analysis identifies affected jobs, assets, interfaces, and consumers before a change is approved.
- Every diagram arrow resolves to a documented movement.
- Every movement resolves to executing components and evidence.

### Security readiness

- 100% of known CUI/FCI flows have a validated boundary classification.
- All in-scope service identities, external connections, audit paths, and protection assets are documented.
- Architecture evidence has an owner, validation date, and review cadence.

### Modernization readiness

- Every production flow has a Retain, Refactor, Replace, or Retire disposition.
- Each migration wave has measurable quality, latency, recovery, security, and rollback criteria.
- New architectural components cannot enter production without updated documentation and review evidence.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Repository and production have drifted | Reconcile code with deployed metadata and runtime evidence |
| Dynamic SQL prevents complete static lineage | Combine static parsing, runtime lineage, and owner validation |
| Domain ownership is unclear | Make unresolved ownership a tracked architecture finding |
| Documentation becomes stale | Automate refresh, assign review dates, and gate material changes |
| Every workload is assumed to require streaming | Use latency, volume, ordering, replay, and cost selection criteria |
| CUI scope expands unintentionally | Diagram trust boundaries and approve every external transfer |
| Migration breaks downstream consumers | Maintain consumer inventory, contract versions, parallel runs, and rollback |
| Tool development outruns architecture quality | Validate the pilot information model before scaling the application |

## 12. Immediate next actions

1. Appoint the architecture owner and pilot-domain reviewers.
2. Select the representative and complex pilot flows.
3. Approve documentation and draw.io conventions.
4. Build the automated notebook, function, job, and movement inventory.
5. Schedule the first current-state validation workshop.
6. Produce the initial A00 enterprise context and A01 logical data-flow diagrams.
7. Record the first architecture decisions, findings, unknowns, and evidence sources.

## 13. Definition of done

The architecture baseline is complete when a reviewer can begin with any supported data product and reliably navigate backward to its authoritative sources and forward to its consumers, while understanding:

- What moved
- Why it moved
- How and when it moved
- Which code and infrastructure performed the movement
- Which transformations were applied
- Which identity and security boundary governed it
- How it is monitored and recovered
- Who owns and supports it
- What must change in the target architecture

The modernization program is complete only after approved target products replace their legacy paths, consumers migrate successfully, obsolete processing is retired, and the architecture documentation reflects the resulting production state.
