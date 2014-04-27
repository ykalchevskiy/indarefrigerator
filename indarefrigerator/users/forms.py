from flask.ext.wtf import Form

from wtforms.fields import PasswordField, TextField
from wtforms.validators import DataRequired, Email

from .models import User


class LoginForm(Form):
    email = TextField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(email=self.email.data).first()
        if not self.user:
            self.email.errors.append('Unknown user')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        return True
