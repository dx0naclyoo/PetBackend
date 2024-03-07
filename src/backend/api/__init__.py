from fastapi import APIRouter
from .auth import router as auth_router

router = APIRouter(prefix="/api_v1",)
router.include_router(auth_router)
