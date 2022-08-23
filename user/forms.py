from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Register(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput)
    username = forms.CharField()

    class Meta:
        model = User
        fields = ["name", "email", "username", "password1", "password2"]
