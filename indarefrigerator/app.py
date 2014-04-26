import os

from flask import Flask

from .extensions import (
    admin,
    api,
    bcrypt,
    db,
    login_manager,
)
from .products import product
from .users import user, User


BLUEPRINTS = (
    product,
    user,
)


def create_app(config_object=None):
    app = Flask(__name__)
    configure_app(app, config_object)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_app(app, config_object):
    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(os.environ['FLASK_APP_CONFIG'])


def configure_blueprints(app):
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)


def configure_extensions(app):
    admin.init_app(app)
    api.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
