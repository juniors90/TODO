# config/dev.py
from .default import __all__

APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
