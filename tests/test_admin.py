import pytest
from flask import session
from app import app
from database import add_user, list_users, delete_user_from_db, verify

@pytest.fixture
def admin_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Log in as admin
        with client.session_transaction() as sess:
            sess['current_user'] = 'ADMIN'
            sess['_fresh'] = True
        yield client

def test_admin_add_user(admin_client):
    """Test adding a new user as admin"""
    # Clean up test user if exists
    test_username = 'NEWTESTUSER'
    if test_username in list_users():
        delete_user_from_db(test_username)
    
    # Add new user
    response = admin_client.post('/add_user', data={
        'id': test_username,
        'pw': 'newpassword'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert test_username in list_users()
    
    # Verify password was set correctly
    assert verify(test_username, 'newpassword')
    
    # Cleanup
    delete_user_from_db(test_username)

def test_admin_delete_user(admin_client):
    """Test deleting a user as admin"""
    # Create a test user first
    test_username = 'USERTODELETE'
    if test_username not in list_users():
        add_user(test_username, 'password')
    
    # Delete the user
    response = admin_client.get(f'/delete_user/{test_username}/', follow_redirects=True)
    
    assert response.status_code == 200
    assert test_username not in list_users()

def test_unauthorized_user_management():
    """Test that non-admin users cannot manage users"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Log in as regular user
        with client.session_transaction() as sess:
            sess['current_user'] = 'TESTUSER'
            sess['_fresh'] = True
        
        # Try to add a user
        response = client.post('/add_user', data={
            'id': 'UNAUTHORIZED',
            'pw': 'password'
        }, follow_redirects=True)
        
        assert response.status_code == 401  # Unauthorized
        
        # Try to delete a user
        response = client.get('/delete_user/TESTUSER/', follow_redirects=True)
        assert response.status_code == 401  # Unauthorized 