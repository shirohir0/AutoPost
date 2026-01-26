from typing import Dict

import requests


class NewsClient:
    BASE_URL = "https://mmo-games.p.rapidapi.com"
    LATEST_NEWS_URL = f"{BASE_URL}/latestnews"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": "mmo-games.p.rapidapi.com",
        }

    def get_latest_games(self) -> Dict[int, Dict]:
        """
        Возвращает последние игровые новости.
        """
        response = requests.get(self.LATEST_NEWS_URL, headers=self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        latest_news = {
            "id": data[0].get("id"),
            "title": data[0].get("title"),
            "short_description": data[0].get("short_description"),
            "thumbnail": data[0].get("thumbnail"),
        }
        return latest_news


if __name__ == "__main__":
    import os

    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY is not set in environment variables")
    news_client = NewsClient(api_key=api_key)
    latest_news = news_client.get_latest_games()
    print(latest_news)
