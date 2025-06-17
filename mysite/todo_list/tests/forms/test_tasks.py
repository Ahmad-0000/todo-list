from django.test import TestCase
from django.forms import ModelForm, CharField, DateTimeField
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

    def test_task_form_fields(self):
        """
        TaskForm fields are title, description and
        deadline, with types CharField, CharField and
        DateTimeField respectively.
        """
        tf = TaskForm()
        self.assertEqual(len(tf.fields.keys()), 3)
        self.assertIn('title', tf.fields.keys())
        self.assertIn('description', tf.fields.keys())
        self.assertIn('deadline', tf.fields.keys())
        self.assertIsInstance(tf.fields['title'], CharField)
        self.assertIsInstance(tf.fields['description'], CharField)
        self.assertIsInstance(tf.fields['deadline'], DateTimeField)
