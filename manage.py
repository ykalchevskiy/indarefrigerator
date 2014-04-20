#!/usr/bin/env python

from flask.ext.script import Manager

from indarefrigerator import create_app
from indarefrigerator.extensions import db


app = create_app()
manager = Manager(app)


@manager.command
def runserver():
    """Run dev server."""

    app.run()


@manager.command
def initdb():
    """Init/reset db."""

    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
