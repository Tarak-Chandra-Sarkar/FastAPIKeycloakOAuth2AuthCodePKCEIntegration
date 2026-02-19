from fastapi import FastAPI
from core.config import settings
from api import routes, protected

app = FastAPI(
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth={
        "clientId": settings.KEYCLOAK_CLIENT_ID,
        "usePkceWithAuthorizationCodeGrant": True,
    }
)

app.include_router(routes.router)
app.include_router(protected.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
