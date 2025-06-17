from django import forms
from . import models

class TaskForm(forms.ModelForm):
    """
    Task model form
    """
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
