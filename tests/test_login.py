import pytest
from app import app
from database import add_user, delete_user_from_db, list_users

TEST_USERNAME = 'TEST_USER'
TEST_PASSWORD = 'test_password'

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Setup test user
        if TEST_USERNAME not in list_users():
            add_user(TEST_USERNAME, TEST_PASSWORD)
        yield client
        # Cleanup test user
        if TEST_USERNAME in list_users():
            delete_user_from_db(TEST_USERNAME)

def test_successful_login(client):
    """Test successful login redirects to private page"""
    response = client.post("/login", data={"id": TEST_USERNAME, "pw": TEST_PASSWORD})
    assert response.status_code == 302
    assert b"Redirecting..." in response.data
    assert b"/private/" in response.data

def test_failed_login_invalid_credentials(client):
    """Test login with invalid credentials"""
    response = client.post("/login", data={"id": "invalid_user", "pw": "wrong_password"})
    assert response.status_code == 302
    assert b"Redirecting..." in response.data
    assert b"/" in response.data  # Should redirect to home page

def test_failed_login_empty_credentials(client):
    """Test login with empty credentials"""
    response = client.post("/login", data={"id": "", "pw": ""})
    assert response.status_code == 302
    assert b"Redirecting..." in response.data
    assert b"/" in response.data  # Should redirect to home page 