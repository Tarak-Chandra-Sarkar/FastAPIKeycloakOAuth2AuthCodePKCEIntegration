from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt, JWTError
from core.config import settings
from services.keycloak_service import get_public_key

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=settings.auth_url,
    tokenUrl=settings.token_url,
    scopes={
        "openid": "OpenID Connect",
        "profile": "User Profile",
    },
    description="Keycloak OAuth2 AuthorizationCode Flow with PKCE",
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            get_public_key(token),
            algorithms=[settings.KEYCLOAK_ALGORITHM],
            audience=settings.KEYCLOAK_AUDIENCE,
            issuer=settings.issuer,
        )

        username = payload.get("preferred_username")
        if username is None:
            raise credentials_exception

        return username

    except JWTError:
        raise credentials_exception
