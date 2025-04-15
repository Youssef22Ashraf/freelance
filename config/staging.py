"""Staging configuration."""
import os

# Flask settings
SECRET_KEY = os.environ.get("SECRET_KEY", "staging_secret_key")
DEBUG = False

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/flask_app_staging"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# File upload settings
UPLOAD_FOLDER = "/app/uploads"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Gunicorn settings (used in deployment)
GUNICORN_WORKERS = 2
GUNICORN_THREADS = 4
GUNICORN_TIMEOUT = 120
GUNICORN_BIND = "0.0.0.0:5000" 