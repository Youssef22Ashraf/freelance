"""Production configuration."""
import os

# Flask settings
SECRET_KEY = os.environ.get("SECRET_KEY")  # Must be set in environment
DEBUG = False

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # Must be set in environment
SQLALCHEMY_TRACK_MODIFICATIONS = False

# File upload settings
UPLOAD_FOLDER = "/app/uploads"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Security settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
PERMANENT_SESSION_LIFETIME = 1800  # 30 minutes

# Gunicorn settings (used in deployment)
GUNICORN_WORKERS = 4
GUNICORN_THREADS = 4
GUNICORN_TIMEOUT = 120
GUNICORN_BIND = "0.0.0.0:5000" 