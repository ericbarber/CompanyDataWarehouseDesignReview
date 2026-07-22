# this powershell script will replace the values in the linked service files with the correct environment values defined in DevOps variables in the DevOps release

param (

    [string]$keyvault_url,
    [string]$sharedkeyvault_url,
    [string]$sdatkeyvault_url,          
    [string]$databricks_url,
    [string]$databricks_clusterid,
    [string]$databricks_resourceid,
    [string]$databricks_nonisolation_clusterid,        
    [string]$datalake_url,
    [string]$powerbi_serviceprincipal_id,
    [string]$default_directory
)

# define variables
$kv_json_file = "lsKeyVaultManagedIdentity"
$shared_kv_json_file = "lsKeyVaultManagedIdentityShared"
$sdat_kv_json_file = "lsKeyVaultManagedIdentitySdat"
$adb_json_file = "lsAdbClusterManagedIdentity"
$adb_nonislolation_json_file = "lsAdbNonIsolationClusterManagedIdentity"
$adb_serverlessmsi_json_file = "lsAdbServerlessManagedIdentity"
$datalake_json_file = "lsAdlsManagedIdentity"
$powerbi_service_principal_json_file = "lsRestApiServicePrincipal"

# replace key vault name
$kv_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$kv_json_file.json" | ConvertFrom-Json
$kv_json.properties.typeProperties.baseUrl = $keyvault_url
$kv_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$kv_json_file.json"

# replace shared sdat key vault name
$kv_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$shared_kv_json_file.json" | ConvertFrom-Json
$kv_json.properties.typeProperties.baseUrl = $sharedkeyvault_url
$kv_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$shared_kv_json_file.json"

# replace web app sdat key vault name
$kv_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$sdat_kv_json_file.json" | ConvertFrom-Json
$kv_json.properties.typeProperties.baseUrl = $sdatkeyvault_url
$kv_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$sdat_kv_json_file.json"

# replace databricks cluster id
$adb_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$adb_json_file.json" | ConvertFrom-Json
$adb_json.properties.typeProperties.domain = $databricks_url
$adb_json.properties.typeProperties.existingClusterId = $databricks_clusterid
$adb_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$adb_json_file.json"

# replace databricks resourceid
$adb_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$adb_json_file.json" | ConvertFrom-Json
$adb_json.properties.typeProperties.domain = $databricks_url
$adb_json.properties.typeProperties.existingClusterId = $databricks_clusterid
$adb_json.properties.typeProperties.workspaceResourceId = $databricks_resourceid
$adb_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$adb_json_file.json"

# replace databricks non isolation cluster id
$adb_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$adb_nonislolation_json_file.json" | ConvertFrom-Json
$adb_json.properties.typeProperties.domain = $databricks_url
$adb_json.properties.typeProperties.existingClusterId = $databricks_nonisolation_clusterid
$adb_json.properties.typeProperties.workspaceResourceId = $databricks_resourceid
$adb_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$adb_nonislolation_json_file.json"

# replace databricks serverless
$adb_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$adb_serverlessmsi_json_file.json" | ConvertFrom-Json
$adb_json.properties.typeProperties.domain = $databricks_url
# $adb_json.properties.typeProperties.existingClusterId = $databricks_nonisolation_clusterid
$adb_json.properties.typeProperties.workspaceResourceId = $databricks_resourceid
$adb_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$adb_serverlessmsi_json_file.json"

# replace datalake name
$datalake_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$datalake_json_file.json" | ConvertFrom-Json
$datalake_json.properties.typeProperties.url = $datalake_url
$datalake_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$datalake_json_file.json"

# replace power bi service principal id
$powerbi_service_principal_json = Get-Content -Path "$default_directory/_DataFactory/linkedService/$powerbi_service_principal_json_file.json" | ConvertFrom-Json
$powerbi_service_principal_json.properties.typeProperties.servicePrincipalId = $powerbi_serviceprincipal_id
$powerbi_service_principal_json | ConvertTo-Json -depth 32 | Set-Content -Path "$default_directory/_DataFactory/linkedService/$powerbi_service_principal_json_file.json"