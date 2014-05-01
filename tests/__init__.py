from flask.ext.testing import LiveServerTestCase, TestCase

from indarefrigerator.app import create_app
from indarefrigerator.extensions import db


class InDaRefrigeratorTestAppMixin(object):

    def create_app(self):
        return create_app('indarefrigerator.config.TestingConfig')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class InDaTestCase(InDaRefrigeratorTestAppMixin, TestCase):
    pass


class InDaLiveServerTestCase(InDaRefrigeratorTestAppMixin, LiveServerTestCase):
    pass
