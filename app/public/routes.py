from flask import (
    abort,
    make_response,
    render_template,
    redirect,
    url_for,
    request,
    current_app,
    escape,
)

from . import public_bp


todos = ["RODO 1", "RODO 2", "RODO 3", "RODO 4", "RODO 5"]


@public_bp.route("/")
def index():
    user_ip = request.remote_addr

    response = make_response(redirect(url_for("public.hello")))
    response.set_cookie("user_ip", user_ip)

    return response


@public_bp.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    user_ip = escape(user_ip)
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }
    return render_template("public/index.html", **context)
