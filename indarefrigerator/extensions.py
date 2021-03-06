from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.heroku import Heroku
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


admin = Admin()
api = APIManager()
bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
heroku = Heroku()
