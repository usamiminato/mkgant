from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'user', 'progress', 'to_be_start_date', 'to_be_complete_date', 'memo', 'complete_date')
