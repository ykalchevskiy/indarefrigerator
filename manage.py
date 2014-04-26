#!/usr/bin/env python

import unittest

from flask.ext.script import Manager, prompt_bool, Shell

from indarefrigerator import create_app
from indarefrigerator.extensions import db
from indarefrigerator.products.models import Product
from indarefrigerator.users.models import User


app = create_app()
manager = Manager(app)
manager_db = Manager(help='Database manager.')


@manager_db.command
def drop():
    """Drops database."""

    if prompt_bool('Are you sure?'):
        db.drop_all()


@manager_db.command
def create():
    """Syncs database."""

    db.create_all()


@manager_db.command
def recreate():
    """Recreates database."""
    drop()
    create()


@manager.command
def create_user(username, password):
    """Creates a new user."""

    User.create(username=username, password=password)


@manager.command
def tests():
    """Runs tests."""

    loader = unittest.TestLoader()
    test_runner = unittest.TextTestRunner()
    test_runner.run(loader.discover('tests'))


def _make_context():
    return {'app': app, 'db': db, 'Product': Product, 'User': User}


manager.add_command('db', manager_db)
manager.add_command('shell', Shell('Welcome to the "InDaRefrigerator"!', _make_context))


if __name__ == '__main__':
    manager.run()
