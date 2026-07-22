# Job Catalog

Generated from `DW2023-Databricks.zip` on 2026-07-22.

This catalog lists Databricks job JSON definitions present in repository evidence. Deployment and schedule state must be reconciled with Databricks Jobs API output before use as production truth.

| ID | Job | Tasks | Notebooks | Parameters | Run as |
|---|---|---:|---|---:|---|
| JOB-00001 | `job_01_bronze_to_silver` | 1 | `/Workspace/data_engineering/200_bronze_to_silver/bronze_to_silver` | 13 | jminer@sundt.com |
| JOB-00002 | `job_02_silver_to_gold` | 1 | `/Workspace/data_engineering/300_silver_to_gold/silver_to_gold_master` | 4 | jminer@sundt.com |
| JOB-00003 | `job_03_bronze_asql` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00004 | `job_04_bronze_asql_ineight` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00005 | `job_05_bronze_asql_qdr` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00006 | `job_06_bronze_asql_sdat_web_app` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00007 | `job_07_bronze_cslb_lisence` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/cslb_data/source_to_bronze_california_license_data` | 7 | jminer@sundt.com |
| JOB-00008 | `job_08_bronze_rest_api_cosetial` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_master` | 8 | jminer@sundt.com |
| JOB-00009 | `job_09_bronze_rest_api_pbi` | 1 | `/Workspace/data_engineering/000_source_to_raw/source-to-raw-powerbi-master` | 11 | jminer@sundt.com |
| JOB-00010 | `job_10_bronze_sql` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00011 | `job_11_bronze_sql_cosential` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00012 | `job_12_bronze_sql_destimator` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00013 | `job_13_bronze_sql_e1` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00014 | `job_14_bronze_sql_ineight_document` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00015 | `job_16_bronze_fs_heavy_job` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00016 | `job_17_bronze_sfs_zip_code` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze_zipcodes_all` | 7 | jminer@sundt.com |
| JOB-00017 | `job_20_bronze_bronze_sharepoint` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/raw_to_bronze` | 7 | jminer@sundt.com |
| JOB-00018 | `job_21_bronze_soap_b2g` | 1 | `/Workspace/data_engineering/100_raw_to_bronze/b2g/raw_to_bronze_b2g_api_master` | 8 | jminer@sundt.com |

## Required validation

- Reconcile repository job definitions with deployed Databricks jobs in development, test, and production.
- Confirm schedules, triggers, retries, permissions, owners, alerts, and run identities.
- Map each job task to notebook records, data movement records, and operational support procedures.
