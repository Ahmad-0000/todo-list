from datetime import timedelta
from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import DataError
from ...models import User, Task

class TestTaskModel(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Initialize the class
        """
        super().setUpClass()
        cls.user = User(name="ahmad", email="ahmadhusain5002@gmail.com", password="random")
        cls.user.save()
        cls.now = timezone.now()

    def test_normal_task(self):
        """
        Test normal task creation
        """
        task = Task(
            user=self.user,
            title="Test task",
            description="I'm using this task as a test",
            add_date=self.now,
            deadline=self.now + timedelta(days=3),
            done_date=None
        )
        task.full_clean() # Test if valid
        task.save() # Test if database-level valid
        self.assertIs(task.user, self.user)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "I'm using this task as a test")
        self.assertEqual(task.add_date, self.now)
        self.assertEqual(task.deadline, self.now + timedelta(days=3))
        self.assertEqual(task.done_date, None)

    def test_task_with_long_title(self):
        """
        Tasks with titles longer than 100 characters are not allowed
        """
        task = Task(
            user=self.user,
            title="a"*101,
            description="I'm using this task as a test",
            add_date=self.now,
            deadline=self.now + timedelta(days=3),
            done_date=None
        )
        with self.assertRaises(ValidationError):
            task.full_clean()
        with self.assertRaises(DataError):
            task.save()
