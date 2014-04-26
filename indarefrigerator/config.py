import os


class BaseConfig(object):
    PROJECT_DIR = os.path.dirname(__file__)
    REPO_DIR = os.path.dirname(PROJECT_DIR)

    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ['FLASK_SECRET_KEY']

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/db.sqlite'.format(REPO_DIR)
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
