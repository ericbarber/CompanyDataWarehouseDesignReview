# Data-Layer Standard

## Durable landing and raw

- Preserve the source representation and ingestion evidence.
- Record origin, extraction time, receipt time, and immutable correlation identifiers.
- Restrict direct consumer access.
- Define replay, quarantine, retention, and deletion behavior.

## Bronze

- Remain source aligned and traceable to a raw object or managed connector.
- Use Delta tables and retain ingestion metadata.
- Avoid business reinterpretation.
- Declare schema-drift behavior and invalid-record handling.

## Silver and ODS

- Standardize types, identifiers, dates, codes, and reference values.
- Declare keys and deduplication behavior.
- Apply classification, masking, and row filters consistently.
- Represent current operational state in ODS models when required.
- Publish measurable quality and freshness requirements.

## Gold and BI warehouse

- Declare the grain of every fact and dimension.
- Use conformed dimensions for shared business concepts.
- Give calculated measures unambiguous business definitions.
- Identify semantic models and reports that consume each product.
- Version breaking changes and provide migration windows.

## AI-ready lakehouse products

- Document approved purpose, training suitability, lineage, bias considerations, and retention.
- Prevent restricted data from entering models or prompts without an approved use case and boundary.
- Record feature definitions and point-in-time correctness requirements.

## API layer

- Expose versioned contracts rather than physical warehouse structure.
- Authenticate service identities and authorize at the least-privilege level.
- Apply classification-aware filtering and response logging.
- Define rate, latency, availability, and deprecation expectations.

