import pytest
from rest_framework.test import APIClient
from users.models import User

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(email="luka@example.com", username="luka", password="test1234")
    assert user.email == "luka@example.com"
    assert user.check_password("test1234")

@pytest.mark.django_db
def test_user_login_api():
    client = APIClient()

    user = User.objects.create_user(email="luka@example.com", username="luka", password="test1234")

    data = {
        "email": "luka@example.com",
        "password": "test1234"
    }
    response = client.post("/api/token/", data, format="json")

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


