from http import HTTPStatus
from flask import Blueprint, request
import sqlalchemy as sa
from src.app import Post, db

app = Blueprint("post", __name__, url_prefix="/posts")


def create_post():
    data = request.json
    post = Post(title=data["title"], body=data["body"], author_id=data["author_id"])
    db.session.add(post)
    db.session.commit()


def list_posts():
    query = db.select(Post)
    posts = db.session.execute(query).scalars()
    return [
        {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "author_id": post.author_id,
        }
        for post in posts
    ]


@app.route("/", methods=["GET", "POST"])
def handle_post():
    if request.method == "POST":
        create_post()
        return {"message": "post created!"}, HTTPStatus.CREATED  # PADRÂO REST
    else:
        return {"posts": list_posts()}


@app.route("/<int:post_id>")
def get_post(post_id):
    post = db.get_or_404(Post, post_id)
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "author_id": post.author_id,
    }


@app.route("/<int:post_id>", methods=["PATCH"])
def update_post(post_id):
    post = db.get_or_404(Post, post_id)
    data = request.json

    # Atualiza apenas os campos permitidos
    if "title" in data:
        post.title = data["title"]
    if "body" in data:
        post.body = data["body"]
    if "author_id" in data:
        post.author_id = data["author_id"]

    db.session.commit()

    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "author_id": post.author_id,
    }


@app.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)
    db.session.delete(post)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
