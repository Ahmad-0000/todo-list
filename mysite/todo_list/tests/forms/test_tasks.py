from django.test import TestCase
from django.forms import ModelForm
from ...forms import TaskForm

class TestTaskForm(TestCase):
    """
    Test tasks model form
    """
    def test_task_form_parent_class(self):
        """
        TaskForm is a subclass of ModelForm
        """
        self.assertIsInstance(TaskForm(), ModelForm)
