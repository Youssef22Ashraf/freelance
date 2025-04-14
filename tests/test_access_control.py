import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_private_page_without_login(client):
    """Test that accessing private page without login returns 401"""
    response = client.get("/private/")
    assert response.status_code == 401
    assert b"You're not allowed to access" in response.data

def test_admin_page_without_login(client):
    """Test that accessing admin page without login returns 401"""
    response = client.get("/admin/")
    assert response.status_code == 401
    assert b"You're not allowed to access" in response.data

def test_admin_page_with_regular_user(client):
    """Test that regular users cannot access admin page"""
    # First login as regular user
    response = client.post("/login", data={"id": "test_user", "pw": "test_password"})
    assert response.status_code == 302
    
    # Try to access admin page
    response = client.get("/admin/")
    assert response.status_code == 401
    assert b"You're not allowed to access" in response.data 