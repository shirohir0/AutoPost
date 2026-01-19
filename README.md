# AutoPost — последние игровые новости

**AutoPost** — простой сервис на Python для получения последних игровых релизов из API [MMO Games](https://rapidapi.com/MMO/api/mmo-games). С помощью FastAPI можно легко отдавать эти данные фронтенду или боту в удобном JSON-формате.

---

## Структура проекта

```
AutoPost/
│
├── api/
│   └── v1/
│       └── endpoints/
│           └── news.py        # FastAPI endpoint для новостей
│
├── services/
│   └── news/
│       └── client.py          # Класс NewsClient для работы с API
│
├── utils/
│   └── .env                   # Хранение секретов (API ключ)
│
├── main.py                    # Запуск FastAPI приложения
├── README.md
├── .gitignore
└── requirements.txt

```

---

## Установка и запуск

1. Клонируйте репозиторий и создайте виртуальное окружение:

```bash
git clone https://github.com/shirohir0/AutoPost
cd AutoPost
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

2. Добавьте `.env` с вашим ключом RapidAPI:

```
RAPIDAPI_KEY=your_rapidapi_key
```

3. Запустите сервер:

```bash
uvicorn main:app --reload
```

4. Перейдите в браузер или отправьте запрос:

```
http://127.0.0.1:8000/news
```

---


## Формат данных

FastAPI endpoint `/news` возвращает:

```json
{
  "status": "ok",
  "total": 10,
  "data": [
    {
      "news_id": 1226,
      "title": "Where Winds Meet",
      "description": "Open-world action-adventure RPG set in ancient China!",
      "thumbnail": "https://www.mmobomb.com/g/1226/thumbnail.jpg",
      "release_date": "2025-11-14"
    },
    ...
  ]
}
```

---
