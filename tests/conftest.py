import pytest
import sys
from os.path import abspath, dirname

# Add project root to Python path
sys.path.insert(0, abspath(dirname(dirname(__file__))))

# Import your Flask app instance
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()