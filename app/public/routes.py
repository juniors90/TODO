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

from app.public import public_bp
from app.firestore_service import get_todos, get_users, save_todo
from app.public.forms import TaskForm, DeleteTaskForm
from app.public.models import Task


@public_bp.route("/")
@login_required
def index():
    user_ip = request.remote_addr
    session["user_ip"] = user_ip
    response = make_response(redirect(url_for("public.task")))

    return response


@public_bp.route("/task", methods=["GET", "POST"])
@login_required
def task():
    user_ip = session.get("user_ip")
    user_id = current_user.get_id()
    todos = get_todos(user_id=user_id)
    task_form = TaskForm()
    delete_form = DeleteTaskForm()
    context = {
        "user_ip": user_ip,
        "todos": todos,
        "username": user_id,
        "task_form": task_form,
        "delete_form": delete_form,
    }
    if task_form.validate_on_submit():
        new_task = {
            'task': task_form.taskArea.data,
            'done': task_form.done.data,
            'state': task_form.state.data,
        }
        task = Task(user_id=user_id)
        task.save_task(**new_task)
        return redirect(url_for('public.task'))
    return render_template("public/index.html", **context)


@public_bp.route("/task/delete/<task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    user_id = current_user.get_id()
    task = Task(user_id=user_id)
    task.delete_task(task_id=task_id)
    return redirect(url_for('public.task'))



@public_bp.route("/task/update/<task_id>/", methods=['GET', 'POST'])
@login_required
def update_task_form(task_id):
    """Actualiza un post existente"""
    user_id = current_user.get_id()
    task = Task(user_id=user_id)
    task_dict=task.get_task_to_dict(task_id=task_id)

    class TaskData:
        taskArea = task_dict['task']
        done = task_dict['done']
        state = task_dict['state']

    task_data = TaskData()

    task_form = TaskForm(obj=task_data)
    context = {
        "task": task,
        "task_form": task_form,
    }
    if task_form.validate_on_submit():
        # Actualiza los campos del post existente
        update_task = {
            'task_id': task_id,
            'task': task_form.taskArea.data,
            'done': task_form.done.data,
            'state': task_form.state.data,
        }
        task.update_task(**update_task)
        return redirect(url_for('public.task'))
    return render_template("public/index.html", **context)
