from http import HTTPStatus
from flask import Blueprint, request
import sqlalchemy as sa
from src.app import User, db

app = Blueprint("user", __name__, url_prefix="/users")


def create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()


def list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            "id": user.id,
            "username": user.username,
        }
        for user in users
    ]


@app.route("/", methods=["GET", "POST"])
def handle_user():
    if request.method == "POST":
        create_user()
        return {"message": "User created!"}, HTTPStatus.CREATED  # PADRÂO REST
    else:
        return {"users": list_users()}


@app.route("/<int:user_id>")
def get_user(user_id):
    user = db.get_or_404(User, user_id)
    return {
        "id": user.id,
        "username": user.username,
    }


@app.route("/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    # Atualiza apenas os campos permitidos
    if "username" in data:
        user.username = data["username"]

    db.session.commit()

    return {
        "id": user.id,
        "username": user.username,
    }

@app.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return "    ", HTTPStatus.NO_CONTENT