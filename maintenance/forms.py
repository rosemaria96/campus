from django import forms

from .models import MaintenanceRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RequestForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = [
            'title', 'description', 'category', 'location', 'priority'
        ]