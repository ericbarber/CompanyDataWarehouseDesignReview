# Notebook Catalog

Generated from `DW2023-Databricks.zip` on 2026-07-22.

The catalog contains every Python file under the Databricks `notebooks/` tree. It is an evidence index; each record still requires owner validation before it is treated as production truth.

## Summary by layer

| Layer | Notebook count |
|---|---:|
| 000_source_to_raw | 13 |
| 100_raw_to_bronze | 75 |
| 200_bronze_to_silver | 2 |
| 300_silver_to_gold | 433 |
| environment_promotion | 14 |
| maintenance | 18 |
| miscellaneous_scripts | 13 |
| security | 2 |
| startup | 1 |
| utility | 10 |

## Top discovered domains

| Domain | Notebook count |
|---|---:|
| project_management | 99 |
| safety | 52 |
| cosential | 35 |
| equipment | 32 |
| operation_financials | 31 |
| textura | 21 |
| mpr | 18 |
| prolog | 16 |
| schedule | 15 |
| z_backfill | 14 |
| cmt | 13 |
| destimator | 13 |
| emars | 12 |
| optimize_and_zorder | 12 |
| bridgit_reporting | 11 |
| b2g | 10 |
| conformed | 9 |
| security | 9 |
| web_app_integration | 8 |
| cosential_api | 7 |

## Notebook index

