# Function Catalog

Generated from `DW2023-Databricks.zip` on 2026-07-22.

This catalog lists explicit Python function declarations discovered by static parsing. Dynamic functions, SQL objects, imported package behavior, and runtime monkey-patching require separate discovery.

## Summary by group

| Group | Function count |
|---|---:|
| Data normalization | 19 |
| Delta processing | 10 |
| Domain or utility | 133 |
| Filesystem | 13 |
| Observability | 3 |
| Runtime context | 6 |
| Schema and keys | 28 |
| Security and access | 34 |

## Function index

| ID | Group | Function | Path | Line |
|---|---|---|---|---:|
| FUN-00001 | Domain or utility | `to_safe_string(v)` | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-reports.py:171` | 171 |
| FUN-00002 | Domain or utility | `get_api_response(url, headers)` | `notebooks/data_engineering/000_source_to_raw/source-to-raw-teambinder.py:166` | 166 |
| FUN-00003 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/000_source_to_raw/source-to-raw-teambinder.py:342` | 342 |
| FUN-00004 | Domain or utility | `get_token()` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetfencehistory.py:107` | 107 |
| FUN-00005 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetfencehistory.py:123` | 123 |
| FUN-00006 | Domain or utility | `get_token()` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetoperationfeed.py:111` | 111 |
| FUN-00007 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetoperationfeed.py:128` | 128 |
| FUN-00008 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetoperationhistory.py:122` | 122 |
| FUN-00009 | Domain or utility | `get_token()` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetsummary.py:106` | 106 |
| FUN-00010 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetsummary.py:123` | 123 |
| FUN-00011 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-faultshistory.py:119` | 119 |
| FUN-00012 | Domain or utility | `fetch_all_pages(api_url, headers)` | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-utilizationhistory.py:122` | 122 |
| FUN-00013 | Security and access | `get_access_token(tenant_id, client_id, client_secret)` | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_actualcost.py:84` | 84 |
| FUN-00014 | Domain or utility | `get_cost_data(subscription_id, access_token)` | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_actualcost.py:100` | 100 |
| FUN-00015 | Security and access | `get_access_token(tenant_id, client_id, client_secret)` | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_amortizedcost.py:84` | 84 |
| FUN-00016 | Domain or utility | `get_cost_data(subscription_id, access_token)` | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_amortizedcost.py:100` | 100 |
| FUN-00017 | Domain or utility | `filter_by_objects(config_list, key="object_name")` | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_silver_bridgit_reporting_master.py:71` | 71 |
| FUN-00018 | Domain or utility | `utc_now_str()` | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_silver_bridgit_reporting_master.py:86` | 86 |
| FUN-00019 | Delta processing | `run_bronze_phase(notebooks)` | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_silver_bridgit_reporting_master.py:89` | 89 |
| FUN-00020 | Delta processing | `run_silver_phase(objects, etl_timestamp)` | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_silver_bridgit_reporting_master.py:122` | 122 |
| FUN-00021 | Domain or utility | `makeexpr(column, dtype)` | `notebooks/data_engineering/100_raw_to_bronze/cslb_data/source_to_bronze_california_license_data.py:129` | 129 |
| FUN-00022 | Domain or utility | `makeexpr(column, dtype)` | `notebooks/data_engineering/100_raw_to_bronze/cslb_data/source_to_bronze_california_license_data_v2.py:133` | 133 |
| FUN-00023 | Domain or utility | `get_token()` | `notebooks/data_engineering/100_raw_to_bronze/nccer/raw_to_bronze_nccer_credentials.py:126` | 126 |
| FUN-00024 | Domain or utility | `get_json_with_refresh(url: str, headers: dict)` | `notebooks/data_engineering/100_raw_to_bronze/nccer/raw_to_bronze_nccer_credentials.py:136` | 136 |
| FUN-00025 | Data normalization | `normalize_to_rows(payload: Any)` | `notebooks/data_engineering/100_raw_to_bronze/nccer/raw_to_bronze_nccer_credentials.py:144` | 144 |
| FUN-00026 | Domain or utility | `exchange_auth_code(code)` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:52` | 52 |
| FUN-00027 | Security and access | `refresh_access_token(refresh_token)` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:68` | 68 |
| FUN-00028 | Domain or utility | `save_refresh_token(refresh_token)` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:83` | 83 |
| FUN-00029 | Domain or utility | `load_latest_refresh_token()` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:93` | 93 |
| FUN-00030 | Domain or utility | `get_procore_token()` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:108` | 108 |
| FUN-00031 | Domain or utility | `get_procore_headers()` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:141` | 141 |
| FUN-00032 | Domain or utility | `pull_procore_records(endpoint_name)` | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py:154` | 154 |
| FUN-00033 | Domain or utility | `strip_html(text)` | `notebooks/data_engineering/100_raw_to_bronze/procore/raw_to_bronze_procore_rfis.py:121` | 121 |
| FUN-00034 | Delta processing | `clean_for_delta(obj)` | `notebooks/data_engineering/100_raw_to_bronze/procore/raw_to_bronze_procore_rfis.py:139` | 139 |
| FUN-00035 | Domain or utility | `extract_timestamp(fileName)` | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_clue_all.py:151` | 151 |
| FUN-00036 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_clue_all.py:304` | 304 |
| FUN-00037 | Domain or utility | `extract_timestamp(fileName)` | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_files_all.py:151` | 151 |
| FUN-00038 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_files_all.py:304` | 304 |
| FUN-00039 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_zipcodes_all.py:320` | 320 |
| FUN-00040 | Domain or utility | `send_query(query)` | `notebooks/data_engineering/100_raw_to_bronze/sitesense/raw_to_bronze_sitesense.py:91` | 91 |
| FUN-00041 | Domain or utility | `pull_dataframe(table_name, column_list)` | `notebooks/data_engineering/100_raw_to_bronze/sitesense/raw_to_bronze_sitesense.py:99` | 99 |
| FUN-00042 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_budgetlines.py:89` | 89 |
| FUN-00043 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_budgetlines.py:251` | 251 |
| FUN-00044 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_changeorders.py:89` | 89 |
| FUN-00045 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_changeorders.py:237` | 237 |
| FUN-00046 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_contracts.py:89` | 89 |
| FUN-00047 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_contracts.py:258` | 258 |
| FUN-00048 | Domain or utility | `safe_int(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_contracts.py:264` | 264 |
| FUN-00049 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_draws.py:89` | 89 |
| FUN-00050 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_invoiceapprovals.py:89` | 89 |
| FUN-00051 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_invoices.py:89` | 89 |
| FUN-00052 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_invoices.py:254` | 254 |
| FUN-00053 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_linewaivers.py:93` | 93 |
| FUN-00054 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_linewaivers.py:255` | 255 |
| FUN-00055 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_manualcontracts.py:88` | 88 |
| FUN-00056 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_manualcontracts.py:241` | 241 |
| FUN-00057 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_organizationlevelholds.py:89` | 89 |
| FUN-00058 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_organizations.py:88` | 88 |
| FUN-00059 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_paymentholds.py:88` | 88 |
| FUN-00060 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_payments.py:89` | 89 |
| FUN-00061 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_payments.py:265` | 265 |
| FUN-00062 | Domain or utility | `safe_int(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_payments.py:271` | 271 |
| FUN-00063 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projects.py:89` | 89 |
| FUN-00064 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projects.py:304` | 304 |
| FUN-00065 | Domain or utility | `safe_int(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projects.py:310` | 310 |
| FUN-00066 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projectuserroles.py:88` | 88 |
| FUN-00067 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingcontractorvalues.py:89` | 89 |
| FUN-00068 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingprograms.py:88` | 88 |
| FUN-00069 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingprogramvalues.py:89` | 89 |
| FUN-00070 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingselectedvalues.py:89` | 89 |
| FUN-00071 | Domain or utility | `safe_float(v)` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingselectedvalues.py:235` | 235 |
| FUN-00072 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_tpaenrollments.py:89` | 89 |
| FUN-00073 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_tpaprograms.py:89` | 89 |
| FUN-00074 | Security and access | `get_access_token()` | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_users.py:89` | 89 |
| FUN-00075 | Data normalization | `flatten_financials_dynamic(all_results)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_financials.py:132` | 132 |
| FUN-00076 | Domain or utility | `get_val(d: dict, key: str)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_financials.py:141` | 141 |
| FUN-00077 | Data normalization | `flatten_list_to_string(list_data, fields, sep="\|", item_sep=", ")` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_financials.py:147` | 147 |
| FUN-00078 | Domain or utility | `_parse_date(s)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_financials.py:207` | 207 |
| FUN-00079 | Domain or utility | `as_list(v)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:369` | 369 |
| FUN-00080 | Domain or utility | `_coerce(rec: dict)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:376` | 376 |
| FUN-00081 | Domain or utility | `_extract_child(base_df, array_col: str, rename_map: dict)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:394` | 394 |
| FUN-00082 | Domain or utility | `_extract_certificates(base_df)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:406` | 406 |
| FUN-00083 | Domain or utility | `_collapse(df, label: str)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:426` | 426 |
| FUN-00084 | Domain or utility | `build_application_df(all_results: list)` | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py:438` | 438 |
| FUN-00085 | Domain or utility | `get_xml(url: str, timeout: int=60)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py:112` | 112 |
| FUN-00086 | Domain or utility | `to_list(x)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py:117` | 117 |
| FUN-00087 | Schema and keys | `lower_keys(d: Dict[str, Any])` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py:122` | 122 |
| FUN-00088 | Domain or utility | `fetch_rows_for_template(tid: int)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py:144` | 144 |
| FUN-00089 | Domain or utility | `to_safe_str(v)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py:194` | 194 |
| FUN-00090 | Schema and keys | `get_val_lowerkey(d, key_upper)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_templates.py:131` | 131 |
| FUN-00091 | Schema and keys | `get_val_lowerkey(d, key_upper)` | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_users.py:136` | 136 |
| FUN-00092 | Data normalization | `flatten_df(df_temp)` | `notebooks/data_engineering/100_raw_to_bronze/visionlinkcat/raw_to_bronze_visionlink.py:124` | 124 |
| FUN-00093 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/100_raw_to_bronze/vrm/raw_to_bronze_vrm_driver_compliance.py:290` | 290 |
| FUN-00094 | Domain or utility | `extract_pdf_to_df(pdf_path: str)` | `notebooks/data_engineering/100_raw_to_bronze/weld_office/raw_to_bronze_weld_office_process_expiry.py:124` | 124 |
| FUN-00095 | Data normalization | `clean_weld_df(spark_df)` | `notebooks/data_engineering/100_raw_to_bronze/weld_office/raw_to_bronze_weld_office_process_expiry.py:172` | 172 |
| FUN-00096 | Domain or utility | `get_fiscal_year(date)` | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py:211` | 211 |
| FUN-00097 | Domain or utility | `get_fiscal_quarter(date)` | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py:218` | 218 |
| FUN-00098 | Domain or utility | `get_previous_fiscal_quarter(number)` | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py:229` | 229 |
| FUN-00099 | Domain or utility | `get_fiscal_month(date)` | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py:236` | 236 |
| FUN-00100 | Domain or utility | `get_previous_fiscal_month(number)` | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py:243` | 243 |
| FUN-00101 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_company.py:147` | 147 |
| FUN-00102 | Schema and keys | `modify_column_name(column_name)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_contact.py:146` | 146 |
| FUN-00103 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_awards.py:147` | 147 |
| FUN-00104 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_descriptions.py:146` | 146 |
| FUN-00105 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_reference_testimonials.py:146` | 146 |
| FUN-00106 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_staff.py:147` | 147 |
| FUN-00107 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_project.py:190` | 190 |
| FUN-00108 | Schema and keys | `cast_specific_keys(df: DataFrame, key_columns: list)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:173` | 173 |
| FUN-00109 | Domain or utility | `load_base_table(spark: SparkSession=None, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:231` | 231 |
| FUN-00110 | Domain or utility | `join_equipment_dimension(df: DataFrame, spark: SparkSession=None, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:247` | 247 |
| FUN-00111 | Domain or utility | `join_work_order_dimension(df: DataFrame, spark: SparkSession=None, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:266` | 266 |
| FUN-00112 | Domain or utility | `join_schedule_type_dimension(df: DataFrame, spark: SparkSession=None, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:285` | 285 |
| FUN-00113 | Domain or utility | `join_schedule_status_dimension(df: DataFrame, spark: SparkSession=None, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:307` | 307 |
| FUN-00114 | Schema and keys | `cast_key_columns_to_string(df: DataFrame, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:328` | 328 |
| FUN-00115 | Domain or utility | `apply_implicit_decimal_adjustments(df: DataFrame, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:342` | 342 |
| FUN-00116 | Observability | `calculate_maintenance_metrics(df: DataFrame, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:360` | 360 |
| FUN-00117 | Schema and keys | `apply_final_column_transformations(df: DataFrame, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:449` | 449 |
| FUN-00118 | Domain or utility | `create_maintenance_schedule_dataframe(debug: bool=False, custom_base_table: str=None, custom_equipment_table: str=None, custom_work_order_table: str=None, custom_schedule_type_table: str=None, custom_schedule_status_table: str=None)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:496` | 496 |
| FUN-00119 | Schema and keys | `apply_final_column_transformations(df: DataFrame, debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:699` | 699 |
| FUN-00120 | Domain or utility | `create_maintenance_schedule_df(debug_flag: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:746` | 746 |
| FUN-00121 | Domain or utility | `get_maintenance_df(debug: bool=False)` | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py:801` | 801 |
| FUN-00122 | Domain or utility | `parse_date_flexible(date_str)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_bid_package.py:185` | 185 |
| FUN-00123 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cco.py:150` | 150 |
| FUN-00124 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract.py:146` | 146 |
| FUN-00125 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_vco.py:150` | 150 |
| FUN-00126 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cor.py:150` | 150 |
| FUN-00127 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_issue.py:150` | 150 |
| FUN-00128 | Data normalization | `HTMLClean(x)` | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_document.py:148` | 148 |
| FUN-00129 | Schema and keys | `get_data_type_for_column(dataframe, column_name)` | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_predecessor_task.py:563` | 563 |
| FUN-00130 | Domain or utility | `add_unknown_record_to_dataframe(dataframe)` | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_predecessor_task.py:566` | 566 |
| FUN-00131 | Domain or utility | `to_safe_string(v)` | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_pbi_datasets_export.py:207` | 207 |
| FUN-00132 | Schema and keys | `explode_qualifications_to_columns(df, source_col="also_qualifies_for", prefix="qualifies_for")` | `notebooks/data_engineering/300_silver_to_gold/weld_office/silver_to_gold_vw_wps_process_expiry_mapping.py:262` | 262 |
| FUN-00133 | Domain or utility | `min_export_date(environment)` | `notebooks/data_engineering/300_silver_to_gold/z_backfill/p6_fact_task_float_trend_weekly.py:149` | 149 |
| FUN-00134 | Domain or utility | `create_adf_client()` | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/run_adf_promote_metadata_pipeline.py:30` | 30 |
| FUN-00135 | Domain or utility | `create_resource_client()` | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/run_adf_promote_metadata_pipeline.py:43` | 43 |
| FUN-00136 | Domain or utility | `run_adf_pipeline(pipeline_name, resource_group_name, data_factory_name, params)` | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/run_adf_promote_metadata_pipeline.py:62` | 62 |
| FUN-00137 | Schema and keys | `get_schedule_validator_schema()` | `notebooks/data_engineering/maintenance/maintenance_define_schedulevalidator_schema.py:5` | 5 |
| FUN-00138 | Domain or utility | `convert_json_to_df(response)` | `notebooks/data_engineering/maintenance/maintenance_define_schedulevalidator_schema.py:189` | 189 |
| FUN-00139 | Runtime context | `create_table_for_enterprise_user_project(df, user)` | `notebooks/data_engineering/maintenance/maintenance_define_schedulevalidator_schema.py:212` | 212 |
| FUN-00140 | Domain or utility | `get_teambinder_shcema(form)` | `notebooks/data_engineering/maintenance/maintenance_define_teambinder_form_schema.py:5` | 5 |
| FUN-00141 | Runtime context | `list_notebook_names_in_folder(folder_path)` | `notebooks/data_engineering/maintenance/maintenance_execute_notebooks_in_optimize_folder.py:25` | 25 |
| FUN-00142 | Security and access | `get_access_token(tenant_id, client_id, client_secret)` | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_actualcost.py:84` | 84 |
| FUN-00143 | Domain or utility | `get_cost_data(subscription_id, access_token)` | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_actualcost.py:100` | 100 |
| FUN-00144 | Security and access | `get_access_token(tenant_id, client_id, client_secret)` | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_amortizedcost.py:84` | 84 |
| FUN-00145 | Domain or utility | `get_cost_data(subscription_id, access_token)` | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_amortizedcost.py:100` | 100 |
| FUN-00146 | Data normalization | `clean_string(col_name)` | `notebooks/data_engineering/miscellaneous_scripts/fact_project_performance_snapshot_history_load_transportation.py:43` | 43 |
| FUN-00147 | Domain or utility | `extract_timestamp(fileName)` | `notebooks/data_engineering/miscellaneous_scripts/raw_to_swat_files_all_sundt_foundation.py:239` | 239 |
| FUN-00148 | Runtime context | `workspace_to_environment()` | `notebooks/data_engineering/utility/common_functions.py:6` | 6 |
| FUN-00149 | Runtime context | `getCurrentUser()` | `notebooks/data_engineering/utility/common_functions.py:77` | 77 |
| FUN-00150 | Filesystem | `getFullNotebookPath()` | `notebooks/data_engineering/utility/common_functions.py:83` | 83 |
| FUN-00151 | Runtime context | `getNotebookName()` | `notebooks/data_engineering/utility/common_functions.py:89` | 89 |
| FUN-00152 | Domain or utility | `verifyNoTrailingSlash(a_path)` | `notebooks/data_engineering/utility/common_functions.py:95` | 95 |
| FUN-00153 | Domain or utility | `verifyLeadingSlash(a_path)` | `notebooks/data_engineering/utility/common_functions.py:104` | 104 |
| FUN-00154 | Filesystem | `normalizePath(a_path)` | `notebooks/data_engineering/utility/common_functions.py:113` | 113 |
| FUN-00155 | Filesystem | `combinePaths(*args)` | `notebooks/data_engineering/utility/common_functions.py:124` | 124 |
| FUN-00156 | Filesystem | `doesPathExist(path)` | `notebooks/data_engineering/utility/common_functions.py:142` | 142 |
| FUN-00157 | Filesystem | `isPathDirectory(path)` | `notebooks/data_engineering/utility/common_functions.py:154` | 154 |
| FUN-00158 | Delta processing | `doesDirectoryContainDeltaFiles(path)` | `notebooks/data_engineering/utility/common_functions.py:171` | 171 |
| FUN-00159 | Filesystem | `doesDirectoryContainCSVFiles(path)` | `notebooks/data_engineering/utility/common_functions.py:203` | 203 |
| FUN-00160 | Filesystem | `doesDirectoryContainJSONFiles(path)` | `notebooks/data_engineering/utility/common_functions.py:222` | 222 |
| FUN-00161 | Filesystem | `getFirstFileNameWithEndingMaskFromDirectory(path, mask)` | `notebooks/data_engineering/utility/common_functions.py:241` | 241 |
| FUN-00162 | Filesystem | `getNthFileNameWithEndingMaskFromDirectory(path, mask, index)` | `notebooks/data_engineering/utility/common_functions.py:260` | 260 |
| FUN-00163 | Filesystem | `renameFileExtension(fileName, newExtension)` | `notebooks/data_engineering/utility/common_functions.py:279` | 279 |
| FUN-00164 | Filesystem | `getBaseFileName(fileName)` | `notebooks/data_engineering/utility/common_functions.py:288` | 288 |
| FUN-00165 | Domain or utility | `compareListsWithoutOrder(list1, list2)` | `notebooks/data_engineering/utility/common_functions.py:293` | 293 |
| FUN-00166 | Domain or utility | `compareListsWithOrder(list1, list2)` | `notebooks/data_engineering/utility/common_functions.py:301` | 301 |
| FUN-00167 | Schema and keys | `replace_column_name_spaces(names)` | `notebooks/data_engineering/utility/common_functions.py:310` | 310 |
| FUN-00168 | Schema and keys | `convert_date_and_timestamp_columns(column_types, dataframe)` | `notebooks/data_engineering/utility/common_functions.py:317` | 317 |
| FUN-00169 | Domain or utility | `string_blank_to_null(column_types, dataframe)` | `notebooks/data_engineering/utility/common_functions.py:335` | 335 |
| FUN-00170 | Schema and keys | `trim_string_columns(column_types_list, dataframe)` | `notebooks/data_engineering/utility/common_functions.py:365` | 365 |
| FUN-00171 | Schema and keys | `reorder_columns_from_prefix(prefix, dataframe)` | `notebooks/data_engineering/utility/common_functions.py:393` | 393 |
| FUN-00172 | Domain or utility | `replaceBlankString(dataframe)` | `notebooks/data_engineering/utility/common_functions.py:412` | 412 |
| FUN-00173 | Domain or utility | `replaceAllBlanks(dataframe)` | `notebooks/data_engineering/utility/common_functions.py:424` | 424 |
| FUN-00174 | Schema and keys | `flatten_dataframe_array_columns(dataframe)` | `notebooks/data_engineering/utility/common_functions.py:434` | 434 |
| FUN-00175 | Domain or utility | `capitalizeFirstLetterAfterDelimeter(string, delimeter)` | `notebooks/data_engineering/utility/common_functions.py:443` | 443 |
| FUN-00176 | Domain or utility | `filter_list(list1, list2)` | `notebooks/data_engineering/utility/common_functions.py:451` | 451 |
| FUN-00177 | Domain or utility | `replace_special_characters(dataframe, characters_to_replace)` | `notebooks/data_engineering/utility/common_functions.py:457` | 457 |
| FUN-00178 | Schema and keys | `generate_hash_key(dataframe, column_name, column_list)` | `notebooks/data_engineering/utility/common_functions.py:475` | 475 |
| FUN-00179 | Observability | `get_table_last_operation_metrics(database, table)` | `notebooks/data_engineering/utility/common_functions.py:485` | 485 |
| FUN-00180 | Domain or utility | `check_if_table_exists(database, table)` | `notebooks/data_engineering/utility/common_functions.py:536` | 536 |
| FUN-00181 | Domain or utility | `check_if_cdc_feed_enabled(database, table)` | `notebooks/data_engineering/utility/common_functions.py:554` | 554 |
| FUN-00182 | Delta processing | `check_if_auto_merge_enabled(database, table)` | `notebooks/data_engineering/utility/common_functions.py:592` | 592 |
| FUN-00183 | Domain or utility | `check_if_auto_compact_enabled(database, table)` | `notebooks/data_engineering/utility/common_functions.py:629` | 629 |
| FUN-00184 | Runtime context | `get_current_environment_from_cluster_tags()` | `notebooks/data_engineering/utility/common_functions.py:666` | 666 |
| FUN-00185 | Domain or utility | `add_table_comment(database, table, comment)` | `notebooks/data_engineering/utility/common_functions.py:705` | 705 |
| FUN-00186 | Security and access | `set_ownership(database, principal, table=None, view=None)` | `notebooks/data_engineering/utility/common_functions.py:729` | 729 |
| FUN-00187 | Domain or utility | `check_if_table_exists(database, table)` | `notebooks/data_engineering/utility/common_functions.py:762` | 762 |
| FUN-00188 | Domain or utility | `dynamically_union_dataframes(df_a, df_b)` | `notebooks/data_engineering/utility/common_functions.py:777` | 777 |
| FUN-00189 | Filesystem | `get_external_location_path(container_name)` | `notebooks/data_engineering/utility/common_functions.py:803` | 803 |
| FUN-00190 | Domain or utility | `ignoreAscii(x)` | `notebooks/data_engineering/utility/common_functions.py:813` | 813 |
| FUN-00191 | Schema and keys | `ignoreAsciiColumns(dataframe)` | `notebooks/data_engineering/utility/common_functions.py:823` | 823 |
| FUN-00192 | Filesystem | `source_file_type(df)` | `notebooks/data_engineering/utility/common_functions.py:836` | 836 |
| FUN-00193 | Delta processing | `bronze_to_silver_drop_duplicates(bronze_database, silver_database, silver_table, has_primary_keys, primary_key_column_list, max_silver_timestamp, last_etl_raw_timestamp, etl_source_file_type, is_incremental=None, is_snapshot=None, snapshot_period=None, is_full_load=None, df=None)` | `notebooks/data_engineering/utility/common_functions.py:851` | 851 |
| FUN-00194 | Delta processing | `staged_silver_drop_duplicates(df, has_primary_keys, primary_key_column_list)` | `notebooks/data_engineering/utility/common_functions.py:1083` | 1083 |
| FUN-00195 | Schema and keys | `add_date_field_for_date_keys(database, table, column_prefix)` | `notebooks/data_engineering/utility/common_functions.py:1107` | 1107 |
| FUN-00196 | Security and access | `define_pii_view(pii_column_list, exclude_groups, view_name, view_database, database, table, column_prefix=None)` | `notebooks/data_engineering/utility/common_functions.py:1149` | 1149 |
| FUN-00197 | Domain or utility | `create_smenatic_view(view_name, view_database, database, table, owner, comment, exclude_groups=None, pii_column_list=None)` | `notebooks/data_engineering/utility/common_functions.py:1225` | 1225 |
| FUN-00198 | Security and access | `assign_rls_by_project_number(view_name, view_database, database, table, project_id_column, source_system, exclude_groups, pii_column_list=None)` | `notebooks/data_engineering/utility/common_functions.py:1262` | 1262 |
| FUN-00199 | Schema and keys | `get_e1_mcu_columns(df)` | `notebooks/data_engineering/utility/common_functions.py:1423` | 1423 |
| FUN-00200 | Security and access | `grant_principal_select_access(database, table, include_groups)` | `notebooks/data_engineering/utility/common_functions.py:1443` | 1443 |
| FUN-00201 | Security and access | `revoke_principal_access(database, table, exclude_groups)` | `notebooks/data_engineering/utility/common_functions.py:1461` | 1461 |
| FUN-00202 | Domain or utility | `try_cast(value, data_type)` | `notebooks/data_engineering/utility/common_functions.py:1492` | 1492 |
| FUN-00203 | Schema and keys | `compare_and_update_schema(source_dataframe, target_database, target_table)` | `notebooks/data_engineering/utility/common_functions.py:1503` | 1503 |
| FUN-00204 | Delta processing | `upsert_delta_serverless(df, database: str, table: str, pk_cols)` | `notebooks/data_engineering/utility/common_functions.py:1533` | 1533 |
| FUN-00205 | Domain or utility | `makeexpr(column)` | `notebooks/data_engineering/utility/common_functions.py:346` | 346 |
| FUN-00206 | Domain or utility | `makeexpr(column)` | `notebooks/data_engineering/utility/common_functions.py:378` | 378 |
| FUN-00207 | Domain or utility | `expr(col)` | `notebooks/data_engineering/utility/common_functions.py:1590` | 1590 |
| FUN-00208 | Domain or utility | `__init__(self, gold_database, gold_table, notebook_name=None, partition_by=None, pii_columns=None)` | `notebooks/data_engineering/utility/gold_table_processor.py:25` | 25 |
| FUN-00209 | Schema and keys | `add_etl_timestamp_column_to_dataframe(self, dataframe, timestamp_value, column_name="etl_gold_timestamp")` | `notebooks/data_engineering/utility/gold_table_processor.py:65` | 65 |
| FUN-00210 | Schema and keys | `update_key_store(self, dataframe, primary_key_column_list, surrogate_key_column_name, surrogate_key_type, add_surrogate_key_column: bool, check_primary_key_violations=True)` | `notebooks/data_engineering/utility/gold_table_processor.py:74` | 74 |
| FUN-00211 | Security and access | `create_pii_view_statement(self, dataframe, user_list)` | `notebooks/data_engineering/utility/gold_table_processor.py:183` | 183 |
| FUN-00212 | Security and access | `has_pii(self)` | `notebooks/data_engineering/utility/gold_table_processor.py:192` | 192 |
| FUN-00213 | Security and access | `create_dynamic_pii_view(self)` | `notebooks/data_engineering/utility/gold_table_processor.py:198` | 198 |
| FUN-00214 | Domain or utility | `does_table_exist(self)` | `notebooks/data_engineering/utility/gold_table_processor.py:210` | 210 |
| FUN-00215 | Domain or utility | `create_hive_database(self)` | `notebooks/data_engineering/utility/gold_table_processor.py:222` | 222 |
| FUN-00216 | Domain or utility | `create_archive_hive_database(self)` | `notebooks/data_engineering/utility/gold_table_processor.py:239` | 239 |
| FUN-00217 | Delta processing | `write_delta_table(self, processed_dataframe)` | `notebooks/data_engineering/utility/gold_table_processor.py:253` | 253 |
| FUN-00218 | Schema and keys | `select_columns(self, dataframe, column_list)` | `notebooks/data_engineering/utility/gold_table_processor.py:272` | 272 |
| FUN-00219 | Schema and keys | `convertDateColumn(self, dataframe, column_name)` | `notebooks/data_engineering/utility/gold_table_processor.py:281` | 281 |
| FUN-00220 | Schema and keys | `checkPrimaryKeyViolations(self, dataframe, column_list)` | `notebooks/data_engineering/utility/gold_table_processor.py:291` | 291 |
| FUN-00221 | Delta processing | `merge_delta_table(self, processed_dataframe, primary_key_column_list)` | `notebooks/data_engineering/utility/gold_table_processor.py:318` | 318 |
| FUN-00222 | Schema and keys | `get_data_type_for_column(self, dataframe, column_name)` | `notebooks/data_engineering/utility/gold_table_processor.py:357` | 357 |
| FUN-00223 | Domain or utility | `add_unknown_record_to_dataframe(self, dataframe)` | `notebooks/data_engineering/utility/gold_table_processor.py:361` | 361 |
| FUN-00224 | Domain or utility | `add_table_comment(self, comment)` | `notebooks/data_engineering/utility/gold_table_processor.py:423` | 423 |
| FUN-00225 | Domain or utility | `get_job_status_for_run_id(run_id)` | `notebooks/data_engineering/utility/insert_silver_to_gold_metadata.py:191` | 191 |
| FUN-00226 | Domain or utility | `mssql_exec_nonqry(info)` | `notebooks/data_engineering/utility/log_operation_metrics.py:14` | 14 |
| FUN-00227 | Domain or utility | `get_mssql_info()` | `notebooks/data_engineering/utility/log_operation_metrics.py:44` | 44 |
| FUN-00228 | Observability | `update_operation_metrics_log(metrics_log_id, metrics_data, debug)` | `notebooks/data_engineering/utility/log_operation_metrics.py:78` | 78 |
| FUN-00229 | Domain or utility | `__init__(self)` | `notebooks/data_engineering/utility/nano_second_timer.py:28` | 28 |
| FUN-00230 | Domain or utility | `get_timer_in_milliseconds(self)` | `notebooks/data_engineering/utility/nano_second_timer.py:33` | 33 |
| FUN-00231 | Domain or utility | `get_timer_in_nanoseconds(self)` | `notebooks/data_engineering/utility/nano_second_timer.py:37` | 37 |
| FUN-00232 | Domain or utility | `reset_timer(self)` | `notebooks/data_engineering/utility/nano_second_timer.py:41` | 41 |
| FUN-00233 | Domain or utility | `__init__(self, view_name, anchor_sql_statement, recursive_sql_statement)` | `notebooks/data_engineering/utility/recursive_query_processor.py:12` | 12 |
| FUN-00234 | Domain or utility | `create_anchor_member(self)` | `notebooks/data_engineering/utility/recursive_query_processor.py:19` | 19 |
| FUN-00235 | Domain or utility | `execute_recursive_query(self)` | `notebooks/data_engineering/utility/recursive_query_processor.py:27` | 27 |
| FUN-00236 | Domain or utility | `createFinalDataframe(self, sort_column=None)` | `notebooks/data_engineering/utility/recursive_query_processor.py:37` | 37 |
| FUN-00237 | Domain or utility | `process(self, sort_column=None)` | `notebooks/data_engineering/utility/recursive_query_processor.py:55` | 55 |
| FUN-00238 | Domain or utility | `__init__(self, view_name, anchor_sql_statement, recursive_sql_statement, staging_database='operation_financials')` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:15` | 15 |
| FUN-00239 | Domain or utility | `create_anchor_member(self)` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:39` | 39 |
| FUN-00240 | Domain or utility | `execute_recursive_query(self)` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:55` | 55 |
| FUN-00241 | Domain or utility | `createFinalDataframe(self, sort_column=None)` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:109` | 109 |
| FUN-00242 | Data normalization | `cleanup(self)` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:125` | 125 |
| FUN-00243 | Domain or utility | `process(self, sort_column=None)` | `notebooks/data_engineering/utility/recursive_query_processor_v2.py:133` | 133 |
| FUN-00244 | Domain or utility | `julian_to_date_df(input_df, julian_date_columns)` | `notebooks/data_engineering/utility/user_defined_functions.py:9` | 9 |
| FUN-00245 | Schema and keys | `convert_single_date_column(julian_date)` | `notebooks/data_engineering/utility/user_defined_functions.py:86` | 86 |
| FUN-00246 | Domain or utility | `convert_single_date(julian_date)` | `notebooks/data_engineering/utility/user_defined_functions.py:10` | 10 |

## Required validation

- Identify shared functions that are production-critical versus domain-local helpers.
- Document inputs, outputs, side effects, failure behavior, security behavior, and modernization disposition using the function template.
- Reconcile static call relationships with notebook execution paths and job parameters.
