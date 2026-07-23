# Resolved Metadata Catalog

Generated from CSV exports in `metadata` on 2026-07-22.

This catalog joins exported `DataProcess` rows to `DataSource` rows and attempts to resolve each `dataProcessPathOrProcedure` to a Databricks notebook discovered in the repository archive.

## Exported table counts

| Table | Rows | Columns |
|---|---:|---:|
| `datasource` | 501 | 37 |
| `dataprocess` | 907 | 25 |
| `dataprocessdependency` | 1035 | 9 |

## Path resolution

| Status | Process rows |
|---|---:|
| resolved_notebook | 877 |
| unresolved_notebook_path | 30 |

## Source types

| Source type | Source rows |
|---|---:|
| Azure SQL Database | 217 |
| SQL Server | 203 |
| REST API | 50 |
| Sharepoint List | 18 |
| Azure SQL Database - SDAT Web App | 4 |
| File System | 3 |
| SOAP API | 3 |
| SFTP File | 1 |
| demo | 1 |
| API | 1 |

## Process types

| Process type | Rows |
|---|---:|
| silver | 495 |
| gold | 412 |

## Unresolved notebook paths

These enabled metadata rows reference Databricks-style notebook paths that were not found in the Databricks repository archive. Treat them as migration blockers until the source notebooks are recovered, replaced, or retired.

| Subject area | Missing paths |
|---|---:|
| textura | 16 |
| ineight_schedule | 7 |
| bridgit_reporting | 4 |
| origami | 2 |
| operation_financials | 1 |

| ID | Target | Metadata path |
|---|---|---|
| META-PROC-00787 | operation_financials.fact_project_labor_cost | 300_silver_to_gold/operation_financials/silver_to_gold_fact_project_labor_cost |
| META-PROC-00789 | bridgit_reporting.dim_person | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_person |
| META-PROC-00790 | bridgit_reporting.dim_project_bridgit | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_project_bridgit |
| META-PROC-00792 | origami.equipment | 300_silver_to_gold/origami/silver_to_gold_origami_equipment |
| META-PROC-00793 | origami.locations | 300_silver_to_gold/origami/silver_to_gold_origami_locations |
| META-PROC-00794 | textura.bridge_project_user_role_textura | 300_silver_to_gold/textura/silver_to_gold_bridge_project_user_role |
| META-PROC-00795 | textura.dim_contract_textura | 300_silver_to_gold/textura/silver_to_gold_dim_contract |
| META-PROC-00796 | textura.dim_draw_textura | 300_silver_to_gold/textura/silver_to_gold_dim_draw |
| META-PROC-00797 | textura.dim_project_textura | 300_silver_to_gold/textura/silver_to_gold_dim_project |
| META-PROC-00798 | textura.dim_subcontractor | 300_silver_to_gold/textura/silver_to_gold_dim_subcontractor |
| META-PROC-00799 | textura.dim_supplier_tracking | 300_silver_to_gold/textura/silver_to_gold_dim_supplier_tracking |
| META-PROC-00800 | textura.dim_user_textura | 300_silver_to_gold/textura/silver_to_gold_dim_user |
| META-PROC-00801 | textura.fact_budget_line_textura | 300_silver_to_gold/textura/silver_to_gold_fact_budgetline |
| META-PROC-00802 | textura.fact_change_order_textura | 300_silver_to_gold/textura/silver_to_gold_fact_change_order |
| META-PROC-00803 | textura.fact_invoice_approval_textura | 300_silver_to_gold/textura/silver_to_gold_fact_invoice_approval |
| META-PROC-00804 | textura.fact_invoice_line_textura | 300_silver_to_gold/textura/silver_to_gold_fact_invoiceline |
| META-PROC-00805 | textura.fact_invoice_textura | 300_silver_to_gold/textura/silver_to_gold_fact_invoice |
| META-PROC-00806 | textura.fact_lien_waiver_textura | 300_silver_to_gold/textura/silver_to_gold_fact_lien_waiver |
| META-PROC-00807 | textura.fact_payment_hold_textura | 300_silver_to_gold/textura/silver_to_gold_fact_payment_hold |
| META-PROC-00808 | textura.fact_payment_textura | 300_silver_to_gold/textura/silver_to_gold_fact_payment |
| META-PROC-00809 | textura.fact_supplier_tracking | 300_silver_to_gold/textura/silver_to_gold_fact_supplier_tracking |
| META-PROC-00896 | bridgit_reporting.dim_role | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_role |
| META-PROC-00897 | bridgit_reporting.fact_allocations | 300_silver_to_gold/bridgit_reporting/silver_to_gold_fact_allocations |
| META-PROC-00901 | ineight_schedule.dim_activity_code | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_activity_code |
| META-PROC-00902 | ineight_schedule.dim_task | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_task |
| META-PROC-00903 | ineight_schedule.dim_wbs | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_wbs |
| META-PROC-00904 | ineight_schedule.fact_task | 300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task |
| META-PROC-00905 | ineight_schedule.fact_task_baseline | 300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task_baseline |
| META-PROC-00906 | ineight_schedule_v.fact_task_baseline_current_v | 300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_baseline_current |
| META-PROC-00907 | ineight_schedule_v.fact_task_current_v | 300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_current |

## Enabled process index

