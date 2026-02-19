import requests
from jose import jwt
from core.config import settings

def get_jwks():
    return requests.get(settings.jwks_url).json()

def get_public_key(token: str):
    jwks = get_jwks()
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")

    for key in jwks["keys"]:
        if key["kid"] == kid:
            return key

    raise Exception("Public key not found")
