from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, ValidationError
from wtforms.validators import InputRequired, Email, Length, EqualTo
from wtforms.fields.__init__ import EmailField
from werkzeug.security import check_password_hash

from author.models import Author


class LoginForm(FlaskForm):
    email = EmailField('Email address', [InputRequired(), Email()])
    password = PasswordField('New Password', [
        InputRequired(),
        Length(min=4, max=80)
    ])

    def validate(self, extra_validators=None):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        author = Author.query.filter_by(
            email=self.email.data,
        ).first()

        if author:
            if not check_password_hash(author.password, self.password.data):
                self.password.errors.append('Incorrect email or password')
                return False
            return True
        else:
            self.password.errors.append('Incorrect email or password')
            return False


class RegisterForm(FlaskForm):
    full_name = StringField('Full Name', [InputRequired()])
    email = EmailField('Email address', [InputRequired(), Email()])
    password = PasswordField('New Password', [
        InputRequired(),
        Length(min=4, max=80)
    ])
    confirm = PasswordField('Repeat Password', [
        EqualTo('password', message='Passwords must match'),
    ])

    def validate_email(self, field):
        author = Author.query.filter_by(email=field.data).first()
        if author:
            raise ValidationError('Email already in use, please use a different one.')
