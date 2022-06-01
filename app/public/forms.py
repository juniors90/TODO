from flask_wtf import FlaskForm

from wtforms import SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    taskArea = TextAreaField(
        'Description',
        validators=[DataRequired(), Length(max=200)],
        render_kw={
            'placeholder': 'The was a beautiful day...',
            'rows': '3',
            'style':'{margin-botton:10px;}'
        },
    )
    state = BooleanField("State")
    done = BooleanField("Done")
    taskButton = SubmitField(
        "Add Task",
        render_kw={
            'class': 'ui blue labeled submit icon button',
        })

class DeleteTaskForm(FlaskForm):
    delete_button = SubmitField(
        "Delete",
        render_kw={
            "class":"ui negative button"
        })