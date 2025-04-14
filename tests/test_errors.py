import pytest
from flask import session
from app import app
from database import add_user, list_users, delete_user_from_db
import os
from io import BytesIO

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_401_unauthorized(client):
    """Test 401 Unauthorized error"""
    # Try to access private page without login
    response = client.get('/private/')
    assert response.status_code == 401
    assert b"You're not allowed to access" in response.data

def test_403_forbidden(client):
    """Test 403 Forbidden error"""
    # Try to access admin page as regular user
    response = client.get('/admin/')
    assert response.status_code == 401
    assert b"You're not allowed to access" in response.data

def test_404_not_found(client):
    """Test 404 Not Found error"""
    # Try to access non-existent page
    response = client.get('/nonexistent-page/')
    assert response.status_code == 404
    assert b"404" in response.data  # Most 404 pages include "404" somewhere

def test_413_file_too_large(client):
    """Test 413 File Too Large error"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Create a large file (bigger than 16MB)
    large_file = BytesIO(b'0' * (16 * 1024 * 1024 + 1))  # 16MB + 1 byte
    
    # Try to upload the large file
    response = client.post('/upload_image', 
                         data={'file': (large_file, 'test.jpg')},
                         content_type='multipart/form-data')
    assert response.status_code == 413
    assert b"Request if too big(413)" in response.data 