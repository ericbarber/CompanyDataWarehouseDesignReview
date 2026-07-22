# ADF Orchestration Catalog

Generated from `DW2023-DataFactory` on 2026-07-22.

This catalog treats Azure Data Factory as current-state orchestration evidence only. The target direction is to migrate orchestration into Databricks-native jobs while preserving the complete source-to-consumer flow semantics.

## Summary

| Artifact | Count |
|---|---:|
| Pipelines | 118 |
| Schedule triggers | 35 |
| Datasets | 22 |
| Linked services | 24 |
| Integration runtimes | 2 |

## Activity types

| Activity type | Count |
|---|---:|
| ExecutePipeline | 558 |
| SqlServerStoredProcedure | 503 |
| SetVariable | 245 |
| Lookup | 146 |
| Copy | 73 |
| ForEach | 71 |
| IfCondition | 64 |
| DatabricksNotebook | 54 |
| WebActivity | 54 |
| DatabricksJob | 25 |
| Switch | 7 |
| Wait | 4 |
| Filter | 4 |
| Until | 1 |
| GetMetadata | 1 |

## Resource types

| Resource type | Count |
|---|---:|
| dataset:Binary | 5 |
| dataset:DelimitedText | 4 |
| dataset:AzureSqlTable | 4 |
| linkedService:AzureSqlDatabase | 4 |
| dataset:RestResource | 3 |
| linkedService:AzureDatabricks | 3 |
| linkedService:AzureKeyVault | 3 |
| linkedService:RestService | 3 |
| dataset:SqlServerTable | 2 |
| linkedService:FileServer | 2 |
| linkedService:Sftp | 2 |
| linkedService:AzureBlobFS | 2 |
| linkedService:SqlServer | 2 |
| dataset:Excel | 1 |
| dataset:Json | 1 |
| dataset:Parquet | 1 |
| dataset:SharePointOnlineListResource | 1 |
| linkedService:Spark | 1 |
| linkedService:HttpServer | 1 |
| linkedService:SharePointOnlineList | 1 |
| integrationRuntime:Managed | 1 |
| integrationRuntime:SelfHosted | 1 |
| credential:ServicePrincipal | 1 |

## Trigger index

