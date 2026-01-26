from fastapi import APIRouter, HTTPException
from services.news import news_client

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/")
def get_news():
    try:
        data = news_client.get_latest_games()
    except Exception as e:
        # Можно логировать ошибку здесь
        raise HTTPException(status_code=503, detail=f"News service error: {str(e)}") from e

    return {
        "status": "ok",
        "data": data
    }
