import os
from flask import current_app
import io
from database import add_user, list_users, delete_user_from_db, image_upload_record, list_images_for_user, delete_image_from_db

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

def test_image_deletion(client):
    """Test image deletion functionality"""
    # First login as admin
    response = client.post("/login", data={"id": "admin", "pw": "admin"})
    assert response.status_code == 302

    # Create and upload a test image
    img = io.BytesIO(b"fake image data")
    img.name = "test_image.jpg"
    
    # Upload the image
    response = client.post(
        "/upload_image",
        data={"file": (img, "test_image.jpg")},
        content_type="multipart/form-data"
    )
    assert response.status_code == 302

    # Get the image UID from the database
    images = list_images_for_user("ADMIN")
    assert len(images) > 0
    image_uid = images[0][0]  # First image's UID

    # Delete the image
    response = client.get(f"/delete_image/{image_uid}", follow_redirects=True)
    assert response.status_code == 200

    # Verify image is deleted from database
    images = list_images_for_user("ADMIN")
    assert not any(img[0] == image_uid for img in images)

    # Clean up
    if os.path.exists(img.name):
        os.remove(img.name) 