import os
import flask
import pytest as pt
import typing as t

from config import testing
from app import create_app, db as _db

if t.TYPE_CHECKING:
    from flask.testing import FlaskClient


@pt.fixture
def app() -> "flask.Flask":
    import os
    settings_module = os.getenv("APP_SETTINGS_MODULE")
    app = create_app(settings_module=testing)
    app.testing = True
    return app


@pt.fixture
def client(app:"flask.Flask") -> "FlaskClient":
    return app.test_client()


@pt.fixture(scope='session')
def db():
    """Session-wide test database."""
    import os
    settings_module = os.getenv("APP_SETTINGS_MODULE")
    app = create_app(settings_module=testing)
    with app.app_context():
        _db.create_all()
        yield _db  
        _db.drop_all()