| ID | Layer | Domain | Notebook | Widgets | Tables | Secrets | Runs |
|---|---|---|---|---:|---:|---:|---:|
| NB-00001 | 000_source_to_raw | powerbi | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-activityevents-one-off-load.py` | 9 | 1 | 3 | 0 |
| NB-00002 | 000_source_to_raw | powerbi | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-activityevents.py` | 9 | 1 | 3 | 0 |
| NB-00003 | 000_source_to_raw | powerbi | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-groups.py` | 9 | 0 | 3 | 0 |
| NB-00004 | 000_source_to_raw | powerbi | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-master.py` | 12 | 0 | 0 | 1 |
| NB-00005 | 000_source_to_raw | powerbi | `notebooks/data_engineering/000_source_to_raw/source-to-raw-powerbi-reports.py` | 9 | 1 | 3 | 0 |
| NB-00006 | 000_source_to_raw | schedulevalidator | `notebooks/data_engineering/000_source_to_raw/source-to-raw-schedulevalidator.py` | 10 | 2 | 1 | 0 |
| NB-00007 | 000_source_to_raw | teambinder | `notebooks/data_engineering/000_source_to_raw/source-to-raw-teambinder.py` | 9 | 5 | 1 | 0 |
| NB-00008 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetfencehistory.py` | 9 | 1 | 3 | 0 |
| NB-00009 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetoperationfeed.py` | 9 | 1 | 3 | 0 |
| NB-00010 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetoperationhistory.py` | 9 | 1 | 3 | 0 |
| NB-00011 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-assetsummary.py` | 9 | 1 | 3 | 0 |
| NB-00012 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-faultshistory.py` | 9 | 1 | 3 | 0 |
| NB-00013 | 000_source_to_raw | visionlink | `notebooks/data_engineering/000_source_to_raw/visionlink/source-to-raw-utilizationhistory.py` | 9 | 1 | 3 | 0 |
| NB-00014 | 100_raw_to_bronze | autodesk | `notebooks/data_engineering/100_raw_to_bronze/autodesk/source_to_gold_autodesk_api_refresh_token.py` | 7 | 5 | 3 | 0 |
| NB-00015 | 100_raw_to_bronze | azure_cost_management_api | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_actualcost.py` | 8 | 5 | 4 | 0 |
| NB-00016 | 100_raw_to_bronze | azure_cost_management_api | `notebooks/data_engineering/100_raw_to_bronze/azure_cost_management_api/source_to_bronze_amortizedcost.py` | 8 | 5 | 4 | 0 |
| NB-00017 | 100_raw_to_bronze | b2g | `notebooks/data_engineering/100_raw_to_bronze/b2g/raw_to_bronze_b2g_api_contract.py` | 8 | 4 | 2 | 0 |
| NB-00018 | 100_raw_to_bronze | b2g | `notebooks/data_engineering/100_raw_to_bronze/b2g/raw_to_bronze_b2g_api_contract_vendor.py` | 8 | 3 | 2 | 0 |
| NB-00019 | 100_raw_to_bronze | b2g | `notebooks/data_engineering/100_raw_to_bronze/b2g/raw_to_bronze_b2g_api_master.py` | 9 | 0 | 0 | 1 |
| NB-00020 | 100_raw_to_bronze | b2g | `notebooks/data_engineering/100_raw_to_bronze/b2g/raw_to_bronze_b2g_api_vendor.py` | 8 | 3 | 2 | 0 |
| NB-00021 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_account_certifications.py` | 8 | 5 | 1 | 0 |
| NB-00022 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_hourly_allocations.py` | 8 | 5 | 1 | 0 |
| NB-00023 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_hourly_roles.py` | 8 | 5 | 1 | 0 |
| NB-00024 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_master.py` | 0 | 0 | 0 | 1 |
| NB-00025 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_persons.py` | 8 | 5 | 1 | 0 |
| NB-00026 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_project_allocations.py` | 8 | 5 | 1 | 0 |
| NB-00027 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_project_groups.py` | 8 | 4 | 1 | 0 |
| NB-00028 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_projects.py` | 8 | 5 | 1 | 0 |
| NB-00029 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_bronze_bridgit_reporting_roles.py` | 8 | 4 | 1 | 0 |
| NB-00030 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/raw_to_silver_bridgit_reporting_master.py` | 2 | 0 | 0 | 2 |
| NB-00031 | 100_raw_to_bronze | bridgit_reporting | `notebooks/data_engineering/100_raw_to_bronze/bridgit_reporting/source_to_gold_bridgit_api_access_token.py` | 7 | 4 | 3 | 0 |
| NB-00032 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_companies.py` | 8 | 2 | 3 | 0 |
| NB-00033 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_contact_opportunities.py` | 8 | 2 | 3 | 0 |
| NB-00034 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_contact_projects.py` | 8 | 2 | 3 | 0 |
| NB-00035 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_contacts.py` | 8 | 2 | 3 | 0 |
| NB-00036 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_master.py` | 9 | 0 | 0 | 1 |
| NB-00037 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_opportunities.py` | 8 | 2 | 3 | 0 |
| NB-00038 | 100_raw_to_bronze | cosential_api | `notebooks/data_engineering/100_raw_to_bronze/cosential_api/raw_to_bronze_cosential_api_projects.py` | 8 | 2 | 3 | 0 |
| NB-00039 | 100_raw_to_bronze | cslb_data | `notebooks/data_engineering/100_raw_to_bronze/cslb_data/source_to_bronze_california_license_data.py` | 9 | 3 | 0 | 0 |
| NB-00040 | 100_raw_to_bronze | cslb_data | `notebooks/data_engineering/100_raw_to_bronze/cslb_data/source_to_bronze_california_license_data_v2.py` | 9 | 3 | 0 | 0 |
| NB-00041 | 100_raw_to_bronze | jjkeller | `notebooks/data_engineering/100_raw_to_bronze/jjkeller/raw_to_bronze_jjkeller_credentials.py` | 8 | 3 | 2 | 0 |
| NB-00042 | 100_raw_to_bronze | metadata_promotion | `notebooks/data_engineering/100_raw_to_bronze/metadata_promotion/build_metadata_table.py` | 4 | 1 | 0 | 0 |
| NB-00043 | 100_raw_to_bronze | nccer | `notebooks/data_engineering/100_raw_to_bronze/nccer/raw_to_bronze_nccer_credentials.py` | 8 | 5 | 2 | 0 |
| NB-00044 | 100_raw_to_bronze | power_bi | `notebooks/data_engineering/100_raw_to_bronze/power_bi/raw_to_bronze_power_bi_get_reports_api.py` | 8 | 3 | 3 | 0 |
| NB-00045 | 100_raw_to_bronze | procore | `notebooks/data_engineering/100_raw_to_bronze/procore/procore_auth.py` | 1 | 3 | 2 | 0 |
| NB-00046 | 100_raw_to_bronze | procore | `notebooks/data_engineering/100_raw_to_bronze/procore/raw_to_bronze_procore_rfis.py` | 7 | 5 | 0 | 0 |
| NB-00047 | 100_raw_to_bronze | procore | `notebooks/data_engineering/100_raw_to_bronze/procore/raw_to_bronze_procore_submittals.py` | 7 | 4 | 0 | 0 |
| NB-00048 | 100_raw_to_bronze | raw | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze.py` | 9 | 1 | 0 | 0 |
| NB-00049 | 100_raw_to_bronze | clue | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_clue_all.py` | 8 | 3 | 0 | 0 |
| NB-00050 | 100_raw_to_bronze | files | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_files_all.py` | 8 | 3 | 0 | 0 |
| NB-00051 | 100_raw_to_bronze | v2 | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_v2.py` | 9 | 2 | 0 | 0 |
| NB-00052 | 100_raw_to_bronze | zipcodes | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_zipcodes_all.py` | 8 | 3 | 1 | 0 |
| NB-00053 | 100_raw_to_bronze | zipcodes | `notebooks/data_engineering/100_raw_to_bronze/raw_to_bronze_zipcodes_all_v2.py` | 9 | 3 | 0 | 0 |
| NB-00054 | 100_raw_to_bronze | schedule_validator | `notebooks/data_engineering/100_raw_to_bronze/schedule_validator/raw_to_bronze_schedule_validator_company_statistics.py` | 8 | 3 | 4 | 0 |
| NB-00055 | 100_raw_to_bronze | schedule_validator | `notebooks/data_engineering/100_raw_to_bronze/schedule_validator/raw_to_bronze_schedule_validator_org_charts.py` | 8 | 2 | 4 | 0 |
| NB-00056 | 100_raw_to_bronze | schedule_validator | `notebooks/data_engineering/100_raw_to_bronze/schedule_validator/raw_to_bronze_schedule_validator_project_tags.py` | 8 | 2 | 4 | 0 |
| NB-00057 | 100_raw_to_bronze | schedule_validator | `notebooks/data_engineering/100_raw_to_bronze/schedule_validator/raw_to_bronze_schedule_validator_projects.py` | 8 | 3 | 4 | 0 |
| NB-00058 | 100_raw_to_bronze | sitesense | `notebooks/data_engineering/100_raw_to_bronze/sitesense/raw_to_bronze_sitesense.py` | 8 | 5 | 1 | 0 |
| NB-00059 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_budgetlines.py` | 8 | 4 | 3 | 0 |
| NB-00060 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_changeorders.py` | 8 | 4 | 3 | 0 |
| NB-00061 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_contracts.py` | 8 | 4 | 3 | 0 |
| NB-00062 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_draws.py` | 8 | 4 | 3 | 0 |
| NB-00063 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_invoiceapprovals.py` | 8 | 4 | 3 | 0 |
| NB-00064 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_invoices.py` | 8 | 4 | 3 | 0 |
| NB-00065 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_linewaivers.py` | 8 | 4 | 3 | 0 |
| NB-00066 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_manualcontracts.py` | 8 | 4 | 3 | 0 |
| NB-00067 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_organizationlevelholds.py` | 8 | 4 | 3 | 0 |
| NB-00068 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_organizations.py` | 8 | 4 | 3 | 0 |
| NB-00069 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_paymentholds.py` | 8 | 4 | 3 | 0 |
| NB-00070 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_payments.py` | 8 | 4 | 3 | 0 |
| NB-00071 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projects.py` | 8 | 4 | 3 | 0 |
| NB-00072 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_projectuserroles.py` | 8 | 4 | 3 | 0 |
| NB-00073 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingcontractorvalues.py` | 8 | 4 | 3 | 0 |
| NB-00074 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingprograms.py` | 8 | 4 | 3 | 0 |
| NB-00075 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingprogramvalues.py` | 8 | 4 | 3 | 0 |
| NB-00076 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_suppliertrackingselectedvalues.py` | 8 | 4 | 3 | 0 |
| NB-00077 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_tpaenrollments.py` | 8 | 4 | 3 | 0 |
| NB-00078 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_tpaprograms.py` | 8 | 4 | 3 | 0 |
| NB-00079 | 100_raw_to_bronze | textura | `notebooks/data_engineering/100_raw_to_bronze/textura/source_to_bronze_users.py` | 8 | 4 | 3 | 0 |
| NB-00080 | 100_raw_to_bronze | tradetapp | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_financials.py` | 8 | 4 | 0 | 0 |
| NB-00081 | 100_raw_to_bronze | tradetapp | `notebooks/data_engineering/100_raw_to_bronze/tradetapp/source_to_bronze_qualifications.py` | 8 | 4 | 0 | 0 |
| NB-00082 | 100_raw_to_bronze | vairkko | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_certifications.py` | 8 | 3 | 2 | 0 |
| NB-00083 | 100_raw_to_bronze | vairkko | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_templates.py` | 8 | 3 | 2 | 0 |
| NB-00084 | 100_raw_to_bronze | vairkko | `notebooks/data_engineering/100_raw_to_bronze/vairkko/raw_to_bronze_vairkko_users.py` | 8 | 3 | 2 | 0 |
| NB-00085 | 100_raw_to_bronze | visionlinkcat | `notebooks/data_engineering/100_raw_to_bronze/visionlinkcat/raw_to_bronze_visionlink.py` | 9 | 1 | 0 | 0 |
| NB-00086 | 100_raw_to_bronze | vrm | `notebooks/data_engineering/100_raw_to_bronze/vrm/raw_to_bronze_vrm_driver_compliance.py` | 8 | 1 | 0 | 0 |
| NB-00087 | 100_raw_to_bronze | weld_office | `notebooks/data_engineering/100_raw_to_bronze/weld_office/raw_to_bronze_weld_office_process_expiry.py` | 8 | 2 | 0 | 0 |
| NB-00088 | 100_raw_to_bronze | weld_office | `notebooks/data_engineering/100_raw_to_bronze/weld_office/raw_to_bronze_weld_office_wpq.py` | 8 | 2 | 0 | 0 |
| NB-00089 | 200_bronze_to_silver | bronze | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver.py` | 15 | 1 | 0 | 0 |
| NB-00090 | 200_bronze_to_silver | v2 | `notebooks/data_engineering/200_bronze_to_silver/bronze_to_silver_v2.py` | 15 | 1 | 0 | 0 |
| NB-00091 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_vendor.py` | 6 | 5 | 1 | 0 |
| NB-00092 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_xbe.py` | 6 | 6 | 1 | 0 |
| NB-00093 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_dim_xbe_subcontractor_commitments.py` | 6 | 6 | 1 | 0 |
| NB-00094 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_fact_contract_payment_xbe.py` | 6 | 7 | 1 | 0 |
| NB-00095 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_fact_vendor_payment_xbe.py` | 6 | 10 | 1 | 0 |
| NB-00096 | 300_silver_to_gold | b2g | `notebooks/data_engineering/300_silver_to_gold/b2g/silver_to_gold_vw_fact_vendor_performance_xbe.py` | 6 | 15 | 1 | 0 |
| NB-00097 | 300_silver_to_gold | bridgit | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgit_project.py` | 6 | 11 | 1 | 0 |
| NB-00098 | 300_silver_to_gold | bridgit | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_nccer_credentials.py` | 6 | 4 | 1 | 0 |
| NB-00099 | 300_silver_to_gold | bridgit | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vairkko_certifications.py` | 6 | 4 | 1 | 0 |
| NB-00100 | 300_silver_to_gold | bridgit | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vairkko_templates.py` | 6 | 4 | 1 | 0 |
| NB-00101 | 300_silver_to_gold | bridgit | `notebooks/data_engineering/300_silver_to_gold/bridgit/silver_to_gold_vw_brdgt_vrm_driver_compliance.py` | 6 | 4 | 1 | 0 |
| NB-00102 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_enr_buildingcost_index.py` | 6 | 4 | 2 | 0 |
| NB-00103 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimate_fee_details.py` | 6 | 5 | 2 | 0 |
| NB-00104 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_general.py` | 6 | 5 | 2 | 0 |
| NB-00105 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_hmf.py` | 6 | 5 | 2 | 0 |
| NB-00106 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_office.py` | 6 | 5 | 2 | 0 |
| NB-00107 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_parking.py` | 6 | 5 | 2 | 0 |
| NB-00108 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_project.py` | 6 | 5 | 2 | 0 |
| NB-00109 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_renovation.py` | 6 | 5 | 2 | 0 |
| NB-00110 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_rsmeans_escalator.py` | 6 | 5 | 2 | 0 |
| NB-00111 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_estimatedatadetails_sm.py` | 6 | 5 | 2 | 0 |
| NB-00112 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_historicalcostdata.py` | 6 | 5 | 2 | 0 |
| NB-00113 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_st_dictionary.py` | 6 | 5 | 2 | 0 |
| NB-00114 | 300_silver_to_gold | cmt | `notebooks/data_engineering/300_silver_to_gold/cmt/silver_to_gold_cmt_summarydatadetails.py` | 6 | 4 | 2 | 0 |
| NB-00115 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_bridge_vendor_eval_evaluator.py` | 6 | 7 | 1 | 0 |
| NB-00116 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_bridge_vendor_eval_work_package.py` | 6 | 10 | 1 | 0 |
| NB-00117 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_project_phase.py` | 6 | 4 | 1 | 0 |
| NB-00118 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_vendor_evaluation_form.py` | 6 | 5 | 1 | 0 |
| NB-00119 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_dim_work_package_trade.py` | 6 | 4 | 1 | 0 |
| NB-00120 | 300_silver_to_gold | compliance | `notebooks/data_engineering/300_silver_to_gold/compliance/silver_to_gold_fact_vendor_evaluation.py` | 6 | 11 | 1 | 0 |
| NB-00121 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_company.py` | 8 | 12 | 1 | 0 |
| NB-00122 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_date.py` | 8 | 5 | 1 | 0 |
| NB-00123 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_employee.py` | 3 | 12 | 1 | 0 |
| NB-00124 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_project.py` | 3 | 42 | 1 | 0 |
| NB-00125 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_project_org_hierarchy.py` | 6 | 19 | 1 | 0 |
| NB-00126 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_dim_zipcodes.py` | 8 | 10 | 1 | 0 |
| NB-00127 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_fact_project_details.py` | 6 | 7 | 1 | 0 |
| NB-00128 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_vw_business_unit.py` | 6 | 6 | 1 | 0 |
| NB-00129 | 300_silver_to_gold | conformed | `notebooks/data_engineering/300_silver_to_gold/conformed/silver_to_gold_vw_closed_project.py` | 6 | 6 | 1 | 0 |
| NB-00130 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_bridge_project_opportunity_contact.py` | 6 | 13 | 1 | 0 |
| NB-00131 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_construction_type.py` | 6 | 6 | 1 | 0 |
| NB-00132 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_company.py` | 6 | 7 | 1 | 0 |
| NB-00133 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_contact.py` | 6 | 10 | 1 | 0 |
| NB-00134 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_project_opportunity_hierarchy.py` | 6 | 20 | 1 | 0 |
| NB-00135 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_cosential_states.py` | 6 | 5 | 1 | 0 |
| NB-00136 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_office.py` | 6 | 10 | 1 | 0 |
| NB-00137 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity.py` | 6 | 15 | 1 | 0 |
| NB-00138 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity_consultants.py` | 6 | 7 | 1 | 0 |
| NB-00139 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_opportunity_staff.py` | 6 | 6 | 1 | 0 |
| NB-00140 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_personnel.py` | 6 | 4 | 1 | 0 |
| NB-00141 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_awards.py` | 6 | 8 | 1 | 0 |
| NB-00142 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_certifications.py` | 6 | 7 | 1 | 0 |
| NB-00143 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_consultants.py` | 6 | 8 | 1 | 0 |
| NB-00144 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_consultants_contacts.py` | 6 | 10 | 1 | 0 |
| NB-00145 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_descriptions.py` | 6 | 7 | 1 | 0 |
| NB-00146 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_documents.py` | 6 | 8 | 1 | 0 |
| NB-00147 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_fees_contract.py` | 6 | 8 | 1 | 0 |
| NB-00148 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_joint_venture.py` | 6 | 8 | 1 | 0 |
| NB-00149 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_joint_venture_other.py` | 6 | 8 | 1 | 0 |
| NB-00150 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_market.py` | 6 | 8 | 1 | 0 |
| NB-00151 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_owner_client.py` | 6 | 8 | 1 | 0 |
| NB-00152 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_owner_client_contacts.py` | 6 | 11 | 1 | 0 |
| NB-00153 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_reference.py` | 6 | 9 | 1 | 0 |
| NB-00154 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_reference_testimonials.py` | 6 | 8 | 1 | 0 |
| NB-00155 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_staff.py` | 6 | 9 | 1 | 0 |
| NB-00156 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_project_type.py` | 6 | 7 | 1 | 0 |
| NB-00157 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_service_types.py` | 6 | 8 | 1 | 0 |
| NB-00158 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_studio.py` | 6 | 10 | 1 | 0 |
| NB-00159 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_subproject.py` | 6 | 10 | 1 | 0 |
| NB-00160 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_dim_type.py` | 6 | 6 | 1 | 0 |
| NB-00161 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_opportunity.py` | 6 | 11 | 1 | 0 |
| NB-00162 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_opportunity_notes.py` | 6 | 6 | 1 | 0 |
| NB-00163 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_fact_project.py` | 6 | 19 | 1 | 0 |
| NB-00164 | 300_silver_to_gold | cosential | `notebooks/data_engineering/300_silver_to_gold/cosential/silver_to_gold_vw_fact_opportunity_current.py` | 6 | 6 | 1 | 0 |
| NB-00165 | 300_silver_to_gold | cslb | `notebooks/data_engineering/300_silver_to_gold/cslb/silver_to_gold_license_data.py` | 7 | 5 | 1 | 0 |
| NB-00166 | 300_silver_to_gold | deficiencies | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_csi_code.py` | 6 | 5 | 1 | 0 |
| NB-00167 | 300_silver_to_gold | deficiencies | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_category.py` | 6 | 7 | 1 | 0 |
| NB-00168 | 300_silver_to_gold | deficiencies | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_cause_disposition.py` | 6 | 6 | 1 | 0 |
| NB-00169 | 300_silver_to_gold | deficiencies | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_dim_deficiency_division_group.py` | 6 | 6 | 1 | 0 |
| NB-00170 | 300_silver_to_gold | deficiencies | `notebooks/data_engineering/300_silver_to_gold/deficiencies/silver_to_gold_fact_deficiency.py` | 8 | 22 | 1 | 0 |
| NB-00171 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_enr_building_cost_Index.py` | 6 | 6 | 1 | 0 |
| NB-00172 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate.py` | 6 | 14 | 1 | 0 |
| NB-00173 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate_feedata.py` | 6 | 6 | 1 | 0 |
| NB-00174 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_estimate_summary.py` | 6 | 6 | 1 | 0 |
| NB-00175 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_rsmeans_escalator.py` | 6 | 6 | 1 | 0 |
| NB-00176 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_dim_sundtcmt_dictionary.py` | 6 | 6 | 1 | 0 |
| NB-00177 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_general.py` | 6 | 6 | 1 | 0 |
| NB-00178 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_hmf.py` | 6 | 7 | 1 | 0 |
| NB-00179 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_office.py` | 6 | 7 | 1 | 0 |
| NB-00180 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_parking.py` | 6 | 7 | 1 | 0 |
| NB-00181 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_project.py` | 6 | 7 | 1 | 0 |
| NB-00182 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_renovation.py` | 6 | 7 | 1 | 0 |
| NB-00183 | 300_silver_to_gold | destimator | `notebooks/data_engineering/300_silver_to_gold/destimator/silver_to_gold_fact_estimate_sm.py` | 6 | 7 | 1 | 0 |
| NB-00184 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_contractor.py` | 8 | 6 | 1 | 0 |
| NB-00185 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_employee_emars.py` | 8 | 7 | 1 | 0 |
| NB-00186 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_ethnicity.py` | 8 | 6 | 1 | 0 |
| NB-00187 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_project_emars.py` | 8 | 7 | 1 | 0 |
| NB-00188 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_dim_work_class.py` | 8 | 6 | 1 | 0 |
| NB-00189 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_fact_payroll.py` | 6 | 16 | 1 | 0 |
| NB-00190 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_fact_payroll_aggregated.py` | 6 | 14 | 1 | 0 |
| NB-00191 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_payroll_aggregate_nonsensitive_v.py` | 6 | 7 | 1 | 0 |
| NB-00192 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_payroll_hours_nonsensitive_v.py` | 6 | 6 | 1 | 0 |
| NB-00193 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_v.py` | 6 | 7 | 1 | 0 |
| NB-00194 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_work_class_v.py` | 6 | 8 | 1 | 0 |
| NB-00195 | 300_silver_to_gold | emars | `notebooks/data_engineering/300_silver_to_gold/emars/silver_to_gold_vw_fact_workforce_summary_worker_zip_v.py` | 6 | 7 | 1 | 0 |
| NB-00196 | 300_silver_to_gold | enterprise_reporting | `notebooks/data_engineering/300_silver_to_gold/enterprise_reporting/silver_to_gold_in8_cr_trn_cost_report.py` | 6 | 13 | 1 | 0 |
| NB-00197 | 300_silver_to_gold | enterprise_reporting | `notebooks/data_engineering/300_silver_to_gold/enterprise_reporting/silver_to_gold_it_employee_hours.py` | 6 | 5 | 1 | 0 |
| NB-00198 | 300_silver_to_gold | enterprise_reporting | `notebooks/data_engineering/300_silver_to_gold/enterprise_reporting/silver_to_gold_vw_generic_cost_curve_v.py` | 6 | 15 | 1 | 0 |
| NB-00199 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_bridge_work_order_gl_trans.py` | 6 | 8 | 1 | 0 |
| NB-00200 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment.py` | 6 | 9 | 1 | 0 |
| NB-00201 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_alert.py` | 6 | 4 | 1 | 0 |
| NB-00202 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_history.py` | 6 | 5 | 1 | 0 |
| NB-00203 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_rate_group.py` | 6 | 6 | 1 | 0 |
| NB-00204 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_status.py` | 6 | 6 | 1 | 0 |
| NB-00205 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_equipment_type.py` | 6 | 11 | 1 | 0 |
| NB-00206 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_maint_schedule_status.py` | 6 | 7 | 1 | 0 |
| NB-00207 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_maint_schedule_type.py` | 6 | 5 | 1 | 0 |
| NB-00208 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_responsible_party.py` | 6 | 4 | 1 | 0 |
| NB-00209 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order.py` | 6 | 5 | 1 | 0 |
| NB-00210 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_ownership.py` | 6 | 6 | 1 | 0 |
| NB-00211 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_status.py` | 6 | 6 | 1 | 0 |
| NB-00212 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_dim_work_order_type.py` | 6 | 8 | 1 | 0 |
| NB-00213 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment.py` | 8 | 11 | 1 | 0 |
| NB-00214 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_account_balance_monthly.py` | 8 | 21 | 1 | 0 |
| NB-00215 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_account_balance_weekly.py` | 8 | 9 | 1 | 0 |
| NB-00216 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_alerts.py` | 6 | 13 | 1 | 0 |
| NB-00217 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_availability.py` | 7 | 7 | 1 | 0 |
| NB-00218 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_demand.py` | 6 | 10 | 1 | 0 |
| NB-00219 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_gl_trans.py` | 8 | 19 | 1 | 0 |
| NB-00220 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_site_rate_integration_log.py` | 8 | 13 | 1 | 0 |
| NB-00221 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_status_history.py` | 6 | 8 | 1 | 0 |
| NB-00222 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_type_demand.py` | 6 | 7 | 1 | 0 |
| NB-00223 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_equipment_utilization.py` | 6 | 26 | 1 | 0 |
| NB-00224 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_maint_schedule.py` | 8 | 9 | 1 | 0 |
| NB-00225 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_fact_work_order.py` | 8 | 23 | 1 | 0 |
| NB-00226 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_dim_account_master_all_v.py` | 6 | 5 | 1 | 0 |
| NB-00227 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_dim_project_bu_all_v.py` | 6 | 5 | 1 | 0 |
| NB-00228 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_equipment_rental_in_service_v.py` | 6 | 11 | 1 | 0 |
| NB-00229 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_equipment_site_rates_ineight_current_v.py` | 6 | 10 | 1 | 0 |
| NB-00230 | 300_silver_to_gold | equipment | `notebooks/data_engineering/300_silver_to_gold/equipment/silver_to_gold_vw_fact_work_order_gl_trans_v.py` | 6 | 8 | 1 | 0 |
| NB-00231 | 300_silver_to_gold | heavyjob | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_daily_cost_by_cost_code.py` | 6 | 8 | 1 | 0 |
| NB-00232 | 300_silver_to_gold | heavyjob | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_equip_detail.py` | 6 | 9 | 1 | 0 |
| NB-00233 | 300_silver_to_gold | heavyjob | `notebooks/data_engineering/300_silver_to_gold/heavyjob/silver_to_gold_fact_labor_detail.py` | 6 | 6 | 1 | 0 |
| NB-00234 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_dim_form.py` | 6 | 5 | 1 | 0 |
| NB-00235 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_dim_submittals_core.py` | 6 | 7 | 1 | 0 |
| NB-00236 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_rfi.py` | 6 | 12 | 1 | 0 |
| NB-00237 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittal_links.py` | 6 | 10 | 1 | 0 |
| NB-00238 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittal_milestone.py` | 6 | 7 | 1 | 0 |
| NB-00239 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittals.py` | 6 | 12 | 1 | 0 |
| NB-00240 | 300_silver_to_gold | ineight_document | `notebooks/data_engineering/300_silver_to_gold/ineight_document/silver_to_gold_fact_submittals_core.py` | 6 | 9 | 1 | 0 |
| NB-00241 | 300_silver_to_gold | ineight_document_reporting | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_dim_document_rfi_report.py` | 6 | 5 | 1 | 0 |
| NB-00242 | 300_silver_to_gold | ineight_document_reporting | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_dim_document_submittal.py` | 6 | 5 | 1 | 0 |
| NB-00243 | 300_silver_to_gold | ineight_document_reporting | `notebooks/data_engineering/300_silver_to_gold/ineight_document_reporting/silver_to_gold_fact_document.py` | 6 | 14 | 1 | 0 |
| NB-00244 | 300_silver_to_gold | labor | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_monthly_subcontractors_hours_by_project.py` | 8 | 10 | 1 | 0 |
| NB-00245 | 300_silver_to_gold | labor | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_weekly_labor_head_count.py` | 8 | 11 | 1 | 0 |
| NB-00246 | 300_silver_to_gold | labor | `notebooks/data_engineering/300_silver_to_gold/labor/silver_to_gold_fact_weekly_labor_hours_by_project.py` | 6 | 10 | 1 | 0 |
| NB-00247 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_dim_mpr_status.py` | 6 | 5 | 1 | 0 |
| NB-00248 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_cor_adjustments.py` | 6 | 10 | 1 | 0 |
| NB-00249 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_costs_vs_budget_summary.py` | 6 | 9 | 1 | 0 |
| NB-00250 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_mpr_base.py` | 6 | 9 | 1 | 0 |
| NB-00251 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_pcco_adjustments.py` | 6 | 10 | 1 | 0 |
| NB-00252 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_reconciliation.py` | 6 | 9 | 1 | 0 |
| NB-00253 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_status.py` | 6 | 11 | 1 | 0 |
| NB-00254 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_fact_upqa.py` | 6 | 10 | 1 | 0 |
| NB-00255 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_account_balances.py` | 6 | 9 | 2 | 0 |
| NB-00256 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_account_master.py` | 6 | 7 | 2 | 0 |
| NB-00257 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_active_projects.py` | 6 | 6 | 2 | 0 |
| NB-00258 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_billing_summary.py` | 6 | 9 | 2 | 0 |
| NB-00259 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_contract_summary.py` | 6 | 14 | 2 | 0 |
| NB-00260 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_contracts.py` | 6 | 13 | 2 | 0 |
| NB-00261 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_cors_detail.py` | 6 | 9 | 2 | 0 |
| NB-00262 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_data_import_log.py` | 6 | 6 | 2 | 0 |
| NB-00263 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_employee_project.py` | 6 | 11 | 2 | 0 |
| NB-00264 | 300_silver_to_gold | mpr | `notebooks/data_engineering/300_silver_to_gold/mpr/silver_to_gold_mpr_source_pcco_details.py` | 6 | 7 | 2 | 0 |
| NB-00265 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_account_master.py` | 6 | 13 | 1 | 0 |
| NB-00266 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_document_type.py` | 6 | 5 | 1 | 0 |
| NB-00267 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_dim_ledger_type.py` | 6 | 5 | 1 | 0 |
| NB-00268 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance.py` | 6 | 17 | 1 | 0 |
| NB-00269 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance_monthly_detail.py` | 6 | 16 | 1 | 0 |
| NB-00270 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance_monthly_header.py` | 6 | 25 | 1 | 0 |
| NB-00271 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_account_balance_weekly.py` | 6 | 26 | 1 | 0 |
| NB-00272 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_accounts_payable.py` | 8 | 12 | 1 | 0 |
| NB-00273 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_accounts_receivable.py` | 6 | 10 | 1 | 0 |
| NB-00274 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_contracts.py` | 8 | 14 | 1 | 0 |
| NB-00275 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_pco_line_items.py` | 8 | 9 | 1 | 0 |
| NB-00276 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_project_billing.py` | 6 | 13 | 1 | 0 |
| NB-00277 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_project_cash_position.py` | 8 | 13 | 1 | 0 |
| NB-00278 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_wpr_weekly.py` | 6 | 31 | 1 | 0 |
| NB-00279 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_wpr_weekly_gl_date_rpt_v.py` | 6 | 6 | 1 | 0 |
| NB-00280 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_fact_wpr_weekly_work_date_rpt_v.py` | 6 | 6 | 1 | 0 |
| NB-00281 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_health_scorecard.py` | 6 | 7 | 1 | 0 |
| NB-00282 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_proforma_executive_summary.py` | 6 | 10 | 1 | 0 |
| NB-00283 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_scanman_approvals.py` | 6 | 6 | 1 | 0 |
| NB-00284 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_scanman_audittrail.py` | 6 | 4 | 1 | 0 |
| NB-00285 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_stg_fact_wpr_weekly.py` | 6 | 8 | 1 | 0 |
| NB-00286 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_timesheet_compliance.py` | 6 | 21 | 1 | 0 |
| NB-00287 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_account_actuals_ledger_v.py` | 6 | 5 | 1 | 0 |
| NB-00288 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_dim_account_master_lvl7_v.py` | 6 | 5 | 1 | 0 |
| NB-00289 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_fact_project_billing_current_v.py` | 6 | 6 | 1 | 0 |
| NB-00290 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_fact_project_cash_position_current_v.py` | 6 | 6 | 1 | 0 |
| NB-00291 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_fact_wpr_weekly_rpt_v.py` | 6 | 6 | 1 | 0 |
| NB-00292 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_missed_time_card_v.py` | 6 | 8 | 1 | 0 |
| NB-00293 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_scanman_workbench_v.py` | 6 | 15 | 1 | 0 |
| NB-00294 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_statement_of_operations_ba_v.py` | 6 | 4 | 1 | 0 |
| NB-00295 | 300_silver_to_gold | operation_financials | `notebooks/data_engineering/300_silver_to_gold/operation_financials/silver_to_gold_vw_statement_of_operations_v.py` | 6 | 4 | 1 | 0 |
| NB-00296 | 300_silver_to_gold | proforma | `notebooks/data_engineering/300_silver_to_gold/proforma/silver_to_gold_fact_proforma.py` | 8 | 4 | 1 | 0 |
| NB-00297 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_brdg_work_package_component.py` | 6 | 6 | 1 | 0 |
| NB-00298 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_brdg_work_package_cost_item.py` | 6 | 6 | 1 | 0 |
| NB-00299 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_bridge_bid_package_cost_item.py` | 6 | 8 | 1 | 0 |
| NB-00300 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_bridge_contract_closeout_user.py` | 6 | 8 | 1 | 0 |
| NB-00301 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_bid_package.py` | 6 | 8 | 1 | 0 |
| NB-00302 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_bid_package_milestone.py` | 6 | 5 | 1 | 0 |
| NB-00303 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cco.py` | 6 | 8 | 1 | 0 |
| NB-00304 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_change_order.py` | 6 | 4 | 1 | 0 |
| NB-00305 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_change_order_description.py` | 6 | 9 | 1 | 0 |
| NB-00306 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_claiming_scheme.py` | 6 | 4 | 1 | 0 |
| NB-00307 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_claiming_scheme_step.py` | 6 | 4 | 1 | 0 |
| NB-00308 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_commodity.py` | 6 | 4 | 1 | 0 |
| NB-00309 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_component.py` | 6 | 5 | 1 | 0 |
| NB-00310 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract.py` | 6 | 10 | 1 | 0 |
| NB-00311 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_closeout_status.py` | 6 | 5 | 1 | 0 |
| NB-00312 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_closeout_type.py` | 6 | 5 | 1 | 0 |
| NB-00313 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_detail_type.py` | 6 | 5 | 1 | 0 |
| NB-00314 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_line.py` | 6 | 10 | 1 | 0 |
| NB-00315 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_responsibility.py` | 6 | 8 | 1 | 0 |
| NB-00316 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_schedule_of_values.py` | 6 | 5 | 1 | 0 |
| NB-00317 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_term.py` | 6 | 7 | 1 | 0 |
| NB-00318 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_type_hierarchy.py` | 6 | 5 | 1 | 0 |
| NB-00319 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_contract_vco.py` | 6 | 13 | 1 | 0 |
| NB-00320 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cor.py` | 6 | 8 | 1 | 0 |
| NB-00321 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_category.py` | 6 | 7 | 1 | 0 |
| NB-00322 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_item.py` | 6 | 8 | 1 | 0 |
| NB-00323 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_cost_item_characteristic_type_list.py` | 6 | 7 | 1 | 0 |
| NB-00324 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_craft.py` | 6 | 4 | 1 | 0 |
| NB-00325 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_daily_plan.py` | 6 | 4 | 1 | 0 |
| NB-00326 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_discipline.py` | 6 | 5 | 1 | 0 |
| NB-00327 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_diversity_category.py` | 6 | 5 | 1 | 0 |
| NB-00328 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_document_rfi_report.py` | 6 | 5 | 1 | 0 |
| NB-00329 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_document_set_report.py` | 6 | 5 | 1 | 0 |
| NB-00330 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_document_submittal.py` | 6 | 5 | 1 | 0 |
| NB-00331 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_document_workflow_history.py` | 6 | 5 | 1 | 0 |
| NB-00332 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forcast_notes.py` | 6 | 9 | 1 | 0 |
| NB-00333 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forecast_method.py` | 6 | 5 | 1 | 0 |
| NB-00334 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_forecast_snapshot.py` | 6 | 5 | 1 | 0 |
| NB-00335 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_invoice.py` | 6 | 7 | 1 | 0 |
| NB-00336 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_invoice_payment_method.py` | 6 | 5 | 1 | 0 |
| NB-00337 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_issue.py` | 6 | 7 | 1 | 0 |
| NB-00338 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_pay_item.py` | 6 | 5 | 1 | 0 |
| NB-00339 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_risk_mitigation_plan.py` | 6 | 5 | 1 | 0 |
| NB-00340 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_time.py` | 6 | 3 | 1 | 0 |
| NB-00341 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_time_card.py` | 6 | 4 | 1 | 0 |
| NB-00342 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_trade.py` | 6 | 4 | 1 | 0 |
| NB-00343 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_union.py` | 6 | 4 | 1 | 0 |
| NB-00344 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_unit_of_measure.py` | 6 | 5 | 1 | 0 |
| NB-00345 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_user.py` | 6 | 6 | 1 | 0 |
| NB-00346 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_wbs.py` | 6 | 8 | 1 | 0 |
| NB-00347 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_dim_work_package.py` | 6 | 5 | 1 | 0 |
| NB-00348 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_actuals.py` | 6 | 14 | 1 | 0 |
| NB-00349 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_actuals_lod_9.py` | 6 | 14 | 1 | 0 |
| NB-00350 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_bid_package.py` | 6 | 11 | 1 | 0 |
| NB-00351 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_bid_package_milestone.py` | 6 | 7 | 1 | 0 |
| NB-00352 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_budget_log.py` | 6 | 29 | 1 | 0 |
| NB-00353 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_cco_log.py` | 6 | 9 | 1 | 0 |
| NB-00354 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_cost.py` | 6 | 13 | 1 | 0 |
| NB-00355 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_detail.py` | 6 | 8 | 1 | 0 |
| NB-00356 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_change_order_pay_item.py` | 6 | 8 | 1 | 0 |
| NB-00357 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_committed_cost_summary.py` | 6 | 9 | 1 | 0 |
| NB-00358 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_claim_history.py` | 6 | 12 | 1 | 0 |
| NB-00359 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_closeout.py` | 6 | 10 | 1 | 0 |
| NB-00360 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_cost_item_pricing.py` | 6 | 10 | 1 | 0 |
| NB-00361 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_diversity.py` | 6 | 11 | 1 | 0 |
| NB-00362 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_line.py` | 6 | 25 | 1 | 0 |
| NB-00363 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_schedule_of_values.py` | 6 | 14 | 1 | 0 |
| NB-00364 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_contract_vco_line.py` | 6 | 14 | 1 | 0 |
| NB-00365 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_control_budget.py` | 6 | 12 | 1 | 0 |
| NB-00366 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_cor_log.py` | 6 | 8 | 1 | 0 |
| NB-00367 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_plan_detail.py` | 6 | 17 | 1 | 0 |
| NB-00368 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_plan_summary.py` | 6 | 4 | 1 | 0 |
| NB-00369 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_current_project_forecast.py` | 6 | 12 | 1 | 0 |
| NB-00370 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_daily_plan_notes.py` | 6 | 7 | 1 | 0 |
| NB-00371 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_daily_plan_quantity.py` | 6 | 15 | 1 | 0 |
| NB-00372 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_document.py` | 6 | 21 | 1 | 0 |
| NB-00373 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_estimates.py` | 6 | 9 | 1 | 0 |
| NB-00374 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_forcast.py` | 6 | 11 | 1 | 0 |
| NB-00375 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_invoice_line.py` | 6 | 10 | 1 | 0 |
| NB-00376 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_invoice_payment.py` | 6 | 12 | 1 | 0 |
| NB-00377 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_issues_log.py` | 6 | 9 | 1 | 0 |
| NB-00378 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_pay_item.py` | 6 | 9 | 1 | 0 |
| NB-00379 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_pay_item_earning.py` | 6 | 10 | 1 | 0 |
| NB-00380 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_quantity_claim.py` | 6 | 17 | 1 | 0 |
| NB-00381 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_time_card.py` | 6 | 16 | 1 | 0 |
| NB-00382 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_work_package.py` | 6 | 6 | 1 | 0 |
| NB-00383 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_fact_wp_component_progress.py` | 6 | 14 | 1 | 0 |
| NB-00384 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_project_employee_role.py` | 6 | 7 | 1 | 0 |
| NB-00385 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_ref_bid_package_document.py` | 6 | 9 | 1 | 0 |
| NB-00386 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_ref_contract_document.py` | 6 | 9 | 1 | 0 |
| NB-00387 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_sat_current_budget_cost_item_category.py` | 6 | 8 | 1 | 0 |
| NB-00388 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_sat_original_budget_cost_item_category.py` | 6 | 8 | 1 | 0 |
| NB-00389 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_plan_actuals_detail_v.py` | 6 | 9 | 1 | 0 |
| NB-00390 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_plan_actuals_summary_v.py` | 6 | 9 | 1 | 0 |
| NB-00391 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_current_project_forecast_detail_v.py` | 6 | 8 | 1 | 0 |
| NB-00392 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_fact_invoice_payment_progress_v.py` | 6 | 10 | 1 | 0 |
| NB-00393 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_project_cost_code_employee_labor_allocation.py` | 6 | 10 | 1 | 0 |
| NB-00394 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_rpt_contract_line_exception_v.py` | 6 | 13 | 1 | 0 |
| NB-00395 | 300_silver_to_gold | project_management | `notebooks/data_engineering/300_silver_to_gold/project_management/silver_to_gold_vw_rpt_contract_original_exception_v.py` | 6 | 8 | 1 | 0 |
| NB-00396 | 300_silver_to_gold | project_mgmt_core | `notebooks/data_engineering/300_silver_to_gold/project_mgmt_core/silver_to_gold_dim_acs.py` | 6 | 5 | 1 | 0 |
| NB-00397 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_budget.py` | 6 | 7 | 1 | 0 |
| NB-00398 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_change_order_requests.py` | 6 | 9 | 1 | 0 |
| NB-00399 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contactlist_by_project_number.py` | 6 | 10 | 1 | 0 |
| NB-00400 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contract_sched_values.py` | 6 | 8 | 1 | 0 |
| NB-00401 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_contracts.py` | 6 | 8 | 1 | 0 |
| NB-00402 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_daily_reports.py` | 6 | 12 | 1 | 0 |
| NB-00403 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_fieldpo.py` | 6 | 8 | 1 | 0 |
| NB-00404 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_pccos.py` | 6 | 7 | 1 | 0 |
| NB-00405 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_potential_change_orders.py` | 6 | 8 | 1 | 0 |
| NB-00406 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_potential_changeorder_lineitems.py` | 6 | 8 | 1 | 0 |
| NB-00407 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_projects_assigned_roles.py` | 6 | 11 | 1 | 0 |
| NB-00408 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_request_for_information.py` | 6 | 10 | 1 | 0 |
| NB-00409 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_safety.py` | 6 | 9 | 1 | 0 |
| NB-00410 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_sub_contract_changeorder.py` | 6 | 9 | 1 | 0 |
| NB-00411 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_submittal_reviewers.py` | 6 | 10 | 1 | 0 |
| NB-00412 | 300_silver_to_gold | prolog | `notebooks/data_engineering/300_silver_to_gold/prolog/silver_to_gold_prolog_submittals.py` | 6 | 13 | 1 | 0 |
| NB-00413 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_body_part.py` | 6 | 3 | 1 | 0 |
| NB-00414 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_compliance_user.py` | 6 | 5 | 1 | 0 |
| NB-00415 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_form.py` | 6 | 6 | 1 | 0 |
| NB-00416 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_form_location.py` | 6 | 4 | 1 | 0 |
| NB-00417 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_ineight_org_hierarchy.py` | 6 | 11 | 1 | 0 |
| NB-00418 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_ineight_project_hierarchy.py` | 6 | 7 | 1 | 0 |
| NB-00419 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_injury_cause.py` | 6 | 4 | 1 | 0 |
| NB-00420 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_injury_cause_hierarchy.py` | 6 | 5 | 1 | 0 |
| NB-00421 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_obs_project.py` | 6 | 8 | 1 | 0 |
| NB-00422 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_org_project_bu.py` | 6 | 9 | 1 | 0 |
| NB-00423 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_reporter_and_assignor.py` | 6 | 4 | 1 | 0 |
| NB-00424 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_role.py` | 6 | 6 | 1 | 0 |
| NB-00425 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_safety_form.py` | 6 | 8 | 1 | 0 |
| NB-00426 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_status.py` | 6 | 4 | 1 | 0 |
| NB-00427 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_stcky_bucket.py` | 6 | 4 | 1 | 0 |
| NB-00428 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_dim_stcky_role.py` | 6 | 4 | 1 | 0 |
| NB-00429 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_recognition.py` | 6 | 5 | 1 | 0 |
| NB-00430 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_suggestion_box.py` | 6 | 5 | 1 | 0 |
| NB-00431 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_cvis_walk.py` | 6 | 8 | 1 | 0 |
| NB-00432 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_event_task.py` | 6 | 25 | 1 | 0 |
| NB-00433 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_incident.py` | 6 | 12 | 1 | 0 |
| NB-00434 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_psli.py` | 6 | 5 | 1 | 0 |
| NB-00435 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_safety_event_task.py` | 6 | 5 | 1 | 0 |
| NB-00436 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_stcky_walk.py` | 6 | 10 | 1 | 0 |
| NB-00437 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_fact_stcky_walk_missing_protection_reason.py` | 6 | 10 | 1 | 0 |
| NB-00438 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_dim_org_project_bu_safety.py` | 6 | 4 | 1 | 0 |
| NB-00439 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_recognition_action_area.py` | 6 | 5 | 1 | 0 |
| NB-00440 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_recognition_award_type.py` | 6 | 5 | 1 | 0 |
| NB-00441 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_walk_corr_action.py` | 6 | 5 | 1 | 0 |
| NB-00442 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_cvis_walk_protection.py` | 6 | 6 | 1 | 0 |
| NB-00443 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_body_part.py` | 6 | 5 | 1 | 0 |
| NB-00444 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_category.py` | 6 | 5 | 1 | 0 |
| NB-00445 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_damage.py` | 6 | 5 | 1 | 0 |
| NB-00446 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_estimated_loss.py` | 6 | 5 | 1 | 0 |
| NB-00447 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_equip_crane_owner.py` | 6 | 5 | 1 | 0 |
| NB-00448 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_event.py` | 6 | 6 | 1 | 0 |
| NB-00449 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_first_aid_provider.py` | 6 | 5 | 1 | 0 |
| NB-00450 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_classification.py` | 6 | 5 | 1 | 0 |
| NB-00451 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_main_cause.py` | 6 | 7 | 1 | 0 |
| NB-00452 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_injury_type.py` | 6 | 5 | 1 | 0 |
| NB-00453 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_medical_treatment.py` | 6 | 5 | 1 | 0 |
| NB-00454 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_medical_treatment_provider.py` | 6 | 5 | 1 | 0 |
| NB-00455 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_utility_info.py` | 6 | 5 | 1 | 0 |
| NB-00456 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incident_utility_pivots.py` | 6 | 5 | 1 | 0 |
| NB-00457 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_incidents_event_task.py` | 6 | 7 | 1 | 0 |
| NB-00458 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_labor_hours_by_project_monthly.py` | 6 | 6 | 1 | 0 |
| NB-00459 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_other_event_task.py` | 6 | 7 | 1 | 0 |
| NB-00460 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_psli_event_task.py` | 6 | 5 | 1 | 0 |
| NB-00461 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_svis_event_task.py` | 6 | 7 | 1 | 0 |
| NB-00462 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_walk_corr_action.py` | 6 | 5 | 1 | 0 |
| NB-00463 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_stcky_walk_protection.py` | 6 | 6 | 1 | 0 |
| NB-00464 | 300_silver_to_gold | safety | `notebooks/data_engineering/300_silver_to_gold/safety/silver_to_gold_vw_fact_subcontractor_labor_hours_by_project_monthly.py` | 6 | 5 | 1 | 0 |
| NB-00465 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_activity_code.py` | 6 | 11 | 1 | 0 |
| NB-00466 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_float_criteria.py` | 6 | 3 | 1 | 0 |
| NB-00467 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_group.py` | 6 | 4 | 1 | 0 |
| NB-00468 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_predecessor_task.py` | 6 | 17 | 1 | 0 |
| NB-00469 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_successor_task.py` | 6 | 13 | 1 | 0 |
| NB-00470 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_task.py` | 6 | 10 | 1 | 0 |
| NB-00471 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_dim_wbs.py` | 6 | 11 | 1 | 0 |
| NB-00472 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_fact_project_schedule_stats.py` | 6 | 5 | 1 | 0 |
| NB-00473 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_fact_task.py` | 6 | 20 | 1 | 0 |
| NB-00474 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_fact_task_float_trend_weekly.py` | 6 | 9 | 1 | 0 |
| NB-00475 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_average_daily_labor.py` | 6 | 6 | 1 | 0 |
| NB-00476 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_average_daily_labor_by_date.py` | 6 | 6 | 1 | 0 |
| NB-00477 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_task_current.py` | 6 | 5 | 1 | 0 |
| NB-00478 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_task_current_max_week.py` | 6 | 8 | 1 | 0 |
| NB-00479 | 300_silver_to_gold | schedule | `notebooks/data_engineering/300_silver_to_gold/schedule/silver_to_gold_vw_fact_task_float_trend_project_weekly.py` | 6 | 7 | 1 | 0 |
| NB-00480 | 300_silver_to_gold | schedule_validator | `notebooks/data_engineering/300_silver_to_gold/schedule_validator/silver_to_gold_vw_schedule_validator_project_current.py` | 6 | 5 | 1 | 0 |
| NB-00481 | 300_silver_to_gold | schedule_validator | `notebooks/data_engineering/300_silver_to_gold/schedule_validator/silver_to_gold_vw_schedule_validator_project_snapshots.py` | 6 | 6 | 1 | 0 |
| NB-00482 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_bridge_user_project_relationship.py` | 8 | 8 | 1 | 0 |
| NB-00483 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_dim_active_directory_user.py` | 8 | 19 | 1 | 0 |
| NB-00484 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_ref_user_project_role.py` | 6 | 14 | 1 | 0 |
| NB-00485 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cosential_opportunity_relationship.py` | 8 | 12 | 1 | 0 |
| NB-00486 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cosential_project_relationship.py` | 8 | 12 | 1 | 0 |
| NB-00487 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_cost_code_relationship.py` | 8 | 17 | 1 | 0 |
| NB-00488 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_defined_permission_override.py` | 8 | 10 | 1 | 0 |
| NB-00489 | 300_silver_to_gold | security | `notebooks/data_engineering/300_silver_to_gold/security/silver_to_gold_stg_user_project_relationship.py` | 8 | 26 | 1 | 0 |
| NB-00490 | 300_silver_to_gold | master | `notebooks/data_engineering/300_silver_to_gold/silver_to_gold_master.py` | 5 | 0 | 0 | 1 |
| NB-00491 | 300_silver_to_gold | support_financials | `notebooks/data_engineering/300_silver_to_gold/support_financials/silver_to_gold_fact_it_actuals.py` | 6 | 6 | 1 | 0 |
| NB-00492 | 300_silver_to_gold | support_financials | `notebooks/data_engineering/300_silver_to_gold/support_financials/silver_to_gold_fact_it_budget.py` | 6 | 6 | 1 | 0 |
| NB-00493 | 300_silver_to_gold | templates | `notebooks/data_engineering/300_silver_to_gold/templates/hello_world.py` | 6 | 3 | 1 | 0 |
| NB-00494 | 300_silver_to_gold | templates | `notebooks/data_engineering/300_silver_to_gold/templates/silver_to_gold_dim_template.py` | 6 | 7 | 1 | 0 |
| NB-00495 | 300_silver_to_gold | templates | `notebooks/data_engineering/300_silver_to_gold/templates/silver_to_gold_fact_incremental.py` | 6 | 8 | 1 | 0 |
| NB-00496 | 300_silver_to_gold | templates | `notebooks/data_engineering/300_silver_to_gold/templates/silver_to_gold_fact_template.py` | 6 | 6 | 1 | 0 |
| NB-00497 | 300_silver_to_gold | templates | `notebooks/data_engineering/300_silver_to_gold/templates/silver_to_gold_vw_template.py` | 6 | 6 | 1 | 0 |
| NB-00498 | 300_silver_to_gold | tradetapp | `notebooks/data_engineering/300_silver_to_gold/tradetapp/silver_to_gold_subcontractor_qualification.py` | 8 | 10 | 1 | 0 |
| NB-00499 | 300_silver_to_gold | user_communication | `notebooks/data_engineering/300_silver_to_gold/user_communication/silver_to_gold_data_warehouse_release_notes.py` | 6 | 5 | 1 | 0 |
| NB-00500 | 300_silver_to_gold | vairkko | `notebooks/data_engineering/300_silver_to_gold/vairkko/silver_to_gold_vairkko_dim_users.py` | 6 | 5 | 1 | 0 |
| NB-00501 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_dim_pbi_report.py` | 6 | 4 | 1 | 0 |
| NB-00502 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_dim_pbi_workspace.py` | 6 | 4 | 1 | 0 |
| NB-00503 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_fact_pbi_user_avtivity.py` | 6 | 14 | 1 | 0 |
| NB-00504 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/silver_to_gold_project_notes_export.py` | 6 | 5 | 1 | 0 |
| NB-00505 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_company_export.py` | 6 | 8 | 1 | 0 |
| NB-00506 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_pbi_datasets_export.py` | 6 | 13 | 4 | 0 |
| NB-00507 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_user_menu_export.py` | 6 | 7 | 1 | 0 |
| NB-00508 | 300_silver_to_gold | web_app_integration | `notebooks/data_engineering/300_silver_to_gold/web_app_integration/web_app_workspace_report_export.py` | 6 | 12 | 1 | 0 |
| NB-00509 | 300_silver_to_gold | weld_office | `notebooks/data_engineering/300_silver_to_gold/weld_office/silver_to_gold_vw_wps_process_expiry_mapping.py` | 6 | 6 | 1 | 0 |
| NB-00510 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/backfill_fact_wpr_weekly.py` | 6 | 31 | 1 | 0 |
| NB-00511 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_account_balances.py` | 6 | 9 | 0 | 0 |
| NB-00512 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_cash_position.py` | 6 | 9 | 0 | 0 |
| NB-00513 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_fact_account_balance_monthly_detail.py` | 6 | 17 | 1 | 0 |
| NB-00514 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_fact_account_balance_monthly_header.py` | 6 | 26 | 1 | 0 |
| NB-00515 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_fact_equipment_account_balance_monthly.py` | 8 | 23 | 1 | 0 |
| NB-00516 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_monthly_subcontractor_hours_by_project.py` | 6 | 8 | 0 | 0 |
| NB-00517 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_project_billing.py` | 6 | 9 | 0 | 0 |
| NB-00518 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_weekly_labor_head_count.py` | 6 | 9 | 0 | 0 |
| NB-00519 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/e1_weekly_labor_hours_by_project.py` | 6 | 11 | 0 | 0 |
| NB-00520 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/emars_payroll.py` | 6 | 5 | 0 | 0 |
| NB-00521 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/p6_fact_task_float_trend_weekly.py` | 6 | 9 | 0 | 0 |
| NB-00522 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/silver_to_gold_fact_project_billing.py` | 6 | 11 | 1 | 0 |
| NB-00523 | 300_silver_to_gold | z_backfill | `notebooks/data_engineering/300_silver_to_gold/z_backfill/silver_to_gold_proforma_executive_summary.py` | 6 | 8 | 1 | 0 |
| NB-00524 | environment_promotion | clone_tables | `notebooks/data_engineering/environment_promotion/clone_tables/1 - clone_table_to_target_environment.py` | 0 | 2 | 0 | 0 |
| NB-00525 | environment_promotion | clone_tables | `notebooks/data_engineering/environment_promotion/clone_tables/2 - clone_table_to_target_environment - silver.py` | 0 | 2 | 0 | 0 |
| NB-00526 | environment_promotion | clone_tables | `notebooks/data_engineering/environment_promotion/clone_tables/3 - clone_table_to_target_environment - silver.py` | 0 | 1 | 0 | 0 |
| NB-00527 | environment_promotion | metadata_promotion_scripts | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/build_metadata_table.py` | 4 | 1 | 0 | 0 |
| NB-00528 | environment_promotion | metadata_promotion_scripts | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/promote_metadata_to_azuresql.py` | 0 | 7 | 1 | 0 |
| NB-00529 | environment_promotion | metadata_promotion_scripts | `notebooks/data_engineering/environment_promotion/metadata_promotion_scripts/run_adf_promote_metadata_pipeline.py` | 0 | 3 | 5 | 0 |
| NB-00530 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/Bug 8342_dim_project_is_business_unit.py` | 0 | 3 | 0 | 0 |
| NB-00531 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/Bug 9711_fact_account_balance.py` | 0 | 1 | 0 | 0 |
| NB-00532 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/Bug 9712_fact_weekly_labor_head_count.py` | 0 | 1 | 0 | 0 |
| NB-00533 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/Bug 9713_fact_deficiency.py` | 0 | 3 | 0 | 0 |
| NB-00534 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/Bug_6583_data_merge.py` | 0 | 4 | 0 | 0 |
| NB-00535 | environment_promotion | misc_scripts | `notebooks/data_engineering/environment_promotion/misc_scripts/data_process_for_bug_6583.py` | 1 | 6 | 0 | 0 |
| NB-00536 | environment_promotion | post_deployment_scripts | `notebooks/data_engineering/environment_promotion/post_deployment_scripts/20231109_maintain_dim_project_ineight_interface_indicator.py` | 6 | 3 | 0 | 0 |
| NB-00537 | environment_promotion | post_deployment_scripts | `notebooks/data_engineering/environment_promotion/post_deployment_scripts/placeholder.py` | 0 | 0 | 0 | 0 |
| NB-00538 | maintenance | maintenace | `notebooks/data_engineering/maintenance/maintenace_optimize_all_tables.py` | 3 | 1 | 0 | 0 |
| NB-00539 | maintenance | maintenace | `notebooks/data_engineering/maintenance/maintenace_update_p6_column_positions.py` | 0 | 7 | 0 | 0 |
| NB-00540 | maintenance | maintenance | `notebooks/data_engineering/maintenance/maintenance_define_schedulevalidator_schema.py` | 0 | 3 | 0 | 0 |
| NB-00541 | maintenance | maintenance | `notebooks/data_engineering/maintenance/maintenance_define_teambinder_form_schema.py` | 0 | 2 | 0 | 0 |
| NB-00542 | maintenance | maintenance | `notebooks/data_engineering/maintenance/maintenance_execute_notebooks_in_optimize_folder.py` | 0 | 0 | 2 | 1 |
| NB-00543 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_account_master.py` | 0 | 0 | 0 | 0 |
| NB-00544 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_dim_project.py` | 0 | 0 | 0 | 0 |
| NB-00545 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_e1_f060116.py` | 0 | 0 | 0 | 0 |
| NB-00546 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_e1_f08001.py` | 0 | 0 | 0 | 0 |
| NB-00547 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_project.py` | 0 | 0 | 0 | 0 |
| NB-00548 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_projwbs.py` | 0 | 0 | 0 | 0 |
| NB-00549 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_task.py` | 0 | 0 | 0 | 0 |
| NB-00550 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_taskactv.py` | 0 | 0 | 0 | 0 |
| NB-00551 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_taskrsrc.py` | 0 | 0 | 0 | 0 |
| NB-00552 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_tbl_sundt_api.py` | 0 | 0 | 0 | 0 |
| NB-00553 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_p6_tbl_sundt_api_weekly.py` | 0 | 0 | 0 | 0 |
| NB-00554 | maintenance | optimize_and_zorder | `notebooks/data_engineering/maintenance/optimize_and_zorder/maintenace_optimize_schedule_fact_task.py` | 0 | 0 | 0 | 0 |
| NB-00555 | maintenance | vacuum | `notebooks/data_engineering/maintenance/vacuum/maintenance_vacuum_all_tables.py` | 0 | 2 | 0 | 0 |
| NB-00556 | miscellaneous_scripts | alter | `notebooks/data_engineering/miscellaneous_scripts/alter_dim_project.py` | 0 | 2 | 0 | 0 |
| NB-00557 | miscellaneous_scripts | azure_cost_management_api_ | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_actualcost.py` | 8 | 5 | 4 | 0 |
| NB-00558 | miscellaneous_scripts | azure_cost_management_api_ | `notebooks/data_engineering/miscellaneous_scripts/azure_cost_management_api_/source_to_bronze_amortizedcost.py` | 8 | 5 | 4 | 0 |
| NB-00559 | miscellaneous_scripts | e1 | `notebooks/data_engineering/miscellaneous_scripts/bronze_to_silver_e1_f03b11_v.py` | 14 | 4 | 0 | 0 |
| NB-00560 | miscellaneous_scripts | fact | `notebooks/data_engineering/miscellaneous_scripts/fact_project_performance_snapshot_history_load_transportation.py` | 0 | 3 | 0 | 0 |
| NB-00561 | miscellaneous_scripts | raw | `notebooks/data_engineering/miscellaneous_scripts/raw_to_swat_files_all_sundt_foundation.py` | 8 | 4 | 0 | 0 |
| NB-00562 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_brdgit.py` | 6 | 10 | 1 | 0 |
| NB-00563 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_dim_timecard_v.py` | 6 | 4 | 1 | 0 |
| NB-00564 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_fact_current_plan_actuals_summary_v.py` | 6 | 9 | 1 | 0 |
| NB-00565 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_fact_current_plan_detail_v.py` | 6 | 17 | 1 | 0 |
| NB-00566 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_fact_current_plan_summary_v.py` | 6 | 4 | 1 | 0 |
| NB-00567 | miscellaneous_scripts | vw | `notebooks/data_engineering/miscellaneous_scripts/silver_to_gold_vw_fact_timecard_v.py` | 6 | 16 | 1 | 0 |
| NB-00568 | miscellaneous_scripts | source | `notebooks/data_engineering/miscellaneous_scripts/source_to_gold_autodesk_api_refresh_token.py` | 7 | 5 | 6 | 0 |
| NB-00569 | security | assign | `notebooks/data_engineering/security/assign_table_access.py` | 5 | 0 | 0 | 0 |
| NB-00570 | security | security | `notebooks/data_engineering/security/security_functions.py` | 0 | 2 | 0 | 0 |
| NB-00571 | startup | environment | `notebooks/data_engineering/startup/environment_startup.py` | 0 | 0 | 0 | 0 |
| NB-00572 | utility | common | `notebooks/data_engineering/utility/common_functions.py` | 0 | 16 | 0 | 0 |
| NB-00573 | utility | gold | `notebooks/data_engineering/utility/gold_table_processor.py` | 0 | 7 | 0 | 0 |
| NB-00574 | utility | insert | `notebooks/data_engineering/utility/insert_silver_to_gold_metadata.py` | 16 | 3 | 2 | 0 |
| NB-00575 | utility | jdbc | `notebooks/data_engineering/utility/jdbc_sql_server.py` | 0 | 5 | 3 | 0 |
| NB-00576 | utility | log | `notebooks/data_engineering/utility/log_operation_metrics.py` | 0 | 1 | 1 | 0 |
| NB-00577 | utility | nano | `notebooks/data_engineering/utility/nano_second_timer.py` | 0 | 0 | 0 | 0 |
| NB-00578 | utility | odbc | `notebooks/data_engineering/utility/odbc_sql_server.py` | 0 | 10 | 0 | 0 |
| NB-00579 | utility | recursive | `notebooks/data_engineering/utility/recursive_query_processor.py` | 0 | 2 | 0 | 0 |
| NB-00580 | utility | recursive | `notebooks/data_engineering/utility/recursive_query_processor_v2.py` | 0 | 2 | 0 | 0 |
| NB-00581 | utility | user | `notebooks/data_engineering/utility/user_defined_functions.py` | 0 | 3 | 0 | 0 |

## Required validation

- Confirm whether each notebook is deployed, scheduled, active, obsolete, or duplicate.
- Reconcile generated table and path references with runtime lineage.
- Assign owner, support group, classification, and modernization disposition.
- Promote validated records into domain architecture packages.
