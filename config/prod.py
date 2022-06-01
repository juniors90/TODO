# config/prod.py
from os.path import abspath, dirname, join
import sys
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
FILE_DIR = join(BASE_DIR,__name__)
sys.path.append(FILE_DIR)

import default

SECRET_KEY = "5e04a4955d8878191923e86fe6a0dfb24edb226c87d6c7787f35ba4698afc86e95cae409aebd47f7"

APP_ENV = default.APP_ENV_PRODUCTION