import os


class BaseConfig(object):
    PROJECT_DIR = os.path.dirname(__file__)
    REPO_DIR = os.path.dirname(PROJECT_DIR)

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ['FLASK_SECRET_KEY']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/db.sqlite'.format(BaseConfig.REPO_DIR)
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    LIVESERVER_PORT = 5005
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
