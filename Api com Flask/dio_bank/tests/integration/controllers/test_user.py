from http import HTTPStatus
from src.app import User, Role, db


def test_get_user_success(client):
    role = Role(name="admin")
    db.session.add(role)
    db.session.commit()

    user = User(username="gab", password="test", role_id=role.id)
    db.session.add(user)
    db.session.commit()

    response = client.get("/users/{user.id}")
    assert response.status_code == HTTPStatus.OK
