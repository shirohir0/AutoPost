from fastapi import APIRouter, HTTPException
from services.news import news_client

router = APIRouter(prefix="/news", tags=["News"])

NEWSMESH_BASE = "https://api.newsmesh.co/v1"

@router.get("/")
def get_news():
    try:
        data = news_client.get_latest_games()
    except Exception as e:
        # Можно логировать ошибку здесь
        raise HTTPException(status_code=503, detail=f"News service error: {str(e)}") from e

    return {
        "status": "ok",
        "total": len(data),
        "data": data  # лучше назвать data, а не news, чтобы совпадало с продакшен-форматом
    }
