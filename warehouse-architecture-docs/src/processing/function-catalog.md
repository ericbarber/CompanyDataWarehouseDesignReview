# Function Catalog

The initial repository scan found approximately **202 explicitly declared Python functions**. Dynamic functions, SQL definitions, and imported package behavior require separate discovery.

## Initial shared-function groups

| Group | Examples | Architectural role |
|---|---|---|
| Runtime context | `workspace_to_environment`, `getCurrentUser`, `getNotebookName` | Resolve execution identity and environment |
| Filesystem | `doesPathExist`, `doesDirectoryContainDeltaFiles` | Discover and validate source content |
| Data normalization | `trim_string_columns`, `flatten_dataframe_array_columns` | Standardize input structures |
| Keys and schema | `generate_hash_key`, `compare_and_update_schema` | Establish identity and schema compatibility |
| Delta processing | `bronze_to_silver_drop_duplicates`, `upsert_delta_serverless` | Incremental processing and persistence |
| Catalog security | `set_ownership`, `grant_principal_select_access` | Apply ownership and permissions |
| Data security | `assign_rls_by_project_number`, `createPiiView` | Apply row and column exposure controls |
| Observability | `get_table_last_operation_metrics`, `update_operation_metrics_log` | Capture processing results |

This table is an index, not a substitute for the detailed function definition required by the template.

