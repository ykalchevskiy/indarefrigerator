from flask import Flask

from .config import LocalConfig
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


def create_app(config=None):
    app = Flask(__name__)
    configure_app(app, config)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_app(app, config=None):
    app.config.from_object(LocalConfig)
    app.config.update(config or {})


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
