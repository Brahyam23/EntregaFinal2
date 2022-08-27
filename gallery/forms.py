from django import forms
from .models import Image


class NewImage(forms.Form):
    image = forms.ImageField(label='Select Image')

    class Meta:
        model = Image
        fields = ['image']
