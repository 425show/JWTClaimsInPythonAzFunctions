import logging
from jose import jwt
import azure.functions as func
import json

token=None

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    token = req.headers.get("X-MS-TOKEN-AAD-ACCESS-TOKEN", None)
    if not token:
        return func.HttpResponse(
            "Please pass the Azure AD Access Token in the X-MS-TOKEN-AAD-ACCESS-TOKEN header",
            status_code=401
        )
    token_claims = jwt.get_unverified_claims(token)

    # Do anything else you need here

    return func.HttpResponse(json.dumps(token_claims, indent=4))