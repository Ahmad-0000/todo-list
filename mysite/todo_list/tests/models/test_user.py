from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import DataError
from ...models import User

class UserModelTest(TestCase):
    """
    test User model
    """
    def test_new_user(self):
        """
        Test new user addition
        """
        user = User(name="Ahmad", email="ahmad.new.m.v@gmail.com", password="random")
        user.full_clean()
        user.save()
        self.assertEqual(User.objects.get(pk=user.id), user)

    def test_long_user_name(self):
        """
        User names with more than 20 characters are not allowed
        """
        user = User(name="a"*21, email="ahmad.new.m.v@gmail.com", password="random")
        with self.assertRaises(ValidationError):
            user.full_clean()
        with self.assertRaises(DataError):
            user.save()
