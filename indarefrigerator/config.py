import os


class BaseConfig(object):
    PROJECT_DIR = os.path.dirname(__file__)
    REPO_DIR = os.path.dirname(PROJECT_DIR)

    DEBUG = True
    TESTING = False

    SECRET_KEY = 'adf43rofk-9dqd23dw'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/db.sqlite'.format(REPO_DIR)
    SQLALCHEMY_ECHO = False


class LocalConfig(BaseConfig):
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    TESTING = True
