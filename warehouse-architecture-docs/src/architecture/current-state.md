# Current-State Overview

**Status:** Observed from repository structure; deployment validation pending

## Processing layers

| Stage | Repository location | Intended responsibility |
|---|---|---|
| Source to raw | `000_source_to_raw` | Acquire source data and create a durable landing representation |
| Raw to bronze | `100_raw_to_bronze` | Create source-aligned Delta data with ingestion metadata |
| Bronze to silver | `200_bronze_to_silver` | Clean, deduplicate, incrementally merge, and apply security behavior |
| Silver to gold | `300_silver_to_gold` | Produce business facts, dimensions, views, and data products |

## Observed shared behavior

The shared processing code includes capabilities for:

- Resolving environment and workspace context
- Discovering files and Delta content
- Normalizing paths and column names
- Cleaning strings and flattening arrays
- Generating hash keys
- Inspecting table history and configuration
- Detecting Change Data Feed and schema settings
- Deduplicating incremental bronze data
- Comparing and updating schemas
- Performing Delta upserts
- Assigning object ownership and access
- Creating semantic and row-secured views
- Logging operation metrics

These capabilities require function-by-function validation before they can be considered a complete description of runtime behavior.

## Architectural concerns to investigate

- Workspace paths and environment-specific assumptions
- Duplicate or superseded notebook implementations
- Dynamic SQL and runtime-derived lineage
- Automatic schema evolution without explicit contracts
- Direct API calls and ephemeral job creation
- Secrets and tokens obtained inside notebooks
- Access-control changes performed during data processing
- Metadata divided between code, job parameters, Unity Catalog, and an external SQL store

