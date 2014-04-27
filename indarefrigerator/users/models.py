from flask.ext.login import UserMixin

from sqlalchemy.orm import validates

from ..extensions import bcrypt, db
from ..utils import CRUDModel


class User(UserMixin, CRUDModel):
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column('password', db.String(128))
    is_admin = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<User(%r)>' % self.email

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = bcrypt.generate_password_hash(password)

    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password, password)

    def is_superuser(self):
        return self.is_admin

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email, 'Given "email" is not correct.'
        return email