| ID | Process | Batch | Source | Source type | Target | Path status | Notebook | Incremental |
|---|---|---|---|---|---|---|---|---|
| META-PROC-00001 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_Office | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00002 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_Parking | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00003 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_Project | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00004 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_Renovation | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00005 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_SM | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00006 | silver | daily | destimator | SQL Server | silver_destimator.EstimateFeeDataDetails_forDW | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00007 | silver | daily | destimator | SQL Server | silver_destimator.EstimateSummaryDataDetails_forDW | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00008 | silver | daily | destimator | SQL Server | silver_destimator.v_Datawarehouse_HistoricalData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00009 | silver | daily | p6 | SQL Server | silver_p6.ACTVCODE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00010 | silver | daily | p6 | SQL Server | silver_p6.ACTVTYPE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00011 | silver | daily | p6 | SQL Server | silver_p6.CALENDAR | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00012 | silver | daily | p6 | SQL Server | silver_p6.FINDATES | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00013 | silver | daily | p6 | SQL Server | silver_p6.PCATTYPE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00014 | silver | daily | p6 | SQL Server | silver_p6.PCATVAL | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00015 | silver | daily | p6 | SQL Server | silver_p6.PROJECT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00016 | silver | daily | p6 | SQL Server | silver_p6.PROJPCAT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00017 | silver | daily | p6 | SQL Server | silver_p6.PROJWBS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00018 | silver | daily | p6 | SQL Server | silver_p6.RSRC | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00019 | silver | daily | p6 | SQL Server | silver_p6.Task | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00020 | silver | daily | p6 | SQL Server | silver_p6.TASKACTV | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00021 | silver | daily | p6 | SQL Server | silver_p6.TASKPRED | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00022 | silver | daily | p6 | SQL Server | silver_p6.TASKSUM | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00023 | silver | daily | e1 | SQL Server | silver_e1.F0111 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00024 | silver | daily | mpr | Azure SQL Database | silver_mpr.Costs | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00025 | silver | daily | mpr | Azure SQL Database | silver_mpr.Employees | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00026 | silver | daily | heavyjob | SQL Server | silver_heavyjob.COSTLEDG | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00027 | silver | daily | heavyjob | SQL Server | silver_heavyjob.COSTCODE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00028 | silver | daily | mpr | Azure SQL Database | silver_mpr.LU_Status | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00029 | silver | daily | mpr | Azure SQL Database | silver_mpr.Margins | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00030 | silver | daily | mpr | Azure SQL Database | silver_mpr.PCCOs | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00031 | silver | daily | mpr | Azure SQL Database | silver_mpr.Projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00032 | silver | daily | destimator | Sharepoint List | silver_destimator.ENRBuildingCostIndex | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00033 | silver | daily | cosential_api | REST API | silver_cosential_api.contact_opportunities | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00034 | silver | daily | cosential | SQL Server | silver_cosential.opportunity_history | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00035 | silver | daily | mpr | Azure SQL Database | silver_mpr.Reconciles | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00036 | silver | daily | mpr | Azure SQL Database | silver_mpr.Reviewers | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00037 | silver | daily | mpr | Azure SQL Database | silver_mpr.UPQAs | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00038 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_General | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00039 | silver | daily | destimator | SQL Server | silver_destimator.EstimateDataDetails_HMF | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00040 | silver | daily | p6 | SQL Server | silver_p6.tbl_Sundt_API | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00041 | silver | daily | p6 | SQL Server | silver_p6.tbl_Sundt_API_Weekly | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00042 | silver | daily | p6 | SQL Server | silver_p6.WBSBUDG | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00043 | silver | daily | heavyjob | SQL Server | silver_heavyjob.COSCODNT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00044 | silver | daily | mpr | Azure SQL Database | silver_mpr.Mprs | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00045 | silver | daily | e1 | SQL Server | silver_e1.F0005 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00046 | silver | daily | e1 | SQL Server | silver_e1.F0006 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00047 | silver | daily | e1 | SQL Server | silver_e1.F00092 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00048 | silver | daily | e1 | SQL Server | silver_e1.F0010 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00049 | silver | daily | e1 | SQL Server | silver_e1.F0101 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00050 | silver | daily | e1 | SQL Server | silver_e1.F0115 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00051 | silver | daily | e1 | SQL Server | silver_e1.F0116 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00052 | silver | daily | e1 | SQL Server | silver_e1.F03B11 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00053 | silver | daily | e1 | SQL Server | silver_e1.F03B14 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00054 | silver | daily | e1 | SQL Server | silver_e1.F0411 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00055 | silver | daily | e1 | SQL Server | silver_e1.F0901 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00056 | silver | daily | e1 | SQL Server | silver_e1.F0902 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00057 | silver | daily | e1 | SQL Server | silver_e1.F0911 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00058 | silver | daily | e1 | SQL Server | silver_e1.F1201 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00059 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwProjectandCharacteristics | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00060 | silver | daily | powerbi | REST API | silver_powerbi.groups | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00061 | silver | daily | mpr | Azure SQL Database | silver_mpr.CORs | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00062 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_CATEGORY | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00063 | silver | daily | e1 | SQL Server | silver_e1.F4311 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00064 | gold | daily |  |  | security.stg_user_project_relationship | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_project_relationship.py` | 0 |
| META-PROC-00065 | gold | daily |  |  | conformed.dim_company | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_company.py` | 0 |
| META-PROC-00066 | silver | daily | e1 | SQL Server | silver_e1.F4311T | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00067 | silver | daily | e1 | SQL Server | silver_e1.F5144 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00068 | silver | daily | e1 | SQL Server | silver_e1.F570901D | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00069 | silver | daily | e1 | SQL Server | silver_e1.F570902D | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00070 | silver | daily | e1 | SQL Server | silver_e1.F5789006 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00072 | silver | daily | e1 | SQL Server | silver_e1.F0413 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00074 | silver | daily | e1 | SQL Server | silver_e1.F4301 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00075 | silver | daily | qdr | Azure SQL Database | silver_qdr.Companies | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00076 | silver | daily | qdr | Azure SQL Database | silver_qdr.CostCenters | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00077 | silver | daily | qdr | Azure SQL Database | silver_qdr.CostCentersCompanies | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00078 | silver | daily | qdr | Azure SQL Database | silver_qdr.CSICODE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00079 | silver | daily | qdr | Azure SQL Database | silver_qdr.E1_ActualCost | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00080 | silver | daily | qdr | Azure SQL Database | silver_qdr.E1_ActualUnits | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00081 | silver | daily | qdr | Azure SQL Database | silver_qdr.EMPLOYEES | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00082 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_APPROVALS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00083 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_ATTACHEDFILE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00084 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_CHRONOLOGYEVENTS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00085 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_CONTRIBUTINGFACTORS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00086 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlPayItemEarning | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00087 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_CORRECTIVEACTIONPLAN | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00088 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_CRAFT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00089 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_DISCIPLINE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00090 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_DISPOSITION | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00091 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_DIVISION | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00092 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_Group | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00093 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_History | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00094 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_PARTICIPANTS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00095 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_PCCPCATEGORY | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00096 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_PREVENTATIVEACTIONS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00097 | gold | daily |  |  | operation_financials.dim_account_master | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_account_master.py` | 0 |
| META-PROC-00098 | gold | daily |  |  | operation_financials.fact_contracts | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_contracts.py` | 0 |
| META-PROC-00099 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlPayItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00100 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlOriginalBudget | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00101 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_ProjectsWithEmployeeRoles | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00102 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_REPORT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00103 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_ROOTCAUSE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00104 | silver | daily | qdr | Azure SQL Database | silver_qdr.QDR_STATUS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00105 | silver | daily | qdr | Azure SQL Database | silver_qdr.SITES | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00106 | silver | daily | cosential | SQL Server | silver_cosential.Companies | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00107 | silver | daily | cosential | SQL Server | silver_cosential.Contact_Lead_ContactRoles | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00108 | silver | daily | cosential | SQL Server | silver_cosential.Contacts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00109 | silver | daily | prolog | SQL Server | silver_prolog.Company | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00110 | silver | daily | prolog | SQL Server | silver_prolog.Contacts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00111 | silver | daily | prolog | SQL Server | silver_prolog.Crews | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00112 | silver | daily | prolog | SQL Server | silver_prolog.LU_Action | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00113 | silver | daily | prolog | SQL Server | silver_prolog.LU_Classification | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00114 | silver | daily | prolog | SQL Server | silver_prolog.LU_Discipline | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00115 | silver | daily | prolog | SQL Server | silver_prolog.LU_PCOCat | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00116 | silver | daily | prolog | SQL Server | silver_prolog.LU_SafetyType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00117 | silver | daily | prolog | SQL Server | silver_prolog.LU_SubRegisterType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00118 | silver | daily | prolog | SQL Server | silver_prolog.LU_Trade | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00119 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_Budget | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00120 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_ChangeOrderRequests | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00121 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_ContactsProjectsLinks | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00122 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_Contracts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00123 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_ContractSchedofValues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00124 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_DailyWork | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00125 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_DwActiveDirectoryUsersOneRow | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00126 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_Labor | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00127 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_PotentialCO | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00128 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_PotentialCOItems | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00129 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_PrimeContractCO | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00130 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_Projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00131 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_PurchaseOrderItems | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00132 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_PurchaseOrders | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00133 | gold | daily |  |  | web_app_integration.pbi_workspace_reports_export | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_workspace_report_export.py` | 0 |
| META-PROC-00134 | gold | daily |  |  | schedule.dim_float_criteria | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_float_criteria.py` | 0 |
| META-PROC-00135 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_RFI | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00136 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_Safety | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00137 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_SubcontractCO | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00138 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_SubmittalPackages | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00139 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_SubmittalRegister | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00140 | silver | daily | prolog | SQL Server | silver_prolog.v_SundtDatawarehouse_SubmittalReviewers | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00141 | silver | daily | cosential | SQL Server | silver_cosential.Countries | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00142 | silver | daily | cosential | SQL Server | silver_cosential.FirmOrg_AssociateOfficeDivision | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00143 | silver | daily | cosential | SQL Server | silver_cosential.FirmOrg_Divisions | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00144 | silver | daily | cosential | SQL Server | silver_cosential.FirmOrg_OfficeDivision | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00145 | silver | daily | cosential | SQL Server | silver_cosential.FirmOrg_Offices | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00146 | silver | daily | cosential | SQL Server | silver_cosential.FirmOrg_Studios | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00147 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00148 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_ConstructionType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00149 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_ContractType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00150 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_DeliveryMethod | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00151 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Divisions | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00152 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_ext | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00153 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Offices | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00154 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_PrimaryCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00155 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_ProspectTypes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00156 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_SecondaryCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00157 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Staff | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00158 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Studios | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00159 | silver | daily | cosential | SQL Server | silver_cosential.Personnel | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00160 | silver | daily | cosential | SQL Server | silver_cosential.Personnel_PrevProjectExperience | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00161 | silver | daily | cosential | SQL Server | silver_cosential.Project_Awards | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00162 | silver | daily | cosential | SQL Server | silver_cosential.Project_Certifications | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00163 | silver | daily | cosential | SQL Server | silver_cosential.Project_clienttypes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00164 | silver | daily | cosential | SQL Server | silver_cosential.Project_ConstructionType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00165 | silver | daily | cosential | SQL Server | silver_cosential.Project_ConstSchedule | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00166 | gold | daily |  |  | safety.dim_form | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_form.py` | 0 |
| META-PROC-00167 | gold | daily |  |  | deficiencies.fact_deficiency | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_fact_deficiency.py` | 0 |
| META-PROC-00168 | gold | daily |  |  | schedule.fact_task_current_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_task_current.py` | 0 |
| META-PROC-00169 | silver | daily | cosential | SQL Server | silver_cosential.Project_Consultants | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00170 | silver | daily | cosential | SQL Server | silver_cosential.Project_Consultants_Contacts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00171 | silver | daily | cosential | SQL Server | silver_cosential.Project_CostFee | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00172 | silver | daily | cosential | SQL Server | silver_cosential.Project_DeliveryMethod | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00173 | silver | daily | cosential | SQL Server | silver_cosential.Project_Descriptions | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00174 | silver | daily | cosential | SQL Server | silver_cosential.Project_Divisions | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00175 | silver | daily | cosential | SQL Server | silver_cosential.Project_FeesCosts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00176 | silver | daily | cosential | SQL Server | silver_cosential.Project_LEED | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00177 | silver | daily | cosential | SQL Server | silver_cosential.Project_Offices | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00178 | silver | daily | cosential | SQL Server | silver_cosential.Project_OwnerClient | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00179 | silver | daily | cosential | SQL Server | silver_cosential.Project_OwnerClient_Contacts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00180 | silver | daily | cosential | SQL Server | silver_cosential.Project_PrimaryCatgories | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00181 | silver | daily | cosential | SQL Server | silver_cosential.Project_Reference | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00182 | silver | daily | cosential | SQL Server | silver_cosential.Project_ReferenceTestimonials | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00183 | silver | daily | cosential | SQL Server | silver_cosential.Project_SecondaryCategories | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00184 | silver | daily | cosential | SQL Server | silver_cosential.Project_ServiceTypes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00185 | silver | daily | cosential | SQL Server | silver_cosential.Project_StaffTeam | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00186 | silver | daily | cosential | SQL Server | silver_cosential.Project_Studios | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00187 | silver | daily | cosential | SQL Server | silver_cosential.Projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00188 | silver | daily | cosential | SQL Server | silver_cosential.Projects_ext | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00189 | silver | daily | cosential | SQL Server | silver_cosential.Projects_JointVenture | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00190 | silver | daily | azureactivedirectory | REST API | silver_azureactivedirectory.users | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00191 | silver | daily | cosential | SQL Server | silver_cosential.Roles | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00192 | silver | daily | cosential | SQL Server | silver_cosential.SalesGoals | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00193 | silver | daily | cosential | SQL Server | silver_cosential.SalesGoals_ValuesByMonth | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00194 | silver | daily | cosential | SQL Server | silver_cosential.States | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00195 | silver | daily | e1 | SQL Server | silver_e1.F01151 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00196 | silver | daily | e1 | SQL Server | silver_e1.F060116 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00197 | silver | daily | e1 | SQL Server | silver_e1.F1207 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00198 | silver | daily | e1 | SQL Server | silver_e1.F1204 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00199 | silver | daily | e1 | SQL Server | silver_e1.F08001 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00200 | silver | daily | e1 | SQL Server | silver_e1.F1217 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00201 | silver | daily | webapp | Azure SQL Database - SDAT Web App | silver_webapp.Contacts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00202 | gold | daily |  |  | safety.dim_form_location | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_form_location.py` | 0 |
| META-PROC-00203 | gold | daily |  |  | deficiencies.dim_deficiency_cause_disposition | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_cause_disposition.py` | 0 |
| META-PROC-00204 | gold | daily |  |  | security.dim_active_directory_user | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_dim_active_directory_user.py` | 0 |
| META-PROC-00205 | silver | daily | webapp | Azure SQL Database - SDAT Web App | silver_webapp.Projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00206 | silver | daily | e1 | SQL Server | silver_e1.F0401 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00207 | silver | daily | e1 | SQL Server | silver_e1.F0150 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00208 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceCurrentEventTaskData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00209 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceFormsandProject | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00210 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceScheduledTaskData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00211 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceCategoryData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00212 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceGeneralHeaderData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00213 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceEventTaskData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00214 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceResponseType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00215 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceResponseTypeElement | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00216 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceQuestionText | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00217 | silver | daily | e1 | SQL Server | silver_e1.F0618 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00218 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwInEightOBSData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00219 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreOrganization | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00220 | silver | daily | powerbi | REST API | silver_powerbi.reports | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00221 | silver | daily | destimator | Sharepoint List | silver_destimator.RSMeansEscalator | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00222 | silver | daily | e1 | SQL Server | silver_e1.F4801 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00223 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProject | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00224 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwBICoreProjectDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00226 | silver | daily | p6 | SQL Server | silver_p6.TASKRSRC | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00227 | gold | daily |  |  | equipment.dim_equipment | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment.py` | 0 |
| META-PROC-00228 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleWorkBreakdownStructureType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00229 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProjectAssignedContact | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00230 | silver | daily | destimator | Sharepoint List | silver_destimator.DEstimator_SundtCMT_ST_Dictionary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00231 | gold | daily |  |  | prolog.fact_budget | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_budget.py` | 0 |
| META-PROC-00232 | gold | daily |  |  | prolog.fact_change_order_requests | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_change_order_requests.py` | 0 |
| META-PROC-00233 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleWorkBreakdownStructure | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00234 | gold | daily |  |  | operation_financials.fact_project_cash_position | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_project_cash_position.py` | 0 |
| META-PROC-00235 | gold | daily |  |  | schedule.dim_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_task.py` | 0 |
| META-PROC-00236 | gold | daily |  |  | schedule.dim_wbs | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_wbs.py` | 0 |
| META-PROC-00237 | gold | daily |  |  | schedule.dim_activity_code | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_activity_code.py` | 0 |
| META-PROC-00238 | gold | daily |  |  | safety.fact_event_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_event_task.py` | 0 |
| META-PROC-00239 | gold | daily |  |  | schedule.dim_successor_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_successor_task.py` | 0 |
| META-PROC-00240 | gold | daily |  |  | safety_v.fact_stcky_svis_event_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_svis_event_task.py` | 0 |
| META-PROC-00241 | gold | daily |  |  | deficiencies.dim_deficiency_division_group | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_division_group.py` | 0 |
| META-PROC-00242 | gold | daily |  |  | safety_v.fact_other_event_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_other_event_task.py` | 0 |
| META-PROC-00243 | gold | daily |  |  | safety.dim_body_part | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_body_part.py` | 0 |
| META-PROC-00245 | gold | daily |  |  | conformed.dim_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_project.py` | 0 |
| META-PROC-00246 | gold | daily |  |  | safety.dim_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_status.py` | 0 |
| META-PROC-00247 | gold | daily |  |  | safety.dim_reporter_and_assignor | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_reporter_and_assignor.py` | 0 |
| META-PROC-00248 | gold | daily |  |  | schedule.dim_predecessor_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_predecessor_task.py` | 0 |
| META-PROC-00249 | gold | daily |  |  | deficiencies.dim_deficiency_category | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_category.py` | 0 |
| META-PROC-00251 | gold | daily |  |  | labor.fact_monthly_subcontractors_hours_by_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_monthly_subcontractors_hours_by_project.py` | 0 |
| META-PROC-00252 | gold | daily |  |  | schedule.fact_weekly_labor_head_count | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_weekly_labor_head_count.py` | 0 |
| META-PROC-00253 | gold | daily |  |  | labor.fact_weekly_labor_hours_by_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_weekly_labor_hours_by_project.py` | 0 |
| META-PROC-00254 | gold | daily |  |  | conformed_v.dim_overhead_business_unit_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_vw_business_unit.py` | 0 |
| META-PROC-00255 | gold | daily |  |  | safety_v.fact_incidents_event_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_svis_event_task.py` | 0 |
| META-PROC-00256 | gold | daily |  |  | web_app_integration.company_export | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_company_export.py` | 0 |
| META-PROC-00257 | gold | daily |  |  | schedule.dim_group | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_group.py` | 0 |
| META-PROC-00258 | gold | daily |  |  | deficiencies.dim_deficiency_csi_code | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_csi_code.py` | 0 |
| META-PROC-00259 | gold | daily |  |  | cosential.bridge_cosential_project_opportunity_contact | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_bridge_project_opportunity_contact.py` | 0 |
| META-PROC-00261 | gold | daily |  |  | security.bridge_user_project_relationship | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_bridge_user_project_relationship.py` | 0 |
| META-PROC-00262 | gold | daily |  |  | operation_financials.fact_account_balance | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance.py` | 0 |
| META-PROC-00263 | gold | daily |  |  | conformed.dim_date | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py` | 0 |
| META-PROC-00264 | gold | daily |  |  | schedule.fact_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_fact_task.py` | 1 |
| META-PROC-00265 | silver | daily | cosential_api | REST API | silver_cosential_api.contact_projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00266 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreUsers | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00267 | gold | daily |  |  | prolog.fact_contact_list_by_project_number | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contactlist_by_project_number.py` | 0 |
| META-PROC-00268 | silver | daily | cosential_api | REST API | silver_cosential_api.opportunities | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00269 | gold | daily |  |  | prolog.fact_contract_sched_of_values | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contract_sched_values.py` | 0 |
| META-PROC-00270 | gold | daily |  |  | prolog.fact_contracts | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contracts.py` | 0 |
| META-PROC-00271 | gold | daily |  |  | prolog.fact_daily_reports | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_daily_reports.py` | 0 |
| META-PROC-00272 | gold | daily |  |  | safety.dim_injury_cause | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_injury_cause.py` | 0 |
| META-PROC-00273 | gold | daily |  |  | prolog.fact_fieldpo | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_fieldpo.py` | 0 |
| META-PROC-00274 | gold | daily |  |  | safety.dim_obs_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_obs_project.py` | 0 |
| META-PROC-00275 | gold | daily |  |  | mpr.dim_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_dim_mpr_status.py` | 0 |
| META-PROC-00276 | gold | daily |  |  | mpr.fact_cor_adjustment | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_cor_adjustments.py` | 0 |
| META-PROC-00277 | gold | daily |  |  | mpr.fact_cost_vs_budget_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_costs_vs_budget_summary.py` | 0 |
| META-PROC-00278 | gold | daily |  |  | mpr.fact_mpr_base | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_mpr_base.py` | 0 |
| META-PROC-00279 | gold | daily |  |  | mpr.fact_pcco_adjustments | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_pcco_adjustments.py` | 0 |
| META-PROC-00280 | gold | daily |  |  | mpr.fact_reconciliation | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_reconciliation.py` | 0 |
| META-PROC-00281 | gold | daily |  |  | mpr.fact_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_status.py` | 0 |
| META-PROC-00282 | gold | daily |  |  | mpr.fact_upqa | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_upqa.py` | 0 |
| META-PROC-00284 | gold | daily |  |  | labor.fact_weekly_labor_head_count | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_weekly_labor_head_count.py` | 0 |
| META-PROC-00285 | gold | daily |  |  | operation_financials.fact_pco_line_items | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_pco_line_items.py` | 0 |
| META-PROC-00286 | gold | daily |  |  | web_app_integration.pbi_dataset_export | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_pbi_datasets_export.py` | 0 |
| META-PROC-00287 | gold | daily |  |  | prolog.fact_pccos | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_pccos.py` | 0 |
| META-PROC-00288 | gold | daily |  |  | prolog.fact_potential_change_orders | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_potential_change_orders.py` | 0 |
| META-PROC-00289 | silver | daily | e1 | SQL Server | silver_e1.F06156 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00290 | gold | daily |  |  | operation_financials.fact_accounts_receivable | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_accounts_receivable.py` | 0 |
| META-PROC-00291 | silver | daily | cosential | SQL Server | silver_cosential.JointVenture_Other | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00293 | silver | daily | heavyjob | File System | silver_heavyjob.SCRDR_Labor | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00294 | gold | daily |  |  | destimator.dim_enr_building_cost_index | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_enr_building_cost_Index.py` | 0 |
| META-PROC-00295 | gold | daily |  |  | heavyjob.fact_daily_cost_by_cost_code | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_daily_cost_by_cost_code.py` | 0 |
| META-PROC-00296 | gold | daily |  |  | heavyjob.fact_equip_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_equip_detail.py` | 0 |
| META-PROC-00297 | gold | daily |  |  | heavyjob.fact_labor_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_labor_detail.py` | 0 |
| META-PROC-00298 | gold | daily |  |  | operation_financials.fact_project_billing | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_project_billing.py` | 0 |
| META-PROC-00299 | gold | daily |  |  | destimator.dim_estimate | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate.py` | 0 |
| META-PROC-00300 | gold | daily |  |  | destimator.dim_estimate_feedata | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate_feedata.py` | 0 |
| META-PROC-00301 | gold | daily |  |  | destimator.dim_estimate_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate_summary.py` | 0 |
| META-PROC-00302 | gold | daily |  |  | destimator.dim_estimate_sundtcmt_dictionary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_sundtcmt_dictionary.py` | 0 |
| META-PROC-00303 | gold | daily |  |  | destimator.dim_rsmeans_escalator | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_rsmeans_escalator.py` | 0 |
| META-PROC-00304 | gold | daily |  |  | destimator.fact_estimate_general | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_general.py` | 0 |
| META-PROC-00305 | gold | daily |  |  | destimator.fact_estimate_hmf | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_hmf.py` | 0 |
| META-PROC-00306 | gold | daily |  |  | destimator.fact_estimate_office | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_office.py` | 0 |
| META-PROC-00307 | gold | daily |  |  | destimator.fact_estimate_parking | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_parking.py` | 0 |
| META-PROC-00308 | gold | daily |  |  | destimator.fact_estimate_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_project.py` | 0 |
| META-PROC-00309 | gold | daily |  |  | destimator.fact_estimate_renovation | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_renovation.py` | 0 |
| META-PROC-00310 | gold | daily |  |  | destimator.fact_estimate_sm | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_sm.py` | 0 |
| META-PROC-00311 | gold | daily |  |  | cmt.destimator_enrbuildingcostindex | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_enr_buildingcost_index.py` | 0 |
| META-PROC-00312 | gold | daily |  |  | cmt.destimator_estimatedatadetails_general | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_general.py` | 0 |
| META-PROC-00313 | gold | daily |  |  | cmt.destimator_estimatedatadetails_hmf | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_hmf.py` | 0 |
| META-PROC-00314 | gold | daily |  |  | cmt.destimator_estimatedatadetails_office | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_office.py` | 0 |
| META-PROC-00315 | gold | daily |  |  | cmt.destimator_estimatedatadetails_parking | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_parking.py` | 0 |
| META-PROC-00316 | gold | daily |  |  | cmt.destimator_estimatedatadetails_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_project.py` | 0 |
| META-PROC-00317 | gold | daily |  |  | cmt.destimator_estimatedatadetails_renovation | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_renovation.py` | 0 |
| META-PROC-00318 | gold | daily |  |  | cmt.destimator_estimatedatadetails_sm | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_sm.py` | 0 |
| META-PROC-00319 | gold | daily |  |  | operation_financials.fact_accounts_payable | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_accounts_payable.py` | 0 |
| META-PROC-00320 | gold | daily |  |  | cmt.destimator_estimatefeedatadetails | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimate_fee_details.py` | 0 |
| META-PROC-00321 | gold | daily |  |  | cmt.destimator_estimatesummarydatadetails | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_summarydatadetails.py` | 0 |
| META-PROC-00322 | gold | daily |  |  | cmt.destimator_historicalcostdata | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_historicalcostdata.py` | 0 |
| META-PROC-00323 | gold | daily |  |  | cmt.destimator_rsmeansescalator | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_rsmeans_escalator.py` | 0 |
| META-PROC-00324 | gold | daily |  |  | cmt.destimator_sundtcmt_st_dictionary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_st_dictionary.py` | 0 |
| META-PROC-00325 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Notes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00326 | gold | daily |  |  | cosential.dim_construction_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_construction_type.py` | 0 |
| META-PROC-00327 | gold | daily |  |  | cosential.dim_cosential_company | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_company.py` | 0 |
| META-PROC-00328 | gold | daily |  |  | cosential.dim_cosential_contact | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_contact.py` | 0 |
| META-PROC-00329 | gold | daily |  |  | cosential.dim_cosential_project_opportunity_hierarchy | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_project_opportunity_hierarchy.py` | 0 |
| META-PROC-00330 | gold | daily |  |  | cosential.dim_office | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_office.py` | 0 |
| META-PROC-00331 | gold | daily |  |  | cosential.dim_opportunity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity.py` | 0 |
| META-PROC-00332 | gold | daily |  |  | cosential.dim_opportunity_staff | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity_staff.py` | 0 |
| META-PROC-00333 | gold | daily |  |  | cosential.dim_personnel | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_personnel.py` | 0 |
| META-PROC-00334 | gold | daily |  |  | cosential.dim_project_awards | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_awards.py` | 0 |
| META-PROC-00335 | gold | daily |  |  | cosential.dim_project_certifications | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_certifications.py` | 0 |
| META-PROC-00336 | gold | daily |  |  | cosential.dim_project_fees_contract | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_fees_contract.py` | 0 |
| META-PROC-00337 | gold | daily |  |  | cosential.dim_project_joint_venture | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_joint_venture.py` | 0 |
| META-PROC-00338 | gold | daily |  |  | cosential.dim_project_joint_venture_other | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_joint_venture_other.py` | 0 |
| META-PROC-00339 | gold | daily |  |  | cosential.dim_project_market | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_market.py` | 0 |
| META-PROC-00340 | gold | daily |  |  | cosential.dim_project_reference | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_reference.py` | 0 |
| META-PROC-00341 | gold | daily |  |  | cosential.dim_project_staff | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_staff.py` | 0 |
| META-PROC-00342 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsTemplateSection | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00343 | gold | daily |  |  | cosential.dim_project_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_type.py` | 0 |
| META-PROC-00344 | gold | daily |  |  | cosential.dim_studio | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_studio.py` | 0 |
| META-PROC-00345 | gold | daily |  |  | cosential.dim_subproject | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_subproject.py` | 0 |
| META-PROC-00346 | gold | daily |  |  | cosential.dim_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_type.py` | 0 |
| META-PROC-00347 | gold | daily |  |  | cosential.fact_opportunity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_opportunity.py` | 0 |
| META-PROC-00348 | gold | daily |  |  | cosential.fact_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_project.py` | 0 |
| META-PROC-00349 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsResponseTypeElementText | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00350 | silver | daily | p6 | Sharepoint List | silver_p6.P6ProjectMapping | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00351 | gold | daily |  |  | cosential.fact_opportunity_notes | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_opportunity_notes.py` | 0 |
| META-PROC-00352 | gold | daily |  |  | project_management.dim_change_order | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_change_order.py` | 0 |
| META-PROC-00353 | gold | daily |  |  | project_mgmt_core.fact_project_details | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_fact_project_details.py` | 0 |
| META-PROC-00354 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceUserRole | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00355 | silver | daily | p6 | SQL Server | silver_p6.PHASE | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00356 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleUserDefinedFieldDataType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00357 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00358 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResourceCurve | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00359 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResourceCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00360 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResource | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00361 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleRegisterEventValueCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00362 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleRegisterEventProbability | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00363 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleRegisterEventDuration | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00364 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleRegisterEventCost | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00365 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleLogicLinkType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00366 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleLogicLink | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00367 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleCalendarException | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00368 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleCalendar | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00369 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00370 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityResource | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00371 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityPercentCompleteType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00372 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityConstraintType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00373 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivity | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00374 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleSchedule | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00375 | silver | daily | cosential | SQL Server | silver_cosential.Document_AssocProject | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00376 | silver | daily | cosential | SQL Server | silver_cosential.Document | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00377 | silver | daily | security | Sharepoint List | silver_security.E1_Project_Overrides_RLS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00378 | silver | daily | security | Sharepoint List | silver_security.Cosential_Projects_RLS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00379 | silver | daily | security | Sharepoint List | silver_security.Cosential_Opportunity_RLS | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00380 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProjectDetailAttribute | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00381 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPCOSummary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00382 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPackage | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00383 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsResponseTypeElement | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00384 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsResponseType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00385 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsQuestionText | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00386 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsQuestionReportingTag | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00387 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsQuestion | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00388 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsGeneralHeaderData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00389 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCompletionsEventTaskData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00390 | silver | daily | e1 | SQL Server | silver_e1.F1307 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00391 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlForecastNotes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00392 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCurrentProjectForecastDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00393 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCurrentEstimateExtended | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00394 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCurrentBudget | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00395 | gold | daily |  |  | operation_financials_v.fact_project_billing_current_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_fact_project_billing_current_v.py` | 0 |
| META-PROC-00396 | gold | daily |  |  | operation_financials_v.fact_project_cash_position_current_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_fact_project_cash_position_current_v.py` | 0 |
| META-PROC-00397 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCostItemDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00398 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCostItemCharacteristicTypeList | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00399 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCostItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00400 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCostCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00401 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCorporateForecastRemainingDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00402 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCorporateForecastDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00403 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCorporateForecast | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00404 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCommittedCostSummary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00405 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlChangeOrder | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00406 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlActualsVendorHours | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00407 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlActualsQuantity | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00408 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlActualsManhours | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00409 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlActualsCost | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00410 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreUnitOfMeasure | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00411 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreAccountCode | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00412 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCurrentProjectForecastRemainingDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00413 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCurrentEstimate | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00414 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCostItemAttributes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00415 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlChangeOrderPayItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00417 | silver | daily | heavyjob | File System | silver_heavyjob.SCRDR_Equip | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00418 | gold | daily |  |  | project_management.dim_change_order_description | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_change_order_description.py` | 0 |
| META-PROC-00419 | gold | daily |  |  | project_management.dim_cost_category | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_category.py` | 0 |
| META-PROC-00420 | gold | daily |  |  | project_management.dim_cost_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_item.py` | 0 |
| META-PROC-00421 | gold | daily |  |  | project_management.dim_cost_item_characteristic_type_list | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_item_characteristic_type_list.py` | 0 |
| META-PROC-00422 | gold | daily |  |  | project_management.dim_forecast_method | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forecast_method.py` | 0 |
| META-PROC-00423 | gold | daily |  |  | project_management.dim_forecast_notes | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forcast_notes.py` | 0 |
| META-PROC-00424 | gold | daily |  |  | project_management.dim_forecast_snapshot | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forecast_snapshot.py` | 0 |
| META-PROC-00425 | gold | daily |  |  | project_management.dim_pay_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_pay_item.py` | 0 |
| META-PROC-00426 | gold | daily |  |  | project_management.dim_unit_of_measure | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_unit_of_measure.py` | 0 |
| META-PROC-00427 | gold | daily |  |  | project_management.fact_actuals | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_actuals.py` | 0 |
| META-PROC-00428 | gold | daily |  |  | project_management.fact_change_order_pay_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_pay_item.py` | 0 |
| META-PROC-00429 | gold | daily |  |  | project_management.fact_committed_cost_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_committed_cost_summary.py` | 0 |
| META-PROC-00430 | gold | daily |  |  | project_management.fact_control_budget | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_control_budget.py` | 0 |
| META-PROC-00431 | gold | daily |  |  | project_management.fact_current_project_forecast | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_project_forecast.py` | 0 |
| META-PROC-00432 | gold | daily |  |  | project_management.fact_estimates | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_estimates.py` | 0 |
| META-PROC-00433 | gold | daily |  |  | project_management.fact_forecast | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_forcast.py` | 0 |
| META-PROC-00434 | gold | daily |  |  | project_management.fact_pay_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_pay_item.py` | 0 |
| META-PROC-00435 | gold | daily |  |  | project_management.fact_pay_item_earning | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_pay_item_earning.py` | 0 |
| META-PROC-00436 | gold | daily |  |  | project_mgmt_core.dim_acs | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_mgmt_core/silver_to_gold_dim_acs.py` | 0 |
| META-PROC-00437 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwIssueSummary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00438 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractPCODetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00439 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractCostItemPricingDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00440 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractCostItemPricingCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00441 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractCCODetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00442 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContract | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00443 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwChangeDocument | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00444 | silver | daily | e1 | SQL Server | silver_e1.F1301 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00445 | gold | daily |  |  | cosential.dim_project_documents | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_documents.py` | 0 |
| META-PROC-00446 | gold | daily |  |  | security.stg_user_cosential_opportunity_relationship | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cosential_opportunity_relationship.py` | 0 |
| META-PROC-00447 | gold | daily |  |  | security.stg_user_cosential_project_relationship | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cosential_project_relationship.py` | 0 |
| META-PROC-00448 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlBudget | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00449 | gold | daily |  |  | conformed.dim_project_org_hierarchy | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_project_org_hierarchy.py` | 0 |
| META-PROC-00450 | gold | daily |  |  | user_communication.data_warehouse_release_notes | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/user_communication/silver_to_gold_data_warehouse_release_notes.py` | 0 |
| META-PROC-00451 | gold | daily |  |  | operation_financials.missed_timecard_report | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_missed_time_card_v.py` | 0 |
| META-PROC-00452 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlPayItemExtended | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00453 | gold | daily |  |  | project_management.brdg_work_package_component | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_brdg_work_package_component.py` | 0 |
| META-PROC-00454 | gold | daily |  |  | project_management.brdg_work_package_cost_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_brdg_work_package_cost_item.py` | 0 |
| META-PROC-00455 | gold | daily |  |  | project_management.dim_claiming_scheme | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_claiming_scheme.py` | 0 |
| META-PROC-00456 | gold | daily |  |  | project_management.dim_claiming_scheme_step | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_claiming_scheme_step.py` | 0 |
| META-PROC-00457 | gold | daily |  |  | project_management.dim_commodity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_commodity.py` | 0 |
| META-PROC-00458 | gold | daily |  |  | project_management.dim_component | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_component.py` | 0 |
| META-PROC-00459 | gold | daily |  |  | project_management.dim_craft | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_craft.py` | 0 |
| META-PROC-00460 | gold | daily |  |  | project_management.dim_daily_plan | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_daily_plan.py` | 0 |
| META-PROC-00461 | gold | daily |  |  | project_management.dim_discipline | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_discipline.py` | 0 |
| META-PROC-00462 | gold | daily |  |  | project_management.dim_time_card | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_time_card.py` | 0 |
| META-PROC-00463 | gold | daily |  |  | project_management.dim_trade | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_trade.py` | 0 |
| META-PROC-00464 | gold | daily |  |  | project_management.dim_union | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_union.py` | 0 |
| META-PROC-00465 | gold | daily |  |  | project_management.dim_user | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_user.py` | 0 |
| META-PROC-00466 | gold | daily |  |  | project_management.dim_work_package | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_work_package.py` | 0 |
| META-PROC-00467 | gold | daily |  |  | project_management.fact_daily_plan_notes | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_daily_plan_notes.py` | 0 |
| META-PROC-00468 | gold | daily |  |  | proforma.fact_proforma | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/proforma/silver_to_gold_fact_proforma.py` | 0 |
| META-PROC-00469 | gold | daily |  |  | operation_financials.fact_executive_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_proforma_executive_summary.py` | 0 |
| META-PROC-00472 | gold | daily |  |  | operation_financials_v.dim_account_master_lvl7_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_dim_account_master_lvl7_v.py` | 0 |
| META-PROC-00474 | gold | daily |  |  | schedule_v.fact_average_daily_labor_by_date_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_average_daily_labor_by_date.py` | 0 |
| META-PROC-00475 | gold | daily |  |  | schedule_v.fact_average_daily_labor_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_average_daily_labor.py` | 0 |
| META-PROC-00476 | gold | daily |  |  | schedule_v.fact_task_current_max_week_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_task_current_max_week.py` | 0 |
| META-PROC-00477 | gold | daily |  |  | equipment.fact_equipment_status_history | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_status_history.py` | 0 |
| META-PROC-00478 | gold | daily |  |  | operation_financials.fact_account_balance_monthly_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance_monthly_detail.py` | 0 |
| META-PROC-00479 | gold | daily |  |  | operation_financials.fact_account_balance_monthly_header | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance_monthly_header.py` | 0 |
| META-PROC-00480 | silver | daily | powerbi | REST API | silver_powerbi.activityevents | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00483 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwDailyPlanSummary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00484 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwDailyPlanQuantity | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00485 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwDailyPlanNote | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00486 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreUnion | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00487 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreTrade | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00488 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProjectEquipment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00489 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProjectEmployee | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00490 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreDiscipline | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00491 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreCraft | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00492 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreCommodity | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00493 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanWorkPackageComponent | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00494 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanWorkPackage | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00495 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanWBSClaimingSchemeAssociation | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00496 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanTimeCardNotes | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00497 | gold | daily |  |  | equipment.fact_equipment | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment.py` | 0 |
| META-PROC-00498 | gold | daily |  |  | equipment.fact_equipment_gl_trans | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_gl_trans.py` | 0 |
| META-PROC-00499 | gold | daily |  |  | equipment_v.dim_account_master_all_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_dim_account_master_all_v.py` | 0 |
| META-PROC-00500 | gold | daily |  |  | equipment_v.dim_project_bu_all_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_dim_project_bu_all_v.py` | 0 |
| META-PROC-00501 | gold | daily |  |  | equipment_v.fact_equipment_rental_in_service_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_equipment_rental_in_service_v.py` | 0 |
| META-PROC-00502 | gold | daily |  |  | operation_financials.dim_document_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_document_type.py` | 0 |
| META-PROC-00503 | gold | daily |  |  | operation_financials.dim_ledger_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_ledger_type.py` | 0 |
| META-PROC-00504 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanQuantityClaimDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00505 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanQuantityClaim | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00506 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanProjectComponentPartialView | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00507 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanDiscipline | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00510 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanComponentCharacteristic | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00511 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanComponent | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00512 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanClaimingSchemeStep | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00513 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanClaimingScheme | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00514 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanAccountCodeClaimingSchemeAssociation | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00515 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanWorkPlanCostItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00516 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanTimeCards | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00518 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwAdvancedWorkPackaging | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00519 | gold | daily |  |  | project_management.fact_daily_plan_quantity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_daily_plan_quantity.py` | 0 |
| META-PROC-00520 | gold | daily |  |  | project_management.fact_quantity_claim | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_quantity_claim.py` | 0 |
| META-PROC-00521 | gold | daily |  |  | project_management.fact_time_card | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_time_card.py` | 0 |
| META-PROC-00522 | gold | daily |  |  | project_management.fact_work_package | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_work_package.py` | 0 |
| META-PROC-00523 | gold | daily |  |  | project_management.fact_wp_component_progress | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_wp_component_progress.py` | 0 |
| META-PROC-00524 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreDocumentApplicationIntegration | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00525 | silver | daily | webapp | Azure SQL Database - SDAT Web App | silver_webapp.Audits | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00526 | silver | daily | b2g | SOAP API | silver_b2g.vendor | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00527 | silver | daily | cslb | API | silver_cslb.license_data | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00528 | silver | daily | b2g | SOAP API | silver_b2g.contract_vendor | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00529 | silver | daily | b2g | SOAP API | silver_b2g.contract | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00530 | silver | daily | b2g | Sharepoint List | silver_b2g.B2G_XBE_Subcontractor_Commitments | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00531 | gold | daily |  |  | prolog.fact_potential_changeorder_line_items | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_potential_changeorder_lineitems.py` | 0 |
| META-PROC-00532 | gold | daily |  |  | prolog.fact_projects_with_assigned_roles | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_projects_assigned_roles.py` | 0 |
| META-PROC-00533 | gold | daily |  |  | prolog.fact_request_for_information | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_request_for_information.py` | 0 |
| META-PROC-00534 | gold | daily |  |  | prolog.fact_safety | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_safety.py` | 0 |
| META-PROC-00535 | gold | daily |  |  | prolog.fact_sub_contract_change_order | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_sub_contract_changeorder.py` | 0 |
| META-PROC-00536 | gold | daily |  |  | prolog.fact_submittal_reviewers | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_submittal_reviewers.py` | 0 |
| META-PROC-00537 | gold | daily |  |  | prolog.fact_submittals | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_submittals.py` | 0 |
| META-PROC-00538 | gold | daily |  |  | mpr.data_import_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_data_import_log.py` | 0 |
| META-PROC-00539 | gold | daily |  |  | mpr.stg_account_balances | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_account_balances.py` | 0 |
| META-PROC-00540 | gold | daily |  |  | mpr.stg_account_master | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_account_master.py` | 0 |
| META-PROC-00541 | gold | daily |  |  | mpr.stg_billing_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_billing_summary.py` | 0 |
| META-PROC-00542 | gold | daily |  |  | mpr.stg_contracts | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_contracts.py` | 0 |
| META-PROC-00543 | gold | daily |  |  | mpr.stg_employee_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_employee_project.py` | 0 |
| META-PROC-00544 | gold | daily |  |  | security.ref_user_project_role | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_ref_user_project_role.py` | 0 |
| META-PROC-00545 | gold | daily |  |  | web_app_integration.project_notes_export | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_project_notes_export.py` | 0 |
| META-PROC-00546 | gold | daily |  |  | mpr.stg_active_projects | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_active_projects.py` | 0 |
| META-PROC-00547 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreContact | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00548 | silver | daily | e1 | SQL Server | silver_e1.F1302 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00549 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractContractCustomField | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00550 | silver | daily | security | Sharepoint List | silver_security.Ga_Overrides_Group_District | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00551 | silver | daily | security | Sharepoint List | silver_security.Ga_Overrides_Group_District | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00552 | silver | daily | security | Sharepoint List | silver_security.Job_Roles_GA | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00553 | silver | daily | emars | SQL Server | silver_emars.Stg_Emars_Payroll | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00554 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwDiversityCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00555 | silver | daily | ineight_document | SQL Server | silver_ineight_document.vw_FormSections_Parsed | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00556 | silver | daily | ineight_document | SQL Server | silver_ineight_document.FormSections | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00557 | silver | daily | ineight_document | SQL Server | silver_ineight_document.Forms | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00558 | silver | daily | ineight_document | SQL Server | silver_ineight_document.Contact | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00559 | gold | daily |  |  | ineight_document.dim_form | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_dim_form.py` | 0 |
| META-PROC-00560 | gold | daily |  |  | ineight_document.fact_rfi | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_rfi.py` | 0 |
| META-PROC-00561 | gold | daily |  |  | ineight_document.fact_submittals | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittals.py` | 0 |
| META-PROC-00562 | gold | daily |  |  | cosential_v.fact_opportunity_current_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_vw_fact_opportunity_current.py` | 0 |
| META-PROC-00563 | silver | daily | zipcodes | SFTP File | silver_zipcodes.Zipcode_Update_Standard | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00564 | gold | daily |  |  | safety.dim_org_project_bu | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_org_project_bu.py` | 0 |
| META-PROC-00565 | gold | daily |  |  | safety_v.dim_org_project_bu_safety_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_dim_org_project_bu_safety.py` | 0 |
| META-PROC-00566 | gold | daily |  |  | project_management.fact_current_plan_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_plan_detail.py` | 0 |
| META-PROC-00567 | gold | daily |  |  | project_management.fact_current_plan_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_plan_summary.py` | 0 |
| META-PROC-00568 | gold | daily |  |  | project_management_v.fact_current_plan_actuals_detail_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_plan_actuals_detail_v.py` | 0 |
| META-PROC-00569 | gold | daily |  |  | project_management_v.fact_current_plan_actuals_summary_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_plan_actuals_summary_v.py` | 0 |
| META-PROC-00570 | gold | daily |  |  | project_management_v.fact_current_project_forecast_detail_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_project_forecast_detail_v.py` | 0 |
| META-PROC-00571 | gold | daily |  |  | operation_financials.scanman_workbench | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_scanman_workbench_v.py` | 0 |
| META-PROC-00572 | gold | daily |  |  | operation_financials.statement_of_operations_report_aa | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_statement_of_operations_v.py` | 0 |
| META-PROC-00573 | gold | daily |  |  | operation_financials.statement_of_operations_report_ba | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_statement_of_operations_ba_v.py` | 0 |
| META-PROC-00574 | silver | daily | e1 | SQL Server | silver_e1.FFZPS30T | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00575 | silver | daily | e1 | SQL Server | silver_e1.FFZPS302 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00576 | silver | daily | e1 | SQL Server | silver_e1.FFZPS300 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00577 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwComplianceTemplateData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00578 | silver | daily | ineight | Azure SQL Database | silver_ineight.qry_complianceobsoleteuseremail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00579 | silver | daily | safety | Sharepoint List | silver_safety.Safety_STCKY_Buckets | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00580 | silver | daily | safety | Sharepoint List | silver_safety.Safety_InjuryCauseHierarchy | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00581 | silver | daily | e1 | SQL Server | silver_e1.F0092 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00582 | silver | conformed-001 | e1 | SQL Server | silver_e1.F5144 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00583 | silver | conformed-001 | e1 | SQL Server | silver_e1.F060116 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00584 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0401 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00585 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0150 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00586 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0116 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00587 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0115 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00588 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0111 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00589 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0101 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00590 | gold | daily |  |  | equipment.dim_equipment_rate_group | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_rate_group.py` | 0 |
| META-PROC-00591 | gold | daily |  |  | equipment.dim_equipment_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_status.py` | 0 |
| META-PROC-00592 | gold | daily |  |  | equipment.fact_equipment_site_rate_integration_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_site_rate_integration_log.py` | 0 |
| META-PROC-00593 | gold | daily |  |  | equipment_secured_v.fact_equipment_site_rates_ineight_current_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_equipment_site_rates_ineight_current_v.py` | 0 |
| META-PROC-00594 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreProjectUserRole | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00596 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreEmployee | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00597 | gold | daily |  |  | cosential.dim_cosential_states | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_states.py` | 0 |
| META-PROC-00598 | gold | daily |  |  | cosential.dim_project_consultants | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_consultants.py` | 0 |
| META-PROC-00599 | gold | daily |  |  | cosential.dim_project_consultants_contacts | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_consultants_contacts.py` | 0 |
| META-PROC-00600 | gold | daily |  |  | cosential.dim_project_descriptions | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_descriptions.py` | 0 |
| META-PROC-00601 | gold | daily |  |  | cosential.dim_project_owner_client | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_owner_client.py` | 0 |
| META-PROC-00602 | gold | daily |  |  | cosential.dim_project_owner_client_contacts | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_owner_client_contacts.py` | 0 |
| META-PROC-00603 | gold | daily |  |  | cosential.dim_service_types | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_service_types.py` | 0 |
| META-PROC-00604 | gold | daily |  |  | cosential.dim_project_reference_testimonials | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_reference_testimonials.py` | 0 |
| META-PROC-00605 | gold | daily |  |  | safety.dim_ineight_role | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_role.py` | 0 |
| META-PROC-00606 | gold | daily |  |  | safety_v.fact_labor_hours_by_project_monthly_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_labor_hours_by_project_monthly.py` | 0 |
| META-PROC-00607 | gold | daily |  |  | safety_v.fact_subcontractor_labor_hours_by_project_monthly_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_subcontractor_labor_hours_by_project_monthly.py` | 0 |
| META-PROC-00608 | gold | daily |  |  | compliance.bridge_vendor_eval_evaluator | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_bridge_vendor_eval_evaluator.py` | 0 |
| META-PROC-00609 | gold | daily |  |  | compliance.bridge_vendor_eval_work_package | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_bridge_vendor_eval_work_package.py` | 0 |
| META-PROC-00610 | gold | daily |  |  | compliance.dim_project_phase | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_project_phase.py` | 0 |
| META-PROC-00611 | gold | daily |  |  | compliance.dim_vendor_evaluation_form | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_vendor_evaluation_form.py` | 0 |
| META-PROC-00612 | gold | daily |  |  | compliance.dim_work_package_trade | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_work_package_trade.py` | 0 |
| META-PROC-00613 | gold | daily |  |  | compliance.fact_vendor_evaluation | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_fact_vendor_evaluation.py` | 0 |
| META-PROC-00614 | gold | daily |  |  | equipment.dim_maint_schedule_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_maint_schedule_type.py` | 0 |
| META-PROC-00615 | gold | daily |  |  | equipment.dim_responsible_party | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_responsible_party.py` | 0 |
| META-PROC-00616 | gold | daily |  |  | equipment.dim_work_order | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order.py` | 0 |
| META-PROC-00617 | gold | daily |  |  | mpr.stg_contract_summary | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_contract_summary.py` | 0 |
| META-PROC-00618 | gold | daily |  |  | mpr.stg_cors_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_cors_detail.py` | 0 |
| META-PROC-00619 | gold | daily |  |  | mpr.stg_pcco_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_pcco_details.py` | 0 |
| META-PROC-00620 | gold | daily |  |  | safety.dim_compliance_user | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_compliance_user.py` | 0 |
| META-PROC-00621 | gold | daily |  |  | safety.dim_injury_cause_hierarchy | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_injury_cause_hierarchy.py` | 0 |
| META-PROC-00622 | gold | daily |  |  | safety_v.fact_cvis_recognition_action_area_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_recognition_action_area.py` | 0 |
| META-PROC-00623 | gold | daily |  |  | safety_v.fact_cvis_recognition_award_type_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_recognition_award_type.py` | 0 |
| META-PROC-00624 | gold | daily |  |  | safety_v.fact_cvis_walk_corr_action_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_walk_corr_action.py` | 0 |
| META-PROC-00625 | gold | daily |  |  | safety_v.fact_cvis_walk_protection_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_walk_protection.py` | 0 |
| META-PROC-00626 | gold | daily |  |  | safety_v.fact_incident_body_part_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_body_part.py` | 0 |
| META-PROC-00627 | gold | daily |  |  | safety_v.fact_incident_equip_category_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_category.py` | 0 |
| META-PROC-00628 | gold | daily |  |  | safety_v.fact_incident_equip_crane_damage_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_damage.py` | 0 |
| META-PROC-00629 | gold | daily |  |  | safety_v.fact_incident_equip_crane_estimated_loss_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_estimated_loss.py` | 0 |
| META-PROC-00630 | gold | daily |  |  | safety_v.fact_incident_equip_crane_owner_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_owner.py` | 0 |
| META-PROC-00631 | gold | daily |  |  | safety_v.fact_incident_event_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_event.py` | 0 |
| META-PROC-00632 | gold | daily |  |  | safety_v.fact_incident_first_aid_provider_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_first_aid_provider.py` | 0 |
| META-PROC-00633 | gold | daily |  |  | safety_v.fact_incident_injury_classification_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_classification.py` | 0 |
| META-PROC-00634 | gold | daily |  |  | safety_v.fact_incident_injury_main_cause_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_main_cause.py` | 0 |
| META-PROC-00635 | gold | daily |  |  | safety_v.fact_incident_injury_type_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_type.py` | 0 |
| META-PROC-00636 | gold | daily |  |  | safety_v.fact_incident_medical_treatment_provider_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_medical_treatment_provider.py` | 0 |
| META-PROC-00637 | gold | daily |  |  | safety_v.fact_incident_medical_treatment_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_medical_treatment.py` | 0 |
| META-PROC-00638 | gold | daily |  |  | safety_v.fact_incident_utility_info_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_utility_info.py` | 0 |
| META-PROC-00639 | gold | daily |  |  | safety_v.fact_incident_utility_pivots_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_utility_pivots.py` | 0 |
| META-PROC-00640 | gold | daily |  |  | safety.dim_safety_form | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_safety_form.py` | 0 |
| META-PROC-00641 | gold | daily |  |  | safety.dim_stcky_bucket | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_stcky_bucket.py` | 0 |
| META-PROC-00642 | gold | daily |  |  | safety.dim_stcky_role | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_stcky_role.py` | 0 |
| META-PROC-00643 | gold | daily |  |  | safety.fact_cvis_recognition | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_recognition.py` | 0 |
| META-PROC-00644 | gold | daily |  |  | equipment.dim_maint_schedule_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_maint_schedule_status.py` | 0 |
| META-PROC-00645 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCCOSummary | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00646 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlChangeOrderDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00647 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlChangeOrderCost | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00648 | gold | daily |  |  | project_management.dim_cor | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cor.py` | 0 |
| META-PROC-00649 | gold | daily |  |  | project_management.dim_issue | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_issue.py` | 0 |
| META-PROC-00650 | gold | daily |  |  | project_management.fact_budget_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_budget_log.py` | 0 |
| META-PROC-00651 | gold | daily |  |  | project_management.fact_cco_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_cco_log.py` | 0 |
| META-PROC-00652 | gold | daily |  |  | project_management.fact_change_order_cost | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_cost.py` | 0 |
| META-PROC-00653 | gold | daily |  |  | project_management.fact_change_order_detail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_detail.py` | 0 |
| META-PROC-00654 | gold | daily |  |  | project_management.fact_cor_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_cor_log.py` | 0 |
| META-PROC-00655 | gold | daily |  |  | project_management.dim_cco | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cco.py` | 0 |
| META-PROC-00656 | gold | daily |  |  | project_management.fact_issues_log | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_issues_log.py` | 0 |
| META-PROC-00657 | gold | daily |  |  | project_management.sat_current_budget_cost_item_category | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_sat_current_budget_cost_item_category.py` | 0 |
| META-PROC-00658 | gold | daily |  |  | project_management.sat_orignial_budget_cost_item_category | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_sat_original_budget_cost_item_category.py` | 0 |
| META-PROC-00659 | gold | daily |  |  | b2g.dim_vendor | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_vendor.py` | 0 |
| META-PROC-00660 | gold | daily |  |  | b2g.dim_xbe | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_xbe.py` | 0 |
| META-PROC-00661 | gold | daily |  |  | b2g.dim_xbe_subcontractor_commitments | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_xbe_subcontractor_commitments.py` | 0 |
| META-PROC-00662 | gold | daily |  |  | b2g.fact_contract_payment_xbe | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_fact_contract_payment_xbe.py` | 0 |
| META-PROC-00663 | gold | daily |  |  | b2g.fact_vendor_payment_xbe | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_fact_vendor_payment_xbe.py` | 0 |
| META-PROC-00664 | gold | daily |  |  | equipment.fact_equipment_utilization | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_utilization.py` | 0 |
| META-PROC-00665 | gold | daily |  |  | equipment.dim_work_order_ownership | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_ownership.py` | 0 |
| META-PROC-00666 | gold | daily |  |  | equipment.dim_work_order_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_status.py` | 0 |
| META-PROC-00667 | gold | daily |  |  | equipment.dim_work_order_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_type.py` | 0 |
| META-PROC-00668 | gold | daily |  |  | equipment.bridge_work_order_gl_trans | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_bridge_work_order_gl_trans.py` | 0 |
| META-PROC-00669 | gold | daily |  |  | equipment_v.fact_work_order_gl_trans_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_work_order_gl_trans_v.py` | 0 |
| META-PROC-00670 | gold | daily |  |  | equipment.fact_maint_schedule | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py` | 0 |
| META-PROC-00671 | gold | daily |  |  | equipment.fact_work_order | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_work_order.py` | 0 |
| META-PROC-00672 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreOrganization | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00673 | gold | daily |  |  | conformed.dim_zipcode | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_zipcodes.py` | 0 |
| META-PROC-00674 | gold | daily |  |  | emars.dim_contractor | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_contractor.py` | 0 |
| META-PROC-00675 | gold | daily |  |  | emars.dim_ethnicity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_ethnicity.py` | 0 |
| META-PROC-00676 | gold | daily |  |  | emars.dim_project_emars | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_project_emars.py` | 0 |
| META-PROC-00677 | gold | daily |  |  | emars.dim_work_class | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_work_class.py` | 0 |
| META-PROC-00678 | gold | daily |  |  | emars_sensitive.dim_employee_emars | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_employee_emars.py` | 0 |
| META-PROC-00679 | gold | daily |  |  | emars_sensitive.fact_payroll | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_fact_payroll.py` | 0 |
| META-PROC-00680 | gold | daily |  |  | emars_v.fact_payroll_hours_nonsensitive_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_payroll_hours_nonsensitive_v.py` | 0 |
| META-PROC-00681 | gold | daily |  |  | emars_v.fact_workforce_summary_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_v.py` | 0 |
| META-PROC-00682 | gold | daily |  |  | emars_v.fact_workforce_summary_work_class_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_work_class_v.py` | 0 |
| META-PROC-00683 | gold | daily |  |  | emars_v.fact_workforce_summary_worker_zip_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_worker_zip_v.py` | 0 |
| META-PROC-00684 | gold | daily |  |  | b2g.fact_vendor_performance_xbe | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_vw_fact_vendor_performance_xbe.py` | 0 |
| META-PROC-00685 | silver | daily | e1 | SQL Server | silver_e1.F4801T | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00686 | silver | daily | equipment | Sharepoint List | silver_equipment.Work_Orders_Responsible_Party | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00688 | gold | daily |  |  | cosential.dim_opportunity_consultants | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity_consultants.py` | 0 |
| META-PROC-00689 | silver | daily | e1 | SQL Server | silver_e1.FFZPS201 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00690 | silver | daily | vairkko | REST API | silver_vairkko.users | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00691 | silver | daily | vairkko | REST API | silver_vairkko.templates | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00692 | silver | daily | vrm | File System | silver_vrm.driver_compliance | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00693 | silver | daily | nccer | REST API | silver_nccer.credentials | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00694 | silver | daily | vairkko | REST API | silver_vairkko.certifications | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00695 | gold | daily |  |  | bridgit.bridgit_project | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgit_project.py` | 0 |
| META-PROC-00696 | gold | daily |  |  | bridgit.nccer_credentials | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_nccer_credentials.py` | 0 |
| META-PROC-00697 | gold | daily |  |  | bridgit.vairkko_certifications | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vairkko_certifications.py` | 0 |
| META-PROC-00698 | gold | daily |  |  | bridgit.vairkko_templates | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vairkko_templates.py` | 0 |
| META-PROC-00699 | gold | daily |  |  | bridgit.vrm_driver_compliance | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vrm_driver_compliance.py` | 0 |
| META-PROC-00700 | gold | daily |  |  | project_management.bridge_bid_package_cost_item | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_bridge_bid_package_cost_item.py` | 0 |
| META-PROC-00701 | gold | daily |  |  | project_management.bridge_contract_closeout_user | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_bridge_contract_closeout_user.py` | 0 |
| META-PROC-00707 | gold | daily |  |  | ineight_document_report.dim_document_rfi_report | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_dim_document_rfi_report.py` | 0 |
| META-PROC-00708 | gold | daily |  |  | ineight_document_report.dim_document_submittal | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_dim_document_submittal.py` | 0 |
| META-PROC-00709 | gold | daily |  |  | ineight_document_report.fact_document | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_fact_document.py` | 0 |
| META-PROC-00710 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlCBSAuditLog | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00711 | gold | daily |  |  | project_management.dim_bid_package | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_bid_package.py` | 0 |
| META-PROC-00712 | gold | daily |  |  | project_management.dim_bid_package_milestone | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_bid_package_milestone.py` | 0 |
| META-PROC-00713 | gold | daily |  |  | project_management.dim_contract | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract.py` | 0 |
| META-PROC-00714 | gold | daily |  |  | project_management.dim_contract_closeout_status | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_closeout_status.py` | 0 |
| META-PROC-00715 | gold | daily |  |  | project_management.dim_contract_closeout_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_closeout_type.py` | 0 |
| META-PROC-00716 | gold | daily |  |  | project_management.dim_contract_detail_type | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_detail_type.py` | 0 |
| META-PROC-00717 | gold | daily |  |  | project_management.dim_contract_line | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_line.py` | 0 |
| META-PROC-00718 | gold | daily |  |  | project_management.dim_contract_responsibility | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_responsibility.py` | 0 |
| META-PROC-00719 | gold | daily |  |  | project_management.dim_contract_schedule_of_values | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_schedule_of_values.py` | 0 |
| META-PROC-00720 | gold | daily |  |  | project_management.dim_contract_type_hierarchy | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_type_hierarchy.py` | 0 |
| META-PROC-00721 | gold | daily |  |  | project_management.dim_contract_vco | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_vco.py` | 0 |
| META-PROC-00722 | gold | daily |  |  | project_management.dim_diversity_category | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_diversity_category.py` | 0 |
| META-PROC-00723 | gold | daily |  |  | project_management.dim_invoice | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_invoice.py` | 0 |
| META-PROC-00724 | gold | daily |  |  | project_management.dim_invoice_payment_method | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_invoice_payment_method.py` | 0 |
| META-PROC-00725 | gold | daily |  |  | project_management.dim_risk_mitigation_plan | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_risk_mitigation_plan.py` | 0 |
| META-PROC-00726 | gold | daily |  |  | project_management.fact_bid_package | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_bid_package.py` | 0 |
| META-PROC-00727 | gold | daily |  |  | project_management.fact_bid_package_milestone | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_bid_package_milestone.py` | 0 |
| META-PROC-00729 | gold | daily |  |  | web_app_integration.dim_pbi_report | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_dim_pbi_report.py` | 0 |
| META-PROC-00730 | gold | daily |  |  | web_app_integration.dim_pbi_workspace | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_dim_pbi_workspace.py` | 0 |
| META-PROC-00731 | gold | daily |  |  | web_app_integration.fact_pbi_user_activity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_fact_pbi_user_avtivity.py` | 0 |
| META-PROC-00732 | gold | daily |  |  | security.stg_user_cost_code_relationship | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cost_code_relationship.py` | 0 |
| META-PROC-00733 | gold | daily |  |  | conformed_v.dim_closed_project_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_vw_closed_project.py` | 0 |
| META-PROC-00734 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0010 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00735 | gold | daily |  |  | safety.fact_cvis_suggestion_box | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_suggestion_box.py` | 0 |
| META-PROC-00736 | gold | daily |  |  | safety.fact_cvis_walk | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_walk.py` | 0 |
| META-PROC-00737 | gold | daily |  |  | safety.fact_incident | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_incident.py` | 0 |
| META-PROC-00738 | gold | daily |  |  | safety.fact_psli | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_psli.py` | 0 |
| META-PROC-00739 | gold | daily |  |  | safety.fact_safety_event_task | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_safety_event_task.py` | 0 |
| META-PROC-00740 | gold | daily |  |  | safety.fact_stcky_walk | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_stcky_walk.py` | 0 |
| META-PROC-00741 | gold | daily |  |  | safety.fact_stcky_walk_missing_protection_reason | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_stcky_walk_missing_protection_reason.py` | 0 |
| META-PROC-00742 | gold | daily |  |  | safety_v.fact_psli_event_task_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_psli_event_task.py` | 0 |
| META-PROC-00743 | gold | daily |  |  | safety_v.fact_stcky_walk_corr_action_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_walk_corr_action.py` | 0 |
| META-PROC-00744 | gold | daily |  |  | safety_v.fact_stcky_walk_protection_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_walk_protection.py` | 0 |
| META-PROC-00745 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0006 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 1 |
| META-PROC-00746 | silver | conformed-001 | e1 | SQL Server | silver_e1.F0005 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00747 | silver | conformed-001 | cosential | SQL Server | silver_cosential.States | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00748 | silver | conformed-001 | p6 | SQL Server | silver_p6.PROJECT | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00749 | silver | conformed-001 | cosential | SQL Server | silver_cosential.Opportunity_DeliveryMethod | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00750 | silver | daily | cosential | SQL Server | silver_cosential.Opportunity_Consultants | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00751 | silver | conformed-001 | cosential_api | REST API | silver_cosential_api.opportunities | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00752 | silver | conformed-001 | cosential | SQL Server | silver_cosential.FirmOrg_OfficeDivision | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00753 | silver | conformed-001 | cosential | SQL Server | silver_cosential.FirmOrg_Divisions | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00754 | silver | conformed-001 | p6 | Sharepoint List | silver_p6.P6ProjectMapping | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00755 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreCostCategory | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00756 | gold | daily |  |  | project_management.fact_actuals_lod_9 | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_actuals_lod_9.py` | 0 |
| META-PROC-00757 | gold | daily |  |  | project_management.fact_contract_cost_item_pricing | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_cost_item_pricing.py` | 0 |
| META-PROC-00758 | gold | daily |  |  | cslb.license_data | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/cslb/silver_to_gold_license_data.py` | 0 |
| META-PROC-00759 | silver | daily | ineight_estimate | SQL Server | silver_ineight_estimate.CostSegments | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00760 | silver | daily | ineight_estimate | SQL Server | silver_ineight_estimate.CostItemsReferencedData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00761 | silver | daily | ineight_estimate | SQL Server | silver_ineight_estimate.CostItemsCalculatedValues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00762 | silver | daily | ineight_estimate | SQL Server | silver_ineight_estimate.CostItems | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00763 | silver | daily | ineight_estimate | SQL Server | silver_ineight_estimate.AccountCostItemUtilizationsReferencedData | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00764 | silver | daily | procore | REST API | silver_procore.submittals | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00765 | silver | daily | procore | REST API | silver_procore.rfis | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00766 | silver | daily | textura | REST API | silver_textura.users | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00769 | silver | daily | textura | REST API | silver_textura.suppliertrackingselectedvalues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00770 | silver | daily | textura | REST API | silver_textura.suppliertrackingprogramvalues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00771 | silver | daily | textura | REST API | silver_textura.suppliertrackingprograms | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00772 | silver | daily | textura | REST API | silver_textura.suppliertrackingcontractorvalues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00773 | silver | daily | textura | REST API | silver_textura.projectuserroles | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00774 | silver | daily | textura | REST API | silver_textura.projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00775 | silver | daily | textura | REST API | silver_textura.payments | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00776 | silver | daily | textura | REST API | silver_textura.paymentholds | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00777 | silver | daily | textura | REST API | silver_textura.organizations | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00778 | silver | daily | textura | REST API | silver_textura.organizationlevelholds | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00779 | silver | daily | textura | REST API | silver_textura.manualcontracts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00781 | silver | daily | textura | REST API | silver_textura.invoices | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00782 | silver | daily | textura | REST API | silver_textura.invoiceapprovals | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00783 | silver | daily | textura | REST API | silver_textura.draws | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00784 | silver | daily | textura | REST API | silver_textura.contracts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00785 | silver | daily | textura | REST API | silver_textura.changeorders | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00786 | silver | daily | textura | REST API | silver_textura.budgetlines | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00787 | gold | daily |  |  | operation_financials.fact_project_labor_cost | unresolved_notebook_path | 300_silver_to_gold/operation_financials/silver_to_gold_fact_project_labor_cost | 0 |
| META-PROC-00788 | gold | monthly |  |  | bridgit_reporting.access_token_bridgit | resolved_notebook | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/source_to_gold_bridgit_api_access_token.py` | 0 |
| META-PROC-00789 | gold | daily |  |  | bridgit_reporting.dim_person | unresolved_notebook_path | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_person | 0 |
| META-PROC-00790 | gold | daily |  |  | bridgit_reporting.dim_project_bridgit | unresolved_notebook_path | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_project_bridgit | 0 |
| META-PROC-00791 | gold | daily |  |  | operation_financials.timesheet_compliance | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_timesheet_compliance.py` | 0 |
| META-PROC-00792 | gold | daily |  |  | origami.equipment | unresolved_notebook_path | 300_silver_to_gold/origami/silver_to_gold_origami_equipment | 0 |
| META-PROC-00793 | gold | daily |  |  | origami.locations | unresolved_notebook_path | 300_silver_to_gold/origami/silver_to_gold_origami_locations | 0 |
| META-PROC-00794 | gold | daily |  |  | textura.bridge_project_user_role_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_bridge_project_user_role | 0 |
| META-PROC-00795 | gold | daily |  |  | textura.dim_contract_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_contract | 0 |
| META-PROC-00796 | gold | daily |  |  | textura.dim_draw_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_draw | 0 |
| META-PROC-00797 | gold | daily |  |  | textura.dim_project_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_project | 0 |
| META-PROC-00798 | gold | daily |  |  | textura.dim_subcontractor | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_subcontractor | 0 |
| META-PROC-00799 | gold | daily |  |  | textura.dim_supplier_tracking | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_supplier_tracking | 0 |
| META-PROC-00800 | gold | daily |  |  | textura.dim_user_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_dim_user | 0 |
| META-PROC-00801 | gold | daily |  |  | textura.fact_budget_line_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_budgetline | 0 |
| META-PROC-00802 | gold | daily |  |  | textura.fact_change_order_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_change_order | 0 |
| META-PROC-00803 | gold | daily |  |  | textura.fact_invoice_approval_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_invoice_approval | 0 |
| META-PROC-00804 | gold | daily |  |  | textura.fact_invoice_line_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_invoiceline | 0 |
| META-PROC-00805 | gold | daily |  |  | textura.fact_invoice_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_invoice | 0 |
| META-PROC-00806 | gold | daily |  |  | textura.fact_lien_waiver_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_lien_waiver | 0 |
| META-PROC-00807 | gold | daily |  |  | textura.fact_payment_hold_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_payment_hold | 0 |
| META-PROC-00808 | gold | daily |  |  | textura.fact_payment_textura | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_payment | 0 |
| META-PROC-00809 | gold | daily |  |  | textura.fact_supplier_tracking | unresolved_notebook_path | 300_silver_to_gold/textura/silver_to_gold_fact_supplier_tracking | 0 |
| META-PROC-00810 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwBIContractVendorDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00811 | silver | daily | e1 | SQL Server | silver_e1.F55116Z | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00812 | silver | daily | timesheetapp | Azure SQL Database | silver_timesheetapp.TimeSheets | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00813 | silver | daily | timesheetapp | Azure SQL Database | silver_timesheetapp.TimeSheetDetails | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00814 | silver | daily | timesheetapp | Azure SQL Database | silver_timesheetapp.DailyEquipmentDetails | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00815 | silver | daily | timesheetapp | Azure SQL Database | silver_timesheetapp.DailyEquipment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00816 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwVendorChangeOrder | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00817 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwVendorAssociatedChangeItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00818 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPackageMilestone | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00819 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPackageDocument | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00820 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwLineItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00821 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwInvoicePayment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00822 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwInvoiceLineItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00823 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwInvoice | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00824 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCorePaymentTerm | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00825 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreIncoterm | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00826 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractVendorChangeOrderLineItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00827 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractVCOLineItemDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00828 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractScheduleOfValuesItemDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00829 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractScheduleOfValuesItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00830 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractScheduleOfValues | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00831 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractPackageCustomField | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00832 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractLineItemCustomField | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00833 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractDocument | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00834 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractDetailType | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00835 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractDetailManualAdjustment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00836 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractDetailCostItem | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00837 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwcontractdetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00838 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractContractExtended | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00839 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractContractDivisionOfResponsibility | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00840 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwContractCloseOut | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00841 | gold | daily |  |  | project_management.fact_contract_claim_history | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_claim_history.py` | 0 |
| META-PROC-00842 | gold | daily |  |  | project_management.fact_contract_closeout | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_closeout.py` | 0 |
| META-PROC-00843 | gold | daily |  |  | project_management.fact_contract_diversity | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_diversity.py` | 0 |
| META-PROC-00844 | gold | daily |  |  | project_management.fact_contract_line | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_line.py` | 0 |
| META-PROC-00845 | gold | daily |  |  | project_management.fact_contract_schedule_of_values | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_schedule_of_values.py` | 0 |
| META-PROC-00846 | gold | daily |  |  | project_management.fact_contract_vco_line | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_vco_line.py` | 0 |
| META-PROC-00847 | gold | daily |  |  | project_management.fact_invoice_line | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_invoice_line.py` | 0 |
| META-PROC-00848 | gold | daily |  |  | project_management.fact_invoice_payment | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_invoice_payment.py` | 0 |
| META-PROC-00849 | gold | daily |  |  | project_management.ref_bid_package_document | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_ref_bid_package_document.py` | 0 |
| META-PROC-00850 | gold | daily |  |  | project_management.ref_contract_document | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_ref_contract_document.py` | 0 |
| META-PROC-00851 | gold | daily |  |  | project_management_v.fact_invoice_payment_progress_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_invoice_payment_progress_v.py` | 0 |
| META-PROC-00852 | gold | daily |  |  | project_management_v.rpt_contract_line_exception_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_rpt_contract_line_exception_v.py` | 0 |
| META-PROC-00853 | gold | daily |  |  | project_management_v.rpt_contract_original_exception_v | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_rpt_contract_original_exception_v.py` | 0 |
| META-PROC-00854 | gold | daily |  |  | schedule_validator.fact_project_performance_snapshot | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/schedule_validator/silver_to_gold_vw_schedule_validator_project_snapshots.py` | 0 |
| META-PROC-00855 | silver | daily | ineight_document | SQL Server | silver_ineight_document.SubmittalRecipients | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00856 | silver | daily | ineight_document | SQL Server | silver_ineight_document.SubmittalMilestoneDates | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00857 | silver | daily | ineight_document | SQL Server | silver_ineight_document.SubmittalLinks | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00858 | silver | daily | ineight_document | SQL Server | silver_ineight_document.SubmittalDeleted | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00859 | silver | daily | ineight_document | SQL Server | silver_ineight_document.SubmittalCustFields | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00860 | silver | daily | ineight_document | SQL Server | silver_ineight_document.Submittal | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00861 | gold | daily |  |  | ineight_document.dim_submittals_core | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_dim_submittals_core.py` | 0 |
| META-PROC-00862 | gold | daily |  |  | ineight_document.fact_submittal_links | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittal_links.py` | 0 |
| META-PROC-00863 | gold | daily |  |  | ineight_document.fact_submittal_milestone | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittal_milestone.py` | 0 |
| META-PROC-00864 | gold | daily |  |  | ineight_document.fact_submittals_core | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittals_core.py` | 0 |
| META-PROC-00865 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanPlanNote | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00866 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwPlanWorkPackageConstraintManagement | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00867 | gold | daily |  |  | enterprise_reporting.in8_cr | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/enterprise_reporting/silver_to_gold_in8_cr_trn_cost_report.py` | 0 |
| META-PROC-00868 | silver | daily | e1 | SQL Server | silver_e1.FFZPS3N1 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00869 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwCoreEmployee | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00870 | silver | daily | webapp | Azure SQL Database - SDAT Web App | silver_webapp.UserMenu | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00871 | gold | daily |  |  | project_management.project_employee_role | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_project_employee_role.py` | 0 |
| META-PROC-00872 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwControlIntegrationAuditLogDetail | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00873 | gold | daily |  |  | enterprise_reporting.it_employee_hours | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/enterprise_reporting/silver_to_gold_it_employee_hours.py` | 0 |
| META-PROC-00874 | silver | daily | e1 | SQL Server | silver_e1.FFZPSGLC | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00875 | silver | daily | schedule_validator | REST API | silver_schedule_validator.project_tags | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00876 | silver | daily | schedule_validator | REST API | silver_schedule_validator.projects | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00877 | silver | daily | schedule_validator | REST API | silver_schedule_validator.org_charts | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00878 | silver | daily | schedule_validator | REST API | silver_schedule_validator.company_statistics | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00879 | gold | daily |  |  | operation_financials.scanman_audittrail | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_scanman_audittrail.py` | 0 |
| META-PROC-00880 | silver | daily | tradetapp | REST API | silver_tradetapp.qualifications | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00881 | silver | daily | tradetapp | REST API | silver_tradetapp.financials | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00882 | gold | daily |  |  | operation_financials.account_actuals_ledger | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_account_actuals_ledger_v.py` | 0 |
| META-PROC-00883 | gold | daily |  |  | conformed.dim_employee | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_employee.py` | 0 |
| META-PROC-00884 | silver | daily | e1 | SQL Server | silver_e1.F0724 | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00885 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleSnapshot | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00886 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResourceCodeValueAssignment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00887 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResourceCodeValue | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00888 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleResourceCode | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00889 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleSchedulePlanningPackageLogicLink | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00890 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleCodeValueAssignment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00891 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleCodeValue | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00892 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleCode | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00893 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityCodeValueAssignment | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00894 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityCodeValue | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00895 | silver | daily | ineight | Azure SQL Database | silver_ineight.vwScheduleScheduleActivityCode | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00896 | gold | daily |  |  | bridgit_reporting.dim_role | unresolved_notebook_path | 300_silver_to_gold/bridgit_reporting/silver_to_gold_dim_role | 0 |
| META-PROC-00897 | gold | daily |  |  | bridgit_reporting.fact_allocations | unresolved_notebook_path | 300_silver_to_gold/bridgit_reporting/silver_to_gold_fact_allocations | 0 |
| META-PROC-00898 | silver | daily | textura | REST API | silver_textura.lienwaivers | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00899 | silver | daily | textura | REST API | silver_textura.invoicelines | resolved_notebook | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 0 |
| META-PROC-00900 | gold | daily |  |  | tradetapp.subcontractor_qualification | resolved_notebook | `notebooks/data_engineering/300_silver_to_gold/tradetapp/silver_to_gold_subcontractor_qualification.py` | 0 |
| META-PROC-00901 | gold | daily |  |  | ineight_schedule.dim_activity_code | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_activity_code | 0 |
| META-PROC-00902 | gold | daily |  |  | ineight_schedule.dim_task | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_task | 0 |
| META-PROC-00903 | gold | daily |  |  | ineight_schedule.dim_wbs | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_dim_wbs | 0 |
| META-PROC-00904 | gold | daily |  |  | ineight_schedule.fact_task | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task | 0 |
| META-PROC-00905 | gold | daily |  |  | ineight_schedule.fact_task_baseline | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_fact_task_baseline | 0 |
| META-PROC-00906 | gold | daily |  |  | ineight_schedule_v.fact_task_baseline_current_v | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_baseline_current | 0 |
| META-PROC-00907 | gold | daily |  |  | ineight_schedule_v.fact_task_current_v | unresolved_notebook_path | 300_silver_to_gold/ineight_schedule/silver_to_gold_vw_fact_task_current | 0 |

## Validation focus

- Review `unresolved_notebook_path`, `external_workspace_path`, and `procedure_or_sql` rows before generating Databricks jobs.
- Confirm whether disabled rows represent retired, future, manual, or environment-specific processing.
- Verify source type and batch group values with domain owners before using them as migration waves.
- Treat `lastExecutionTimestamp` as metadata evidence only; reconcile with Databricks and ADF run history.

The machine-readable export summary is `architecture-lens/metadata/metadata-exports.json`.
