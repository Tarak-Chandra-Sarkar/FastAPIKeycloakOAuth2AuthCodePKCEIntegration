import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KEYCLOAK_URL: str = os.getenv("KEYCLOAK_URL")
    KEYCLOAK_REALM: str = os.getenv("KEYCLOAK_REALM")
    KEYCLOAK_CLIENT_ID: str = os.getenv("KEYCLOAK_CLIENT_ID")
    KEYCLOAK_AUDIENCE: str = os.getenv("KEYCLOAK_AUDIENCE")
    KEYCLOAK_ALGORITHM: str = os.getenv("KEYCLOAK_ALGORITHM")

    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = int(os.getenv("APP_PORT"))

    @property
    def auth_url(self):
        return f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}/protocol/openid-connect/auth"

    @property
    def token_url(self):
        return f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}/protocol/openid-connect/token"

    @property
    def jwks_url(self):
        return f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}/protocol/openid-connect/certs"

    @property
    def issuer(self):
        return f"{self.KEYCLOAK_URL}/realms/{self.KEYCLOAK_REALM}"


settings = Settings()
