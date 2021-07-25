from django import forms
from .models import *
from django.forms.widgets import TextInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = "__all__"
        widgets = {
                'title': TextInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 50%',
                    'placeholder': 'Add tasks to list'
                })
        }