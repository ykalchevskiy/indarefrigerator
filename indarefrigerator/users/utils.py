from .models import User
from ..extensions import db


def create_user(username, password):
    user = User(username, password)
    db.session.add(user)
    db.session.commit()
