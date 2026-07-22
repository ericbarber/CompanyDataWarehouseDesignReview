# Modernization Principles

1. Modernize by business flow, not by moving isolated notebooks.
2. Preserve lineage and replayability during every transition.
3. Select streaming when latency and event semantics justify it.
4. Make every write idempotent or explicitly non-repeatable.
5. Treat schema as a versioned contract.
6. Separate operational integration, analytical models, and delivery APIs.
7. Prefer platform-native governance, observability, and deployment mechanisms.
8. Keep CUI inside an explicitly designed and evidenced boundary.
9. Introduce quality objectives before changing processing mode.
10. Retire duplicate implementations after consumers migrate.

## Disposition vocabulary

- **Retain:** The component meets the target standard.
- **Refactor:** Its capability remains necessary but implementation must change.
- **Replace:** A different platform capability will assume responsibility.
- **Retire:** The component is obsolete, duplicated, or unsupported.

