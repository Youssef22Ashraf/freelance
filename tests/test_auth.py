def test_login(client):
    response = client.post("/login", data={"id": "test_user", "pw": "test_password"})
    assert response.status_code == 302  # Assuming login redirects
    assert b"Redirecting..." in response.data