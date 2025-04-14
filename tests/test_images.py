import os
from flask import current_app
import io

def test_image_upload(client):
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302  # Should redirect after login

    # Create a test image file
    img = io.BytesIO(b"fake image data")
    img.name = "test_image.jpg"

    # Upload the image
    response = client.post(
        "/upload_image",
        data={"file": (img, "test_image.jpg")},
        content_type="multipart/form-data"
    )
    assert response.status_code == 302  # Should redirect after upload
    assert b"/private/" in response.data  # Should redirect to private page

    # Clean up
    if os.path.exists(img.name):
        os.remove(img.name) 