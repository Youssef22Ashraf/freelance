import pytest
from flask import session
from app import app
from database import add_user, read_note_from_db, list_users, delete_user_from_db, write_note_into_db
import hashlib

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clean up any existing test user
        test_username = 'TESTUSER'
        if test_username in list_users():
            delete_user_from_db(test_username)
            
        # Create a test user
        test_password = 'password'
        add_user(test_username, test_password)
        
        # Log in the test user
        with client.session_transaction() as sess:
            sess['current_user'] = test_username
            sess['_fresh'] = True
            
        yield client
        
        # Cleanup after test
        if test_username in list_users():
            delete_user_from_db(test_username)

def test_create_note(client):
    """Test creating a new note"""
    test_note = 'This is a test note'
    response = client.post('/write_note', data={
        'text_note_to_take': test_note
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"This is a test note" in response.data
    
    # Verify note was saved in database
    notes = read_note_from_db('TESTUSER')
    assert any(test_note in note for note in notes)

def test_delete_note(client):
    """Test deleting a note"""
    # First create a note
    test_note = 'Note to be deleted'
    write_note_into_db('TESTUSER', test_note)
    
    # Get the note_id of the created note
    notes = read_note_from_db('TESTUSER')
    note_id = next(note[0] for note in notes if test_note in note)
    
    # Delete the note
    response = client.get(f'/delete_note/{note_id}', follow_redirects=True)
    assert response.status_code == 200
    
    # Verify note was deleted from database
    notes = read_note_from_db('TESTUSER')
    assert not any(test_note in note for note in notes) 