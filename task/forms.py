from django import forms
from datetime import date
from .models import Task

class TaskForm(forms.ModelForm):
    title =  forms.CharField(required=False)
    description = forms.CharField(required=False)
    due_date = forms.CharField(required=False)

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')