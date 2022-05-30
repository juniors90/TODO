from flask_wtf import FlaskForm

from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[DataRequired(), Length(max=64)],
        render_kw={"placeholder": "Name"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"},
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"},
    )
    submit = SubmitField("Registrar")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired()],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"},
    )
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")
