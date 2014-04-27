from sqlalchemy.exc import IntegrityError

from indarefrigerator.users.models import User

from tests import InDaTestCase


class UserModelTest(InDaTestCase):

    def test_create_user(self):
        user_data = {
            'email': 'test@test.com',
            'password': 'Testson',
        }
        user = User.create(**user_data)
        self.assertTrue(user.id)
        self.assertTrue(user.check_password(user_data['password']))
        self.assertEquals(user.email, user_data['email'])
        self.assertTrue(user.is_active())
        self.assertFalse(user.is_superuser())

    def test_create_superuser(self):
        user_data = {
            'email': 'test@test.com',
            'password': 'Testson',
            'is_admin': True
        }
        user = User.create(**user_data)
        self.assertTrue(user.is_superuser())

    def test_save_user(self):
        user_data = {
            'email': 'test@test.com',
            'password': 'Testson',
        }
        user_email = 'notest@notest.com'
        user = User.create(**user_data)
        user.email = user_email
        user.save()

        check_user = User.get(user.id)
        self.assertEquals(check_user.email, user_email)

    def test_delete_user(self):
        user_data = {
            'email': 'test@test.com',
            'password': 'Testson',
        }
        user = User.create(**user_data)
        user_id = user.id
        user.delete()

        none_user = User.get(user_id)
        self.assertFalse(none_user)

    def test_user_email_is_unique(self):
        user_data = {
            'email': 'test@test.com',
            'password': 'Testson',
        }
        User.create(**user_data)
        self.assertRaises(IntegrityError, User.create, **user_data)

    def test_user_email_is_correct_email(self):
        user_data = {
            'email': 'testtest.com',
            'password': 'Testson',
        }
        self.assertRaises(AssertionError, User.create, **user_data)