| ID | Trigger | State | Schedule | Pipelines |
|---|---|---|---|---|
| ADF-TRG-00001 | `DEV_Bridgit_Reporting` | Started | Week every 1 US Mountain Standard Time | `plSourceToGoldBridgit_Reporting`<br>`plSourceToSilverRestApi_Procore`<br>`plSourceToSilverSmartPm` |
| ADF-TRG-00002 | `DEV_INEIGHT_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00003 | `DEV_INEIGHT_DOCS_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00004 | `DEV_INEIGHT_DOCS_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00005 | `DEV_INEIGHT_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00006 | `DEV_MonthlyMaintenance` | Started | Month every 1 Pacific Standard Time | `plMonthlyMaintenance` |
| ADF-TRG-00007 | `DEV_Security` | Stopped | Hour every 4 Greenwich Standard Time | `plWebAppUpdateSecurityAndWebAppIntegration` |
| ADF-TRG-00008 | `DEV_TEXTURA` | Started | Week every 1 US Mountain Standard Time | `plSourceToGoldTextura` |
| ADF-TRG-00009 | `DEV_Weekly` | Started | Week every 1 US Mountain Standard Time | `plSourceToGold` |
| ADF-TRG-00010 | `DEV_WeldOffice_weekly` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToGoldWeldOffice` |
| ADF-TRG-00011 | `DEV_cslb_weekly` | Started | Week every 1 US Mountain Standard Time | `plSourceToSilverCslb` |
| ADF-TRG-00012 | `DEV_zip_monthly` | Started | Month every 1 US Mountain Standard Time | `plSourceToSilverZipcodes` |
| ADF-TRG-00013 | `PROD_Bridgit_Reporting` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToGoldBridgit_Reporting`<br>`plSourceToSilverRestApi_Procore`<br>`plSourceToSilverSmartPm` |
| ADF-TRG-00014 | `PROD_Daily` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGold` |
| ADF-TRG-00015 | `PROD_INEIGHT_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00016 | `PROD_INEIGHT_DOCS_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00017 | `PROD_INEIGHT_DOCS_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00018 | `PROD_INEIGHT_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00019 | `PROD_MonthlyMaintenance` | Stopped | Month every 1 Pacific Standard Time | `plMonthlyMaintenance` |
| ADF-TRG-00020 | `PROD_TEXTURA` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldTextura` |
| ADF-TRG-00021 | `PROD_WeldOffice_weekly` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToGoldWeldOffice` |
| ADF-TRG-00022 | `PROD_cslb_weekly` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToSilverCslb` |
| ADF-TRG-00023 | `PROD_dailyHeavyJob` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldHeavyJob` |
| ADF-TRG-00024 | `PROD_zip_monthly` | Stopped | Month every 1 US Mountain Standard Time | `plSourceToSilverZipcodes` |
| ADF-TRG-00025 | `TEST_Bridgit_Reporting` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToGoldBridgit_Reporting`<br>`plSourceToSilverRestApi_Procore`<br>`plSourceToSilverSmartPm` |
| ADF-TRG-00026 | `TEST_INEIGHT_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00027 | `TEST_INEIGHT_DOCS_AM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00028 | `TEST_INEIGHT_DOCS_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneightDocument` |
| ADF-TRG-00029 | `TEST_INEIGHT_PM` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldIneight` |
| ADF-TRG-00030 | `TEST_MonthlyMaintenance` | Stopped | Month every 1 Pacific Standard Time | `plMonthlyMaintenance` |
| ADF-TRG-00031 | `TEST_TEXTURA` | Stopped | Day every 1 US Mountain Standard Time | `plSourceToGoldTextura` |
| ADF-TRG-00032 | `TEST_Weekly` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToGold` |
| ADF-TRG-00033 | `TEST_WeldOffice_weekly` | Stopped | Week every 15 US Mountain Standard Time | `plSourceToGoldWeldOffice` |
| ADF-TRG-00034 | `TEST_cslb_weekly` | Stopped | Week every 1 US Mountain Standard Time | `plSourceToSilverCslb` |
| ADF-TRG-00035 | `TEST_zip_monthly` | Stopped | Month every 1 US Mountain Standard Time | `plSourceToSilverZipcodes` |

## Pipeline index

