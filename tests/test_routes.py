def test_public_route(client):
    response = client.get('/public')
    assert response.status_code == 200  # If no redirection is expected, change the test accordingly
