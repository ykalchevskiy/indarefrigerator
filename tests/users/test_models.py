from indarefrigerator.extensions import db
from indarefrigerator.users.models import User

from tests import InDaRefrTestCase


class UserModelTest(InDaRefrTestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_user(self):
        user_data = {
            'username': 'Test',
            'password': 'Testson',
        }
        user = User.create(**user_data)
        self.assertTrue(user.id)
        self.assertEquals(user.username, user_data['username'])
        self.assertEquals(user.password, user_data['password'])

    def test_save_user(self):
        user_data = {
            'username': 'Test',
            'password': 'Testson',
        }
        user_username = 'Notest'
        user = User.create(**user_data)
        user.username = user_username
        user.save()

        check_user = User.get(user.id)
        self.assertEquals(check_user.username, user_username)

    def test_delete_user(self):
        user_data = {
            'username': 'Test',
            'password': 'Testson',
        }
        user = User.create(**user_data)
        user_id = user.id
        user.delete()

        none_user = User.get(user_id)
        self.assertFalse(none_user)
