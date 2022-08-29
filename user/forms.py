from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):

    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User

        fields = ["first_name", "last_name", "email",
                  "username", "password1", "password2"]
        help_texts = {"email": "", "password1": "", "password2": ""}


class Edit(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(
        label="New password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm new password", widget=forms.PasswordInput)
    avatar = forms.ImageField(label="New avatar")

    class Meta:
        model = User

        fields = ["email", "password1", "password2", "avatar"]
        help_texts = {"email": "", "password1": "", "password2": ""}
