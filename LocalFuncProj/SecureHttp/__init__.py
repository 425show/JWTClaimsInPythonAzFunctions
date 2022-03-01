import logging
from jose import jwt
import azure.functions as func
import json

token=None

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')

    auth = req.headers.get("Authorization", None)
    if not auth:
        return func.HttpResponse(
             "Authentication error: Authorization header is missing",
             status_code=401
        )
    parts = token.split()

    if parts[0].lower() != "bearer":
        return func.HttpResponse("Authentication error: Authorization header must start with ' Bearer'", 401)
    elif len(parts) == 1:
        return func.HttpResponse("Authentication error: Token not found", 401)
    elif len(parts) > 2:
        return func.HttpResponse("Authentication error: Authorization header must be 'Bearer <token>'", 401)

    token_claims = jwt.get_unverified_claims(parts[1])

    # Do anything else you need here

    return func.HttpResponse(json.dumps(token_claims, indent=4))