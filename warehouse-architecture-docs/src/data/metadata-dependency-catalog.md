# Metadata Dependency Catalog

Generated from ADF pipeline query evidence on 2026-07-22.

This catalog identifies the Azure SQL metadata tables, query patterns, and `item().field` values that currently drive ADF fan-out, notebook paths, job IDs, source queries, and object-level processing behavior.

## Summary

| Metric | Count |
|---|---:|
| Metadata/query expressions | 140 |
| Distinct `item().field` references | 49 |
| Distinct metadata tables referenced | 6 |

## Metadata tables

| Table | Query count |
|---|---:|
| `adf.DataSource` | 62 |
| `adf.operationMetricLog` | 14 |
| `adf.azureResources` | 11 |
| `adf.powerBiDataset` | 2 |
| `adf.DataProcess` | 1 |
| `adf.DataProcessDependency` | 1 |

## Query categories

| Category | Query count |
|---|---:|
| Source metadata lookup | 62 |
| Per-object runtime query | 48 |
| Operational metrics lookup | 14 |
| Azure resource lookup | 11 |
| Other metadata query | 3 |
| Process metadata lookup | 1 |
| Process dependency lookup | 1 |

## High-use metadata fields

| Field | Uses | Pipelines | Sample expressions |
|---|---:|---:|---|
| `objectName` | 803 | 60 | `@item().objectName`<br>`@{replace(item().objectName,'_','')}_@{formatDateTime(variables('localTimestamp'), 'yyyy')}@{formatDateTime(variables('localTimestamp'), 'MM')}@{formatDateTi...`<br>`The clue file for @{item().objectName} had zero rows, therefore the file probably did not exist.` |
| `objectSchema` | 510 | 60 | `@item().objectSchema`<br>`@coalesce(item().sourceQuery, concat('SELECT * FROM ', item().objectSchema, '.', item().objectName))`<br>`SELECT * FROM @{item().objectSchema}.@{item().objectName} WHERE @{item().watermarkColumn} >= '@{item().watermarkValue}'` |
| `dataSourceId` | 337 | 60 | `@item().dataSourceId` |
| `dataSourceName` | 299 | 59 | `/@{item().dataSourceName}/@{item().objectName}/@{formatDateTime(variables('localTimestamp'), 'yyyy')}/@{formatDateTime(variables('localTimestamp'), 'MM')}/@{...`<br>`@item().dataSourceName`<br>`@{item().dataSourceName}/@{item().objectName}/@{formatDateTime(variables('localTimestamp'), 'yyyy')}/@{formatDateTime(variables('localTimestamp'), 'MM')}/@{f...` |
| `isIncremental` | 204 | 56 | `@string(item().isIncremental)`<br>`@item().isIncremental`<br>`<b>Row count validation failed</b> <b>Data Source Name:</b> @{item().dataSourceName} <b>Object Schema:</b> @{item().objectSchema} <b>Object Name:</b> @{item(...` |
| `IsIncremental` | 109 | 57 | `@string(item().IsIncremental)`<br>`@bool(item().IsIncremental)` |
| `primaryKeyColumns` | 68 | 62 | `@coalesce(item().primaryKeyColumns, '')`<br>`@coalesce(item().primaryKeyColumns,'')` |
| `description` | 63 | 57 | `@coalesce(item().description, '')` |
| `ObjectName` | 61 | 59 | `<b>Notebook:</b> /data_engineering/Source2Raw/Source2RawIncrementalLoad <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b...`<br>`<b>Notebook:</b> /Users/gpabbathi@sundt.com/Site_Sense_columns <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b> @{item(...`<br>`<b>Notebook:</b> /data_engineering/100_raw_to_bronze/raw_to_bronze <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b> @{i...` |
| `ObjectSchema` | 61 | 59 | `<b>Notebook:</b> /data_engineering/Source2Raw/Source2RawIncrementalLoad <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b...`<br>`<b>Notebook:</b> /Users/gpabbathi@sundt.com/Site_Sense_columns <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b> @{item(...`<br>`<b>Notebook:</b> /data_engineering/100_raw_to_bronze/raw_to_bronze <br><b>ObjectSchema: </b> @{coalesce(item().ObjectSchema, '')} <br><b>ObjectName: </b> @{i...` |
| `connectionSecretName` | 55 | 24 | `@item().connectionSecretName` |
| `destinationObjectName` | 43 | 5 | `@item().destinationObjectName`<br>`Notebook Failure: @{pipeline().Pipeline} for @{item().destinationObjectSchema}.@{item().destinationObjectName}`<br>`<b>Notebook:</b> @{item().dataProcessPathOrProcedure} <br><b>ObjectSchema: </b> @{item().destinationObjectSchema} <br><b>ObjectName: </b> @{item().destinatio...` |
| `destinationObjectSchema` | 43 | 5 | `@item().destinationObjectSchema`<br>`Notebook Failure: @{pipeline().Pipeline} for @{item().destinationObjectSchema}.@{item().destinationObjectName}`<br>`<b>Notebook:</b> @{item().dataProcessPathOrProcedure} <br><b>ObjectSchema: </b> @{item().destinationObjectSchema} <br><b>ObjectName: </b> @{item().destinatio...` |
| `sourceQuery` | 30 | 19 | `@coalesce(item().sourceQuery, concat('SELECT * FROM ', item().objectSchema, '.', item().objectName))`<br>`@coalesce(item().sourceQuery, activity('Remove special characters in column names').output.firstRow.Query)`<br>`@coalesce(item().sourceQuery, concat('SELECT * FROM ', item().objectSchema, '.', item().objectName), ' WHERE ', item().watermarkColumn, ' >= ', item().waterm...` |
| `dataProcessId` | 17 | 5 | `@item().dataProcessId` |
| `userName` | 14 | 8 | `@item().userName` |
| `databaseName` | 12 | 6 | `@item().databaseName` |
| `serverName` | 12 | 6 | `@item().serverName` |
| `watermarkColumn` | 11 | 11 | `SELECT * FROM @{item().objectSchema}.@{item().objectName} WHERE @{item().watermarkColumn} >= '@{item().watermarkValue}'`<br>`@coalesce(item().sourceQuery, concat('SELECT * FROM ', item().objectSchema, '.', item().objectName), ' WHERE ', item().watermarkColumn, ' >= ', item().waterm...`<br>`@concat(activity('Remove special characters in column names incremental').output.firstRow.Query, ' WHERE ''', item().watermarkColumn, ''', >= ', item().water...` |
| `watermarkValue` | 11 | 11 | `SELECT * FROM @{item().objectSchema}.@{item().objectName} WHERE @{item().watermarkColumn} >= '@{item().watermarkValue}'`<br>`@coalesce(item().sourceQuery, concat('SELECT * FROM ', item().objectSchema, '.', item().objectName), ' WHERE ', item().watermarkColumn, ' >= ', item().waterm...`<br>`@concat(activity('Remove special characters in column names incremental').output.firstRow.Query, ' WHERE ''', item().watermarkColumn, ''', >= ', item().water...` |
| `level` | 10 | 2 | `@item().level`<br>`Gold Child Pipeline Failure - Level @{item().level}`<br>`<b>Message:</b> The child pipeline failed for level: @{item().level} <br><b>Error Code: </b> @{activity('execute child pipeline').error.errorCode} <br><b>Err...` |
| `dataProcessPathOrProcedure` | 9 | 5 | `@item().dataProcessPathOrProcedure`<br>`<b>Notebook:</b> @{item().dataProcessPathOrProcedure} <br><b>ObjectSchema: </b> @{item().destinationObjectSchema} <br><b>ObjectName: </b> @{item().destinatio...`<br>`/data_engineering/@{item().dataProcessPathOrProcedure}` |
| `dataLakeEntityName` | 8 | 2 | `@item().dataLakeEntityName`<br>`@concat(item().dataLakePath,'/archive/', item().dataLakeEntityName, '/year-' ,string(formatDateTime(variables('utcTimestamp'),'yyyy')), '/month-' ,string(for...` |
| `dataLakePath` | 6 | 2 | `@item().dataLakePath`<br>`@concat(item().dataLakePath,'/archive/', item().dataLakeEntityName, '/year-' ,string(formatDateTime(variables('utcTimestamp'),'yyyy')), '/month-' ,string(for...` |
| `partitionBy` | 5 | 5 | `@coalesce(item().partitionBy, '')`<br>`@coalesce(item().partitionBy,'')` |
| `piiColumns` | 5 | 5 | `@coalesce(item().piiColumns, '')` |
| `dataLakeContainerName` | 4 | 2 | `@item().dataLakeContainerName` |
| `dataProcessID` | 3 | 3 | `@item().dataProcessID` |
| `projectIdColumn` | 3 | 3 | `@coalesce(item().projectIdColumn, '')` |
| `propertyValue` | 3 | 1 | `@concat(item().propertyValue,'/', item().resourceName, '/Stop?api-version=2022-03-01')`<br>`@concat(item().propertyValue,'/', item().resourceName, '/Start?api-version=2022-03-01')`<br>`@concat(item().propertyValue,'/', item().resourceName, '/InstanceView?api-version=2022-03-01')` |
| `relativePath` | 3 | 3 | `@item().relativePath`<br>`@if(equals(item().relativePath, null), 'https://sundtconstruction.sharepoint.com/sites/DatawarehouseFiles/',concat('https://sundtconstruction.sharepoint.com/...` |
| `resourceName` | 3 | 1 | `@concat(item().propertyValue,'/', item().resourceName, '/Stop?api-version=2022-03-01')`<br>`@concat(item().propertyValue,'/', item().resourceName, '/Start?api-version=2022-03-01')`<br>`@concat(item().propertyValue,'/', item().resourceName, '/InstanceView?api-version=2022-03-01')` |
| `silverIsSnapshot` | 3 | 3 | `@string(coalesce(item().silverIsSnapshot, ''))` |
| `silverJulianDateColumns` | 3 | 3 | `@coalesce(item().silverJulianDateColumns, '')` |
| `silverSnapshotPeriod` | 3 | 3 | `@coalesce(item().silverSnapshotPeriod, '')` |
| `basePath` | 2 | 2 | `@item().basePath` |
| `connectionsecretname` | 2 | 2 | `@item().connectionsecretname` |
| `excelSheetName` | 2 | 1 | `@item().excelSheetName` |
| `partitionCount` | 2 | 2 | `@string(coalesce(item().partitionCount, ''))` |
| `pipelineName` | 2 | 2 | `@and(less(item().runStart,addminutes(utcnow(), int(-3))), contains(item().pipelineName, pipeline().parameters.pipelineName))`<br>`@and(and(less(item().runStart,addminutes(utcnow(), int(-1))), contains(item().pipelineName, pipeline().parameters.pipelineName)), not(equals(item().pipelineN...` |

