from flask_wtf import FlaskForm

# wtforms é uma extensão pra fazer form com flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
import email_validator

# fazendo a class e declarando form de registro
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8)],
    )
    confirm_password = PasswordField(
        "Confirm Password:",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords don't match"),
        ],
    )
    submit = SubmitField("Sign Up")


# fazendo a class e declarando form de login
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8)],
    )
    remember = BooleanField("Remember Me!")
    submit = SubmitField("Login")
