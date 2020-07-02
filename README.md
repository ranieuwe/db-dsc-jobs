# db-dsc-jobs
A mechanism to ensure a series of configured jobs are loaded into an Azure Databricks instance


## Parameter File

The parameter file will have the following values present:




### Parameter Examples

{
    "authority_type": "spn-cert"
    "authority": "https://login.microsoftonline.com/<tenant_id>"
    "client_id": "<client-id>"

    "resource": "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"
    "databricks_uri": "https://<adb_instance>.azuredatabricks.net",

    "cert_thumbprint": "<cert_thumbprint>",
    "private_key_file": "<private_key_file.ext>"
}

{
    "authority_type": "spn-key"
    "authority": "https://login.microsoftonline.com/<tenant_id>"
    "client_id": "<your-sp-client-id>"

    "resource": "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"
    "databricks_uri": "https://<adb_instance>.azuredatabricks.net",

    "client_secret": "<client_secret>"
}

{
    "authority_type": "msi"
    "authority": "https://login.microsoftonline.com/<tenant_id>"
    "client_id": "<client-id>"

    "resource": ["2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"],
    "databricks_uri": "https://<adb_instance>.azuredatabricks.net"
}



{
    "authority_type": "msi",
    "authority": "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01",
    "client_id": "c6e59a73-6fc8-43bb-9fb2-93af2323ce6c",
    "resource": "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d",
    "databricks_uri": "https://adb-4960803188663244.4.azuredatabricks.net/"
}