from fastapi import FastAPI
from datetime import datetime, UTC

app = FastAPI()


fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC)},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC)},
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC)},
    {"title": "Criando uma aplicação com scarlet", "date": datetime.now(UTC)},
]


@app.get("/posts")
def read_posts(skip: int = 0, limit: int = len(fake_db)):
    return fake_db[skip: skip + limit]


@app.get("/posts/{framework}")
def read_framework_posts(framework):
    return {
        "posts": [
            {"title": f"Criando uma aplicação {framework}", "date": datetime.now(UTC)},
            {"title": f"Globalizando uma app {framework}", "date": datetime.now(UTC)},
        ]
    }


# rotas e endpoints FastAPI