## Metadata query index

| ID | Pipeline | Category | Metadata tables | Source type filters | Item fields |
|---|---|---|---|---|---|
| META-QRY-00001 | `plCheckIfRunning` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00002 | `plCheckIfRunning` | Other metadata query | None detected | None detected | None detected |
| META-QRY-00003 | `plCheckIfRunning` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00004 | `plCheckIfRunningAndStopShir` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00005 | `plCheckIfRunningAndStopShir` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00006 | `plCopyClue` | Source metadata lookup | `adf.DataSource` | `SFTP File` | None detected |
| META-QRY-00007 | `plLogMsgAndSendEmail` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00008 | `plLogMsgAndSendEmail` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00009 | `plMdwToPbiParentWebAppRLSTables` | Other metadata query | `adf.powerBiDataset` | None detected | None detected |
| META-QRY-00010 | `plPromoteMetadata` | Process metadata lookup | `adf.DataProcess` | None detected | None detected |
| META-QRY-00011 | `plPromoteMetadata` | Source metadata lookup | `adf.DataSource` | None detected | None detected |
| META-QRY-00012 | `plPromoteMetadata` | Process dependency lookup | `adf.DataProcessDependency` | None detected | None detected |
| META-QRY-00013 | `plRowCountValidateSendEmail` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00014 | `plRowCountValidateSendEmail` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00015 | `plSelfHostedIntegrationRuntime` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00016 | `plSourceToBronzeAsql` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00017 | `plSourceToBronzeAsql` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00018 | `plSourceToBronzeAsql` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00019 | `plSourceToBronzeAsqlInEight` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00020 | `plSourceToBronzeAsqlInEight` | Per-object runtime query | None detected | None detected | `sourceQuery` |
| META-QRY-00021 | `plSourceToBronzeAsqlInEight` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00022 | `plSourceToBronzeAsqlInEight` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00023 | `plSourceToBronzeAsqlInEight_serverless` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00024 | `plSourceToBronzeAsqlInEight_serverless` | Per-object runtime query | None detected | None detected | `sourceQuery` |
| META-QRY-00025 | `plSourceToBronzeAsqlInEight_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00026 | `plSourceToBronzeAsqlInEight_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00027 | `plSourceToBronzeAsqlInEight_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00028 | `plSourceToBronzeAsqlQdr` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00029 | `plSourceToBronzeAsqlQdr` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00030 | `plSourceToBronzeAsqlQdr` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00031 | `plSourceToBronzeAsqlQdr_serverless` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00032 | `plSourceToBronzeAsqlQdr_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00033 | `plSourceToBronzeAsqlQdr_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00034 | `plSourceToBronzeAsqlQdr_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00035 | `plSourceToBronzeAsqlSdatWebApp` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database - SDAT Web App` | None detected |
| META-QRY-00036 | `plSourceToBronzeAsqlSdatWebApp` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00037 | `plSourceToBronzeAsqlSdatWebApp_serverless` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database - SDAT Web App` | None detected |
| META-QRY-00038 | `plSourceToBronzeAsqlSdatWebApp_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00039 | `plSourceToBronzeAsqlSdatWebApp_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00040 | `plSourceToBronzeAsql_serverless` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00041 | `plSourceToBronzeAsql_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00042 | `plSourceToBronzeAsql_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00043 | `plSourceToBronzeAsql_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00044 | `plSourceToBronzeAsqlgng` | Source metadata lookup | `adf.DataSource` | `Azure SQL Server` | None detected |
| META-QRY-00045 | `plSourceToBronzeAsqlgng` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00046 | `plSourceToBronzeAsqlgng` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00047 | `plSourceToBronzeAsqltimesheetApp` | Source metadata lookup | `adf.DataSource` | `Azure SQL Database` | None detected |
| META-QRY-00048 | `plSourceToBronzeAsqltimesheetApp` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00049 | `plSourceToBronzeAsqltimesheetApp` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00050 | `plSourceToBronzeCslbLisence` | Source metadata lookup | `adf.DataSource` | `API` | None detected |
| META-QRY-00051 | `plSourceToBronzeCslbLisence_serverless` | Source metadata lookup | `adf.DataSource` | `API` | None detected |
| META-QRY-00052 | `plSourceToBronzeDropZoneCsv` | Source metadata lookup | `adf.DataSource` | `drop-zone` | None detected |
| META-QRY-00053 | `plSourceToBronzeDropZoneXls` | Source metadata lookup | `adf.DataSource` | `drop-zone` | None detected |
| META-QRY-00054 | `plSourceToBronzeFileSystemHeavyJob` | Source metadata lookup | `adf.DataSource` | `File System` | None detected |
| META-QRY-00055 | `plSourceToBronzeFileSystemHeavyJob_serverless` | Source metadata lookup | `adf.DataSource` | `File System` | None detected |
| META-QRY-00056 | `plSourceToBronzeFileSystemHeavyJob_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00057 | `plSourceToBronzeFileSystemWeldOffice` | Source metadata lookup | `adf.DataSource` | `File System` | None detected |
| META-QRY-00058 | `plSourceToBronzeGraphQlApiAzureCostManagement` | Source metadata lookup | `adf.DataSource` | `GRAPHQL API` | None detected |
| META-QRY-00059 | `plSourceToBronzeGraphQlApiSiteSense` | Source metadata lookup | `adf.DataSource` | `GRAPHQL API` | None detected |
| META-QRY-00060 | `plSourceToBronzeRestApiAAD` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00061 | `plSourceToBronzeRestApiAAD` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00062 | `plSourceToBronzeRestApiAAD_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00063 | `plSourceToBronzeRestApiAAD_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00064 | `plSourceToBronzeRestApiAAD_serverless` | Azure resource lookup | `adf.azureResources` | None detected | None detected |
| META-QRY-00065 | `plSourceToBronzeRestApiCosetial` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00066 | `plSourceToBronzeRestApiCosetial_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00067 | `plSourceToBronzeRestApiNccer` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00068 | `plSourceToBronzeRestApiNccer_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00069 | `plSourceToBronzeRestApiPbi` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00070 | `plSourceToBronzeRestApiPbiArchive` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00071 | `plSourceToBronzeRestApiPbi_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00072 | `plSourceToBronzeRestApiProcore` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00073 | `plSourceToBronzeRestApiScheduleValidator` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00074 | `plSourceToBronzeRestApiScheduleValidator_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00075 | `plSourceToBronzeRestApiTeamBinder` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00076 | `plSourceToBronzeRestApiTexura` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00077 | `plSourceToBronzeRestApiTradetapp` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00078 | `plSourceToBronzeRestApiTradetapp_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00079 | `plSourceToBronzeRestApiVairkko` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00080 | `plSourceToBronzeRestApiVairkko_serverless` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00081 | `plSourceToBronzeRestApiVisionLink` | Source metadata lookup | `adf.DataSource` | `REST API` | None detected |
| META-QRY-00082 | `plSourceToBronzeSecureFileSystemClueAll` | Source metadata lookup | `adf.DataSource` | `SFTP File` | None detected |
| META-QRY-00083 | `plSourceToBronzeSecureFileSystemVRM` | Source metadata lookup | `adf.DataSource` | `File System` | None detected |
| META-QRY-00084 | `plSourceToBronzeSecureFileSystemVRM_serverless` | Source metadata lookup | `adf.DataSource` | `File System` | None detected |
| META-QRY-00085 | `plSourceToBronzeSecureFileSystemVRM_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00086 | `plSourceToBronzeSecureFileSystemzipcode` | Source metadata lookup | `adf.DataSource` | `SFTP File` | None detected |
| META-QRY-00087 | `plSourceToBronzeSecureFileSystemzipcode_serverless` | Source metadata lookup | `adf.DataSource` | `SFTP File` | None detected |
| META-QRY-00088 | `plSourceToBronzeSecureFileSystemzipcode_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00089 | `plSourceToBronzeSharepoint` | Source metadata lookup | `adf.DataSource` | `sharepoint list` | None detected |
| META-QRY-00090 | `plSourceToBronzeSharepoint_serverless` | Source metadata lookup | `adf.DataSource` | `sharepoint list` | None detected |
| META-QRY-00091 | `plSourceToBronzeSharepoint_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00092 | `plSourceToBronzeSoapApiB2G` | Source metadata lookup | `adf.DataSource` | `SOAP API` | None detected |
| META-QRY-00093 | `plSourceToBronzeSoapApiB2G_serverless` | Source metadata lookup | `adf.DataSource` | `SOAP API` | None detected |
| META-QRY-00094 | `plSourceToBronzeSql` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00095 | `plSourceToBronzeSql` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00096 | `plSourceToBronzeSql` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00097 | `plSourceToBronzeSqlConcur` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00098 | `plSourceToBronzeSqlConcur` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00099 | `plSourceToBronzeSqlConcur` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00100 | `plSourceToBronzeSqlCosential` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00101 | `plSourceToBronzeSqlCosential` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00102 | `plSourceToBronzeSqlCosential` | Per-object runtime query | None detected | None detected | `watermarkColumn`<br>`watermarkValue` |
| META-QRY-00103 | `plSourceToBronzeSqlCosential` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00104 | `plSourceToBronzeSqlCosential_serverless` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00105 | `plSourceToBronzeSqlCosential_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00106 | `plSourceToBronzeSqlCosential_serverless` | Per-object runtime query | None detected | None detected | `watermarkColumn`<br>`watermarkValue` |
| META-QRY-00107 | `plSourceToBronzeSqlCosential_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema` |
| META-QRY-00108 | `plSourceToBronzeSqlCosential_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00109 | `plSourceToBronzeSqlDEstimator` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00110 | `plSourceToBronzeSqlDEstimator` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00111 | `plSourceToBronzeSqlDEstimator` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00112 | `plSourceToBronzeSqlDEstimator_serverless` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00113 | `plSourceToBronzeSqlDEstimator_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00114 | `plSourceToBronzeSqlDEstimator_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00115 | `plSourceToBronzeSqlDEstimator_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00116 | `plSourceToBronzeSqlE1` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00117 | `plSourceToBronzeSqlE1` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00118 | `plSourceToBronzeSqlE1` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00119 | `plSourceToBronzeSqlE1_serverless` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00120 | `plSourceToBronzeSqlE1_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00121 | `plSourceToBronzeSqlE1_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00122 | `plSourceToBronzeSqlE1_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00123 | `plSourceToBronzeSqlIneightDocument` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00124 | `plSourceToBronzeSqlIneightDocument` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00125 | `plSourceToBronzeSqlIneightDocument` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00126 | `plSourceToBronzeSqlIneightDocument_serverless` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00127 | `plSourceToBronzeSqlIneightDocument_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00128 | `plSourceToBronzeSqlIneightDocument_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery`<br>`watermarkColumn`<br>`watermarkValue` |
| META-QRY-00129 | `plSourceToBronzeSqlIneightDocument_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00130 | `plSourceToBronzeSqlIneightEstimate` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00131 | `plSourceToBronzeSqlIneightEstimate` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00132 | `plSourceToBronzeSqlIneightEstimate` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00133 | `plSourceToBronzeSql_Referencedb` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00134 | `plSourceToBronzeSql_Referencedb` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00135 | `plSourceToBronzeSql_Referencedb` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00136 | `plSourceToBronzeSql_serverless` | Source metadata lookup | `adf.DataSource` | `sql server` | None detected |
| META-QRY-00137 | `plSourceToBronzeSql_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00138 | `plSourceToBronzeSql_serverless` | Per-object runtime query | None detected | None detected | `objectName`<br>`objectSchema`<br>`sourceQuery` |
| META-QRY-00139 | `plSourceToBronzeSql_serverless` | Operational metrics lookup | `adf.operationMetricLog` | None detected | None detected |
| META-QRY-00140 | `plUpdateDatasetId` | Other metadata query | `adf.powerBiDataset` | None detected | None detected |

## Required validation

- Export the actual metadata rows for `adf.DataSource`, `adf.DataProcess`, and `adf.DataProcessDependency` from the governed Azure SQL metadata database.
- Confirm which metadata fields are authoritative versus legacy or unused.
- Resolve dynamic notebook paths and Databricks job IDs before creating production Databricks task definitions.
- Preserve process dependency, retry, logging, row-count validation, and notification semantics during migration.

The machine-readable dependency file is `architecture-lens/metadata/metadata-dependencies.json`.
