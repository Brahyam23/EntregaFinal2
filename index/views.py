from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notice
from .forms import EditNotice, NewNotice
from user.models import Avatar
from random import randint


def index(request):

    notice = Notice.objects.all()
    value = randint(11, 100)

    try:
        avatar = Avatar.objects.filter(user=request.user).first()
        return render(request, 'index/index.html', {'notices': notice, 'avatar': avatar.avatar.url, 'value': value})

    except:
        return render(request, 'index/index.html', {'notices': notice, 'value': value})


@login_required
def new_notice(request):

    if request.method == 'GET':
        form = NewNotice()
        return render(request, 'index/new_notice.html', {'form': form})

    else:
        form = NewNotice(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            new_notice = Notice(title=data.get("title"),
                                description=data.get("description"),
                                image=data.get("image"),
                                url=data.get("url"),
                                created_by=request.user.username)
            new_notice.save()

            return redirect("index")
        return render(request, 'index/new_notice.html', {'form': form})


@ login_required
def edit_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)

    if request.method == 'GET':
        form = EditNotice(initial={"title": notice.title,
                                   "description": notice.description,
                                   "url": notice.url,
                                   "image": notice.image})
        return render(request, 'index/edit_notice.html', {'form': form, 'notice': notice})
    else:
        form = EditNotice(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            notice.title = data.get('title')
            notice.description = data.get('description')
            notice.image = data.get('image')
            notice.url = data.get('url')

            notice.save()
            return redirect('index')
        return render(request, 'index/edit_notice.html', {'form': form, 'notice': notice})


@ login_required
def del_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)

    notice.delete()

    return redirect('index')


def not_found(request):
    return render(request, 'index/404.html')


def routes(request):
    return render(request, 'index/routes.html')


def about(request):
    return render(request, 'index/about.html')
