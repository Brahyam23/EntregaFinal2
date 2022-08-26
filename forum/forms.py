from django import forms
from django.utils import timezone
from .models import Post


class EditPost(forms.Form):

    title = forms.CharField(max_length=100, label="New title")
    description = forms.CharField(max_length=500, label="New description")

    class Meta:
        model = Post
        fields = ["title", "description"]
        help_texts = {"title": "You can't' exceed 100 characters",
                      "description": "You can't exceed 500 characters"}
