import os
from datetime import timedelta

# Session configuration
PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)

# Security settings
SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

# File upload settings
UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "uploads")
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///test.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

