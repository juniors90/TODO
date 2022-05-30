# entrypoint.py
import os

import pytest

from app import create_app

settings_module = os.getenv("APP_SETTINGS_MODULE")

app = create_app(settings_module)

@app.cli.command()
def test():
    '''
    Run tests.
    '''
    pytest.main(['--rootdir', './tests'])
