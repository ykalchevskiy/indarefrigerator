from flask import Flask

from .config import LocalConfig
from .extensions import admin, api, db
from .products import product


BLUEPRINTS = (
    product,
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
    db.init_app(app)
