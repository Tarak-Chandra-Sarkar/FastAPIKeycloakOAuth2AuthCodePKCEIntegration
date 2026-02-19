from fastapi import APIRouter, Depends
from middleware.auth_middleware import get_current_user

router = APIRouter(prefix="/protected", tags=["Protected"])

@router.get("/")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}! This is protected."}
