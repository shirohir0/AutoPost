from services.news.client import NewsClient
import os
from dotenv import load_dotenv
load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    raise RuntimeError(
        "NEWSMESH_API_KEY is not set. "
        "Please set it in the environment variables or in the .env file."
    )

news_client = NewsClient(NEWS_API_KEY)
