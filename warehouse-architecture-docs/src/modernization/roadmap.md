# Migration Roadmap

## Phase 0 — Architecture reconstruction

- Generate notebook, function, job, and data-asset inventories.
- Validate one representative end-to-end domain.
- Establish drawing and documentation conventions.
- Identify security boundaries and unknowns.

## Phase 1 — Platform foundations

- Confirm Unity Catalog topology and environment isolation.
- Establish data contracts, quality policies, and deployment standards.
- Standardize identity, secrets, logging, and observability.
- Create durable ingestion and quarantine patterns.

## Phase 2 — Ingestion modernization

- Classify sources as event, CDC, micro-batch, or scheduled batch.
- Implement checkpointed and replayable ingestion patterns.
- Migrate selected high-value flows and measure behavior.

## Phase 3 — ODS and warehouse modernization

- Introduce ODS models for integrated operational state.
- Establish conformed dimensions and declared fact grain.
- Version semantic contracts and migrate BI consumers.

## Phase 4 — Data and AI products

- Publish supported, discoverable products.
- Introduce feature and model-input governance.
- Add quality, freshness, use restrictions, and lifecycle evidence.

## Phase 5 — Governed API layer

- Define resource and event contracts.
- Enforce classification-aware authorization.
- Decouple applications and agents from physical storage models.
- Establish versioning, throttling, monitoring, and deprecation.

