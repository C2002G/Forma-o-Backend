from http import HTTPStatus
import pytest


@pytest.mark.django_db
def test_contacts_thanks(client):
    # Given
    name = "John"

    # When
    response = client.get(f"/contacts/thanks/{name}")

    # Then
    assert response.status_code == HTTPStatus.OK
    assert "Obrigado, John!" in response.content.decode()
