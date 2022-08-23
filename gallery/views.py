from django.shortcuts import render
from .models import Image


def new_image(request):
    image = Image.objects.all()
    return render(request, 'gallery/images.html', {'images': image})
