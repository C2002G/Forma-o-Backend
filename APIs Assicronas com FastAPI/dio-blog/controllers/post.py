from fastapi import status, APIRouter
from datetime import datetime, UTC
from schemas.post import PostIn
from views.post import PostOut

# https://fastapi.tiangolo.com/tutorial/body/

router = APIRouter(prefix="/posts")


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


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostOut])
def read_posts(published: bool, limit: int, skip: int = 0):
    tail = skip + limit
    return [post for post in fake_db[skip:tail] if post["published"] is published]
    # posts = []
    # for post in fake_db:
    #     if len(posts) == limit:
    #         break
    #     if post["published"] is published:
    #         posts.append(post)
    # return posts
    # def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):


@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework):
    return {
        "posts": [
            {"title": f"Criando uma aplicação {framework}", "date": datetime.now(UTC)},
            {"title": f"Globalizando uma app {framework}", "date": datetime.now(UTC)},
        ]
    }
