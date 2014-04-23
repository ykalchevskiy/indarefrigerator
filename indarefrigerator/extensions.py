from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


admin = Admin()
api = Api()
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
