import json, sys

Class Params:
    def __init__(self, paramFile):

        paramFileJson = json.loads(paramFile)

        for val in paramFileJson:
            
        self.authority_type = paramFileJson["authority_type"]
        self.authority = paramFileJson["authority"]
        self.client_id = paramFileJson["client_id"]
        self.resource = paramFileJson["resource"]
        self.databricks_uri = paramFileJson["databricks_uri"]
        self.cert_thumbprint = paramFileJson["cert_thumbprint"]
        self.private_key_file = paramFileJson["private_key_file"]
        self.client_secret = paramFileJson["client_secret"]