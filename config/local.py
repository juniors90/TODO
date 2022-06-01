# config/local.py
from os.path import abspath, dirname, join
import sys
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
FILE_DIR = join(BASE_DIR,__name__)
sys.path.append(FILE_DIR)

import default

APP_ENV = default.APP_ENV_LOCAL
