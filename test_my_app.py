import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login(client):
    response = client.post("/login", data={"id": "test_user", "pw": "test_password"})
    assert response.status_code == 302  # Assuming login redirects
    assert b"Redirecting..." in response.data

def test_private_page_without_login(client):
    response = client.get("/private/")
    assert response.status_code == 401
