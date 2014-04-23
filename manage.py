#!/usr/bin/env python

from flask.ext.script import Manager

from indarefrigerator import create_app
from indarefrigerator.extensions import db
from indarefrigerator.users.utils import create_user


app = create_app()
manager = Manager(app)


@manager.command
def syncdb():
    """Init db."""

    db.create_all()


@manager.command
def new_user(username, password):
    create_user(username, password)


@manager.command
def runserver():
    """Run dev server."""

    app.run()


if __name__ == '__main__':
    manager.run()
