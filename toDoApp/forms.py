from django import forms

from .models import Task


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "due", "tags"]
