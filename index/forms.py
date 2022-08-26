from django import forms
from django.utils import timezone
from .models import Notice


class NewNotice(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    description = forms.CharField(max_length=500, label="Description")
    image = forms.ImageField(label="Image")
    url = forms.URLField(label="URL")

    class Meta:
        model = Notice
        fields = ["title", "description", "image", "url"]
        help_texts = {"title": "You can't' exceed 100 characters",
                      "description": "You can't exceed 500 characters"}


class EditNotice(forms.Form):

    title = forms.CharField(max_length=100, label="New title")
    description = forms.CharField(max_length=500, label="New description")
    image = forms.ImageField(label="New image")
    url = forms.URLField(label="New URL")

    class Meta:
        model = Notice
        fields = ["title", "description", "image", "url"]
        help_texts = {"title": "You can't' exceed 100 characters",
                      "description": "You can't exceed 500 characters"}
