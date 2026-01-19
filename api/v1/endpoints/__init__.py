from api.v1.endpoints.news import router as news_router

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1")

router.include_router(news_router)
