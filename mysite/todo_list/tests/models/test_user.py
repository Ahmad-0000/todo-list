from django.test import TestCase
from django.core.exceptions import ValidationError
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
