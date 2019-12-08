from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)
from models import User


def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User already exists')


def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('Email associated with this user  already exists')


class RegistrationForm(Form):
    username = StringField('Username', validators=[  # Username is the placeholder/Label for the form
        DataRequired(),
        Regexp(r'^[a-zA-Z0-9_]+$', message='User should be one word with letters numbers and underscore only'),
        name_exists])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6),
                                                     EqualTo('password2', message='Passwords must be matched')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class PostForm(Form):
    content = TextAreaField('Whats on your mind', validators=[DataRequired()])
