import sys, json, requests, msal

# Cert based authentication using a service principal against MSFT AAD common endpoint (v2)
# This is using MSAL over ADAL and uses a private key with a thumbprint loaded onto the service principal for authentication
# TODO: provide instructions in README on how to get the .pem
def get_auth_token_from_cert(paramFile):

    app = msal.ConfidentialClientApplication(
        paramFile["client_id"], authority=paramFile["authority"],
        client_credential={"thumbprint": paramFile["thumbprint"], "private_key": open(paramFile['private_key_file']).read()}
        )

    result = None

    if not result:
        result = app.acquire_token_for_client(scopes=paramFile["scope"])

    return result