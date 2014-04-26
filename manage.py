#!/usr/bin/env python

from flask.ext.script import Manager, prompt_bool, Shell

from indarefrigerator import create_app
from indarefrigerator.extensions import db
from indarefrigerator.products.models import Product
from indarefrigerator.users.models import User


app = create_app()
manager = Manager(app)


@manager.command
def dropdb():
    """Drops current database."""

    if prompt_bool('Are you sure?'):
        db.drop_all()


@manager.command
def syncdb():
    """Syncs current database."""

    db.create_all()


@manager.command
def create_user(username, password):
    """Creates a new user."""

    User.create(username=username, password=password)


def _make_context():
    return {'app': app, 'db': db, 'Product': Product, 'User': User}


manager.add_command('shell', Shell('Welcome to the "InDaRefrigerator"!', _make_context))


if __name__ == '__main__':
    manager.run()
