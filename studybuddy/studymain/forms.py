from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.admin.widgets import AdminSplitDateTime

from .models import CustomUser, Task



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class TaskForm(ModelForm):
    

    class Meta:
        model = Task
        fields = ['title', 'body', 'due_date']
        widgets = {
            'due_date' : AdminSplitDateTime()
        }
        

    