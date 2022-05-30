from flask import (
    escape,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required

from . import public_bp
from app.firestore_service import get_todos, get_users


@public_bp.route("/")
@login_required
def index():
    user_ip = request.remote_addr
    session["user_ip"] = user_ip
    response = make_response(redirect(url_for("public.hello")))

    return response


@public_bp.route("/hello")
@login_required
def hello():
    user_ip = session.get("user_ip")
    username = session.get("email")
    todos = get_todos(user_id=username)
    context = {
        "user_ip": user_ip,
        "todos": todos,
        "username": username,
    }
    return render_template("public/index.html", **context)
