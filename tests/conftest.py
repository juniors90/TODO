import flask
import pytest as pt
import typing as t

if t.TYPE_CHECKING:
    from flask.testing import FlaskClient



@pt.fixture
def app() -> "flask.Flask":
    from entrypoint import app
    app.testing = True
    return app

@pt.fixture
def client(app:"flask.Flask") -> "FlaskClient":
    return app.test_client()