from flask.ext.login import UserMixin

from ..extensions import db
from ..utils import CRUDModel


class User(UserMixin, CRUDModel):
    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

    def __repr__(self):
        return '<User(%r)>' % self.username
