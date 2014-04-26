from flask.ext.testing import TestCase

from indarefrigerator import create_app


class InDaRefrTestCase(TestCase):

    def create_app(self):
        return create_app('indarefrigerator.config.TestConfig')
