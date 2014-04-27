#!/usr/bin/env python
""" Useful project commands.

See list of available commands by './manage.py -h'.
"""

import sys
import unittest

from flask.ext.script import Manager, prompt_bool, Shell

import flake8.main as flake8

from indarefrigerator.app import create_app
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
def create_superuser(email, password):
    """Creates a new user."""

    User.create(email=email, password=password, is_admin=True)


@manager.command
def lint():
    """Runs flake8."""

    sys.argv = [None, '.']
    flake8.main()


@manager.command
def tests():
    """Runs tests."""

    loader = unittest.TestLoader()
    test_runner = unittest.TextTestRunner()
    test_runner.run(loader.discover('tests'))


def _make_context():
    """Returns variables will be available in shell by default."""

    return {'app': app, 'db': db, 'Product': Product, 'User': User}


manager.add_command('db', manager_db)
shell = Shell('Welcome to the "InDaRefrigerator"!', _make_context)
manager.add_command('shell', shell)


if __name__ == '__main__':
    manager.run()
