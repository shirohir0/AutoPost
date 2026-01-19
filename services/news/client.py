import requests
from typing import Dict


class NewsClient:
    BASE_URL = "https://mmo-games.p.rapidapi.com/games"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "mmo-games.p.rapidapi.com"
        }

    def get_latest_games(self, limit: int = 10) -> Dict[int, Dict]:
        """
        Возвращает последние игры в формате словаря (ключ int),
        но в продакшен мы будем отдавать массив через FastAPI
        """
        params = {"sort-by": "release-date"}
        response = requests.get(self.BASE_URL, headers=self.headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data[:limit]
