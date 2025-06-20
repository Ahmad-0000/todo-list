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

    def test_invalid_email_patterns(self):
        """
        Invalid email patterns are not allowed
        """
        user = User(name="ahmad", email="ahmad", password="random")
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_vary_long_passwords(self):
        """
        Passwords with more than 100 characters are not allowed
        """
        user = User(name="ahmad", email="ahmadhusain5002@gmail.com", password="a"*101)
        with self.assertRaises(ValidationError):
            user.full_clean()
        with self.assertRaises(DataError):
            user.save()
