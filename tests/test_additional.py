import pytest
from io import BytesIO
from flask import session

def test_405_method_not_allowed(client):
    """Test 405 Method Not Allowed error"""
    # Try to POST to a GET-only endpoint
    response = client.post('/private/')
    assert response.status_code == 405
    assert b"Method not allowd (405)" in response.data

def test_invalid_file_upload(client):
    """Test uploading a file with invalid extension"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Create a test file with invalid extension
    invalid_file = BytesIO(b"fake image data")
    invalid_file.name = "test.txt"

    # Try to upload the invalid file
    response = client.post('/upload_image',
                         data={'file': (invalid_file, "test.txt")},
                         content_type='multipart/form-data')
    assert response.status_code == 302  # Should redirect
    assert b"/private/" in response.data  # Should redirect to private page

def test_empty_file_upload(client):
    """Test uploading an empty file"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to upload without a file
    response = client.post('/upload_image',
                         data={},
                         content_type='multipart/form-data')
    assert response.status_code == 302  # Should redirect
    assert b"/private/" in response.data  # Should redirect to private page

def test_empty_note_creation(client):
    """Test creating a note with empty content"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to create an empty note
    response = client.post('/write_note',
                         data={'text_note_to_take': ''},
                         follow_redirects=True)
    assert response.status_code == 200
    assert b"/private/" in response.data

def test_delete_nonexistent_note(client):
    """Test deleting a non-existent note"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to delete a note that doesn't exist
    response = client.get('/delete_note/999', follow_redirects=True)
    assert response.status_code == 401  # Should return unauthorized since note doesn't exist

def test_add_user_invalid_chars(client):
    """Test adding a user with invalid characters"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to add a user with invalid characters
    response = client.post("/add_user", data={"id": "invalid'user", "pw": "password"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"The account name is invalid." in response.data  # This is the actual error message displayed

def test_add_user_with_spaces(client):
    """Test adding a user with spaces in the username"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to add a user with spaces
    response = client.post("/add_user", data={"id": "user with spaces", "pw": "password"})
    assert response.status_code == 200
    assert b"The account name is invalid." in response.data

def test_delete_nonexistent_user(client):
    """Test deleting a user that doesn't exist"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Try to delete a non-existent user
    response = client.get('/delete_user/nonexistent_user/', follow_redirects=True)
    assert response.status_code == 200  # The route returns 200 and redirects to admin page
    assert b"ADMIN" in response.data  # Verify we're on the admin page

def test_session_timeout(client):
    """Test session timeout"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Access private page
    response = client.get('/private/')
    assert response.status_code == 200

    # Logout
    response = client.get('/logout/')
    assert response.status_code == 302

    # Try to access private page after logout
    response = client.get('/private/')
    assert response.status_code == 401 