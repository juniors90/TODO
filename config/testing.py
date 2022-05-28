# config/testing.py
from .default import __all__

# Parámetros para activar el modo debug

TESTING = True

DEBUG = True

APP_ENV = APP_ENV_TESTING

SQLALCHEMY_DATABASE_URI = "sqlite:///db_test.sqlite"
