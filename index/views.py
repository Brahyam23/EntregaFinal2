from django.shortcuts import render
from .models import Notice


def index(request):
    notice = Notice.objects.all()
    return render(request, 'index/index.html', {'notices': notice})
