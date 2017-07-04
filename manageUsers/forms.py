from django import forms
from django.contrib.auth.models import User
from authentication.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        ]
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "password": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "email": forms.EmailInput(attrs={'class': 'form-control ppap-form-field'}),
        }