| ID | Pipeline | Activities | Key activity types | Calls pipelines | Databricks notebooks | Linked services | Datasets |
|---|---|---:|---|---:|---:|---:|---:|
| ADF-PL-00001 | `ArchiveClueFile` | 1 | Copy (1) | 0 | 0 | 0 | 1 |
| ADF-PL-00002 | `Demo Pipeline` | 1 | Wait (1) | 0 | 0 | 0 | 0 |
| ADF-PL-00003 | `plBronzeToSilver` | 15 | SqlServerStoredProcedure (6)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00004 | `plBronzeToSilverFullLoad` | 15 | SqlServerStoredProcedure (6)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00005 | `plBronzeToSilver_serverless` | 19 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00006 | `plCheckIfRunning` | 8 | Lookup (3)<br>Filter (2)<br>IfCondition (1)<br>SetVariable (1) | 0 | 0 | 1 | 1 |
| ADF-PL-00007 | `plCheckIfRunningAndStopShir` | 8 | Filter (2)<br>Lookup (2)<br>ExecutePipeline (1)<br>IfCondition (1) | 1 | 0 | 1 | 1 |
| ADF-PL-00008 | `plClusterTest01` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00009 | `plClusterTest02` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00010 | `plClusterTest03` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00011 | `plClusterTest04` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00012 | `plClusterTest05` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00013 | `plClusterTest06` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00014 | `plClusterTest07` | 3 | SqlServerStoredProcedure (2)<br>ExecutePipeline (1) | 1 | 0 | 1 | 0 |
| ADF-PL-00015 | `plCopyClue` | 19 | SetVariable (5)<br>ExecutePipeline (4)<br>SqlServerStoredProcedure (4)<br>Copy (2) | 1 | 0 | 1 | 2 |
| ADF-PL-00016 | `plFrequentWebAppAndPBIDatasetUpdates` | 16 | ExecutePipeline (14)<br>SqlServerStoredProcedure (2) | 8 | 0 | 1 | 0 |
| ADF-PL-00017 | `plLogMsgAndSendEmail` | 6 | IfCondition (2)<br>Lookup (2)<br>SqlServerStoredProcedure (1)<br>WebActivity (1) | 0 | 0 | 2 | 1 |
| ADF-PL-00018 | `plMdwToPbiChildWebAppRLSTables` | 25 | WebActivity (8)<br>SetVariable (7)<br>ExecutePipeline (4)<br>SqlServerStoredProcedure (2) | 1 | 0 | 2 | 0 |
| ADF-PL-00019 | `plMdwToPbiParentWebAppRLSTables` | 11 | ExecutePipeline (5)<br>SqlServerStoredProcedure (4)<br>ForEach (1)<br>Lookup (1) | 2 | 0 | 1 | 1 |
| ADF-PL-00020 | `plMonthlyMaintenance` | 6 | DatabricksNotebook (2)<br>ExecutePipeline (2)<br>SqlServerStoredProcedure (2) | 1 | 2 | 2 | 0 |
| ADF-PL-00021 | `plPromoteMetadata` | 20 | ExecutePipeline (8)<br>DatabricksNotebook (4)<br>SetVariable (4)<br>Copy (3) | 1 | 2 | 2 | 2 |
| ADF-PL-00022 | `plRowCountValidateSendEmail` | 4 | Lookup (2)<br>IfCondition (1)<br>WebActivity (1) | 0 | 0 | 1 | 1 |
| ADF-PL-00023 | `plSelfHostedIntegrationRuntime` | 9 | WebActivity (3)<br>IfCondition (2)<br>ForEach (1)<br>Lookup (1) | 0 | 0 | 1 | 1 |
| ADF-PL-00024 | `plSilverToGoldChild` | 15 | SqlServerStoredProcedure (6)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00025 | `plSilverToGoldChild_serverless` | 19 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00026 | `plSilverToGoldParent` | 11 | ExecutePipeline (5)<br>SqlServerStoredProcedure (4)<br>ForEach (1)<br>Lookup (1) | 2 | 0 | 1 | 1 |
| ADF-PL-00027 | `plSilverToGoldParent_serverless` | 11 | ExecutePipeline (5)<br>SqlServerStoredProcedure (4)<br>ForEach (1)<br>Lookup (1) | 2 | 0 | 1 | 1 |
| ADF-PL-00028 | `plSourceArchiveClueAll` | 4 | ExecutePipeline (1)<br>ForEach (1)<br>GetMetadata (1)<br>IfCondition (1) | 1 | 0 | 0 | 1 |
| ADF-PL-00029 | `plSourceToBronzeAsql` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 4 |
| ADF-PL-00030 | `plSourceToBronzeAsqlInEight` | 25 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Lookup (3)<br>Copy (2) | 2 | 1 | 2 | 4 |
| ADF-PL-00031 | `plSourceToBronzeAsqlInEight_serverless` | 31 | ExecutePipeline (7)<br>Lookup (6)<br>SetVariable (6)<br>SqlServerStoredProcedure (5) | 2 | 0 | 3 | 4 |
| ADF-PL-00032 | `plSourceToBronzeAsqlQdr` | 25 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Lookup (3)<br>Copy (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00033 | `plSourceToBronzeAsqlQdr_serverless` | 31 | ExecutePipeline (7)<br>Lookup (6)<br>SetVariable (6)<br>SqlServerStoredProcedure (5) | 2 | 0 | 3 | 3 |
| ADF-PL-00034 | `plSourceToBronzeAsqlSdatWebApp` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00035 | `plSourceToBronzeAsqlSdatWebApp_serverless` | 29 | ExecutePipeline (7)<br>SetVariable (6)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 3 |
| ADF-PL-00036 | `plSourceToBronzeAsql_serverless` | 29 | ExecutePipeline (7)<br>SetVariable (6)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 4 |
| ADF-PL-00037 | `plSourceToBronzeAsqlgng` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 4 |
| ADF-PL-00038 | `plSourceToBronzeAsqltimesheetApp` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 4 |
| ADF-PL-00039 | `plSourceToBronzeCslbLisence` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00040 | `plSourceToBronzeCslbLisence_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00041 | `plSourceToBronzeDropZoneCsv` | 17 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>Copy (2)<br>SetVariable (2) | 1 | 1 | 2 | 3 |
| ADF-PL-00042 | `plSourceToBronzeDropZoneXls` | 17 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>Copy (2)<br>SetVariable (2) | 1 | 1 | 2 | 3 |
| ADF-PL-00043 | `plSourceToBronzeFileSystemHeavyJob` | 20 | ExecutePipeline (6)<br>SqlServerStoredProcedure (6)<br>SetVariable (2)<br>Copy (1) | 2 | 1 | 3 | 3 |
| ADF-PL-00044 | `plSourceToBronzeFileSystemHeavyJob_serverless` | 25 | ExecutePipeline (6)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>Lookup (3) | 2 | 0 | 3 | 3 |
| ADF-PL-00045 | `plSourceToBronzeFileSystemWeldOffice` | 23 | SqlServerStoredProcedure (9)<br>ExecutePipeline (5)<br>Copy (2)<br>DatabricksNotebook (2) | 1 | 2 | 2 | 3 |
| ADF-PL-00046 | `plSourceToBronzeGraphQlApiAzureCostManagement` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00047 | `plSourceToBronzeGraphQlApiSiteSense` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00048 | `plSourceToBronzeRestApiAAD` | 22 | SqlServerStoredProcedure (6)<br>ExecutePipeline (5)<br>WebActivity (4)<br>Lookup (2) | 2 | 1 | 3 | 3 |
| ADF-PL-00049 | `plSourceToBronzeRestApiAAD_serverless` | 27 | ExecutePipeline (5)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>WebActivity (5) | 2 | 0 | 3 | 3 |
| ADF-PL-00050 | `plSourceToBronzeRestApiCosetial` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00051 | `plSourceToBronzeRestApiCosetial_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00052 | `plSourceToBronzeRestApiNccer` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00053 | `plSourceToBronzeRestApiNccer_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00054 | `plSourceToBronzeRestApiPbi` | 16 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>DatabricksNotebook (2)<br>SetVariable (2) | 1 | 2 | 2 | 1 |
| ADF-PL-00055 | `plSourceToBronzeRestApiPbiArchive` | 16 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>SetVariable (2)<br>Copy (1) | 1 | 1 | 2 | 3 |
| ADF-PL-00056 | `plSourceToBronzeRestApiPbi_serverless` | 21 | ExecutePipeline (5)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>DatabricksJob (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00057 | `plSourceToBronzeRestApiProcore` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00058 | `plSourceToBronzeRestApiScheduleValidator` | 14 | SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00059 | `plSourceToBronzeRestApiScheduleValidator_serverless` | 19 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00060 | `plSourceToBronzeRestApiTeamBinder` | 16 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>DatabricksNotebook (2)<br>SetVariable (2) | 1 | 2 | 2 | 1 |
| ADF-PL-00061 | `plSourceToBronzeRestApiTexura` | 14 | SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00062 | `plSourceToBronzeRestApiTradetapp` | 15 | SqlServerStoredProcedure (5)<br>ExecutePipeline (4)<br>DatabricksNotebook (2)<br>SetVariable (2) | 1 | 2 | 2 | 1 |
| ADF-PL-00063 | `plSourceToBronzeRestApiTradetapp_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00064 | `plSourceToBronzeRestApiVairkko` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00065 | `plSourceToBronzeRestApiVairkko_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00066 | `plSourceToBronzeRestApiVisionLink` | 16 | ExecutePipeline (5)<br>SqlServerStoredProcedure (5)<br>DatabricksNotebook (2)<br>SetVariable (2) | 1 | 2 | 2 | 1 |
| ADF-PL-00067 | `plSourceToBronzeSecureFileSystemClueAll` | 28 | ExecutePipeline (10)<br>SqlServerStoredProcedure (6)<br>SetVariable (5)<br>Copy (1) | 4 | 1 | 3 | 3 |
| ADF-PL-00068 | `plSourceToBronzeSecureFileSystemVRM` | 20 | ExecutePipeline (6)<br>SqlServerStoredProcedure (6)<br>SetVariable (2)<br>Copy (1) | 2 | 1 | 3 | 3 |
| ADF-PL-00069 | `plSourceToBronzeSecureFileSystemVRM_serverless` | 25 | ExecutePipeline (6)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>Lookup (3) | 2 | 0 | 3 | 3 |
| ADF-PL-00070 | `plSourceToBronzeSecureFileSystemzipcode` | 20 | ExecutePipeline (6)<br>SqlServerStoredProcedure (6)<br>SetVariable (2)<br>Copy (1) | 2 | 1 | 3 | 3 |
| ADF-PL-00071 | `plSourceToBronzeSecureFileSystemzipcode_serverless` | 25 | ExecutePipeline (6)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>Lookup (3) | 2 | 0 | 3 | 3 |
| ADF-PL-00072 | `plSourceToBronzeSharepoint` | 15 | SqlServerStoredProcedure (6)<br>ExecutePipeline (4)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00073 | `plSourceToBronzeSharepoint_serverless` | 22 | ExecutePipeline (5)<br>SetVariable (5)<br>SqlServerStoredProcedure (5)<br>Lookup (3) | 2 | 0 | 3 | 3 |
| ADF-PL-00074 | `plSourceToBronzeSoapApiB2G` | 14 | SqlServerStoredProcedure (6)<br>ExecutePipeline (3)<br>SetVariable (2)<br>DatabricksNotebook (1) | 1 | 1 | 2 | 1 |
| ADF-PL-00075 | `plSourceToBronzeSoapApiB2G_serverless` | 18 | SetVariable (5)<br>SqlServerStoredProcedure (5)<br>ExecutePipeline (3)<br>Lookup (2) | 1 | 0 | 3 | 1 |
| ADF-PL-00076 | `plSourceToBronzeSql` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00077 | `plSourceToBronzeSqlConcur` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00078 | `plSourceToBronzeSqlCosential` | 25 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Lookup (3)<br>Copy (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00079 | `plSourceToBronzeSqlCosential_serverless` | 31 | ExecutePipeline (7)<br>Lookup (6)<br>SetVariable (6)<br>SqlServerStoredProcedure (5) | 2 | 0 | 3 | 3 |
| ADF-PL-00080 | `plSourceToBronzeSqlDEstimator` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00081 | `plSourceToBronzeSqlDEstimator_serverless` | 29 | ExecutePipeline (7)<br>SetVariable (6)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 3 |
| ADF-PL-00082 | `plSourceToBronzeSqlE1` | 28 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>SetVariable (6)<br>Copy (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00083 | `plSourceToBronzeSqlE1_serverless` | 34 | SetVariable (10)<br>ExecutePipeline (7)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 3 |
| ADF-PL-00084 | `plSourceToBronzeSqlIneightDocument` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00085 | `plSourceToBronzeSqlIneightDocument_serverless` | 29 | ExecutePipeline (7)<br>SetVariable (6)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 3 |
| ADF-PL-00086 | `plSourceToBronzeSqlIneightEstimate` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00087 | `plSourceToBronzeSql_Referencedb` | 23 | ExecutePipeline (7)<br>SqlServerStoredProcedure (7)<br>Copy (2)<br>IfCondition (2) | 2 | 1 | 2 | 3 |
| ADF-PL-00088 | `plSourceToBronzeSql_serverless` | 29 | ExecutePipeline (7)<br>SetVariable (6)<br>SqlServerStoredProcedure (5)<br>Lookup (4) | 2 | 0 | 3 | 3 |
| ADF-PL-00089 | `plSourceToGold` | 19 | ExecutePipeline (10)<br>SetVariable (4)<br>SqlServerStoredProcedure (3)<br>IfCondition (1) | 10 | 0 | 1 | 0 |
| ADF-PL-00090 | `plSourceToGoldBridgit_Reporting` | 4 | ExecutePipeline (2)<br>DatabricksNotebook (1)<br>SqlServerStoredProcedure (1) | 1 | 1 | 2 | 0 |
| ADF-PL-00091 | `plSourceToGoldHeavyJob` | 7 | ExecutePipeline (4)<br>SqlServerStoredProcedure (3) | 4 | 0 | 1 | 0 |
| ADF-PL-00092 | `plSourceToGoldIneight` | 22 | ExecutePipeline (13)<br>SqlServerStoredProcedure (9) | 8 | 0 | 1 | 0 |
| ADF-PL-00093 | `plSourceToGoldIneightDocument` | 7 | SqlServerStoredProcedure (4)<br>ExecutePipeline (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00094 | `plSourceToGoldIneightDocument_serverless` | 7 | SqlServerStoredProcedure (4)<br>ExecutePipeline (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00095 | `plSourceToGoldIneight_serverless` | 22 | ExecutePipeline (13)<br>SqlServerStoredProcedure (9) | 8 | 0 | 1 | 0 |
| ADF-PL-00096 | `plSourceToGoldP6` | 6 | ExecutePipeline (3)<br>SqlServerStoredProcedure (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00097 | `plSourceToGoldSafety_TEMP` | 6 | ExecutePipeline (3)<br>SqlServerStoredProcedure (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00098 | `plSourceToGoldTextura` | 6 | ExecutePipeline (3)<br>SqlServerStoredProcedure (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00099 | `plSourceToGoldWeldOffice` | 6 | ExecutePipeline (3)<br>SqlServerStoredProcedure (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00100 | `plSourceToSilverAzureSql` | 10 | ExecutePipeline (7)<br>SqlServerStoredProcedure (3) | 7 | 0 | 1 | 0 |
| ADF-PL-00101 | `plSourceToSilverClue` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00102 | `plSourceToSilverCslb` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00103 | `plSourceToSilverGraphQl` | 7 | ExecutePipeline (4)<br>SqlServerStoredProcedure (3) | 3 | 0 | 1 | 0 |
| ADF-PL-00104 | `plSourceToSilverRestApi` | 21 | ExecutePipeline (18)<br>SqlServerStoredProcedure (3) | 10 | 0 | 1 | 0 |
| ADF-PL-00105 | `plSourceToSilverRestApi_Procore` | 4 | ExecutePipeline (2)<br>SqlServerStoredProcedure (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00106 | `plSourceToSilverSharepoint` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00107 | `plSourceToSilverSmartPm` | 4 | ExecutePipeline (2)<br>DatabricksNotebook (1)<br>SqlServerStoredProcedure (1) | 1 | 1 | 2 | 0 |
| ADF-PL-00108 | `plSourceToSilverSoapApi` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00109 | `plSourceToSilverSql` | 25 | ExecutePipeline (22)<br>SqlServerStoredProcedure (3) | 9 | 0 | 1 | 0 |
| ADF-PL-00110 | `plSourceToSilverVRM` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00111 | `plSourceToSilverZipcodes` | 5 | SqlServerStoredProcedure (3)<br>ExecutePipeline (2) | 2 | 0 | 1 | 0 |
| ADF-PL-00112 | `plUpdateAllWebAppTables` | 7 | ExecutePipeline (5)<br>SqlServerStoredProcedure (2) | 5 | 0 | 1 | 0 |
| ADF-PL-00113 | `plUpdateCompany` | 5 | SqlServerStoredProcedure (2)<br>Copy (1)<br>ExecutePipeline (1)<br>Lookup (1) | 1 | 0 | 1 | 2 |
| ADF-PL-00114 | `plUpdateDatasetId` | 5 | SqlServerStoredProcedure (2)<br>Copy (1)<br>ExecutePipeline (1)<br>Lookup (1) | 1 | 0 | 1 | 2 |
| ADF-PL-00115 | `plUpdatePBIDatasets` | 10 | ExecutePipeline (8)<br>SqlServerStoredProcedure (2) | 6 | 0 | 1 | 0 |
| ADF-PL-00116 | `plUpdateUserMenu` | 6 | Lookup (2)<br>SqlServerStoredProcedure (2)<br>Copy (1)<br>ExecutePipeline (1) | 1 | 0 | 1 | 2 |
| ADF-PL-00117 | `plUpdateWorkspace` | 6 | Lookup (2)<br>SqlServerStoredProcedure (2)<br>Copy (1)<br>ExecutePipeline (1) | 1 | 0 | 1 | 2 |
| ADF-PL-00118 | `plWebAppUpdateSecurityAndWebAppIntegration` | 16 | ExecutePipeline (14)<br>SqlServerStoredProcedure (2) | 9 | 0 | 1 | 0 |

## Required validation

- Confirm which triggers are active in production; repository `runtimeState` alone is not sufficient.
- Reconcile ADF pipeline definitions with Databricks Jobs, notebook paths, metadata tables, and runtime execution logs.
- Preserve operational semantics during migration: trigger cadence, dependency conditions, retries, alerts, logging, and restart behavior.
- Identify ADF-only connectors or integration runtimes that need a Databricks-native replacement pattern.
