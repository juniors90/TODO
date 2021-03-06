from flask import Flask, render_template

from flask_fomanticui import FomanticUI

from flask_login import LoginManager




from app.common.filters import format_datetime  # noqa: I100

login_manager = LoginManager()

semantic = FomanticUI()


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    # Load the config file specified by the APP environment variable

    app.config.from_object(settings_module)
    app.secret_key="jhfuyd54275870yyfk5366e"

    # Load the configuration from the instance folder

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    semantic.init_app(app)

    # Registro de los filtros
    register_filters(app)

    # Blueprint Registers
    from app.auth import auth_bp

    app.register_blueprint(auth_bp)

    from app.admin import admin_bp

    app.register_blueprint(admin_bp)

    from app.public import public_bp

    app.register_blueprint(public_bp)

    # Custom error handlers
    register_error_handlers(app)
    
    return app


def register_filters(app):
    app.jinja_env.filters["datetime"] = format_datetime


def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template("500.html"), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template("404.html"), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return render_template("401.html"), 401
