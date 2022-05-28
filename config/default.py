from os.path import abspath, dirname

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY = "7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"

# Database configuration
SQLALCHEMY_TRACK_MODIFICATIONS = False


# app.secret_key = 'dev'
FOMANTIC_SERVE_LOCAL = False


# set default button sytle and size, will be overwritten by macro parameters
FOMANTIC_BUTTON_STYLE = "primary"
FOMANTIC_BUTTON_SIZE = ""

# set default icon title of table actions
FOMANTIC_TABLE_VIEW_TITLE = "Read"
FOMANTIC_TABLE_EDIT_TITLE = "Update"
FOMANTIC_TABLE_DELETE_TITLE = "Remove"
FOMANTIC_TABLE_NEW_TITLE = "Create"

FOMANTIC_CHECKBOX_HEADER_ERROR = "Checkbox Header Error"
FOMANTIC_RADIO_HEADER_ERROR = "Radio Header Error"


# App environments
APP_ENV_LOCAL = "local"
APP_ENV_TESTING = "testing"
APP_ENV_DEVELOPMENT = "development"
APP_ENV_STAGING = "staging"
APP_ENV_PRODUCTION = "production"
APP_ENV = ""
