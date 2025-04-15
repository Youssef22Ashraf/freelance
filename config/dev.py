"""Development configuration."""
import os

# Flask settings
SECRET_KEY = "dev_secret_key"
DEBUG = True

# Database settings
SQLALCHEMY_DATABASE_URI = "sqlite:///database_file/app.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# File upload settings
UPLOAD_FOLDER = "image_pool"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size 