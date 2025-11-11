from fastapi import FastAPI, status
from datetime import datetime, UTC
from pydantic import BaseModel

app = FastAPI()


fake_db = [
    {
        "title": "Criando uma aplicação com Django",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com Flask",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com FastAPI",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": "Criando uma aplicação com scarlet",
        "date": datetime.now(UTC),
        "published": True,
    },
]


# https://fastapi.tiangolo.com/tutorial/body/
class Post(BaseModel):
    name: str
    date: datetime = datetime.now(UTC)
    published: bool = False


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    fake_db.append(post.model_dump())
    return post


@app.get("/posts")
def read_posts(published: bool, limit: int, skip: int = 0):
    return [
        post for post in fake_db[skip: skip + limit] if post["published"] is published
    ]
    # posts = []
    # for post in fake_db:
    #     if len(posts) == limit:
    #         break
    #     if post["published"] is published:
    #         posts.append(post)
    # return posts
    # def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):


@app.get("/posts/{framework}")
def read_framework_posts(framework):
    return {
        "posts": [
            {"title": f"Criando uma aplicação {framework}", "date": datetime.now(UTC)},
            {"title": f"Globalizando uma app {framework}", "date": datetime.now(UTC)},
        ]
    }


# rotas e endpoints FastAPI
