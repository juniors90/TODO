from os.path import abspath, dirname, join
import sys
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
FILE_DIR = join(BASE_DIR,__name__)
sys.path.append(FILE_DIR)

from flask import Blueprint

auth_bp = Blueprint("auth", __name__, template_folder="templates")

from app.auth import routes
