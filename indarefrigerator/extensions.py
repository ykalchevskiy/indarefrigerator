from flask.ext.admin import Admin
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy


admin = Admin()
api = Api()
db = SQLAlchemy()
