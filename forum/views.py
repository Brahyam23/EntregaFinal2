from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import EditPost


def forum(request):
    post = Post.objects.all()

    if request.GET.get("post_title"):

        post = Post.objects.filter(
            title__icontains=request.GET.get("post_title"))
        return render(request, "forum/forum.html", {'posts': post})

    else:
        return render(request, "forum/forum.html", {'posts': post})


@login_required
def new_post(request):

    if request.method == 'GET':
        return render(request, 'forum/new_post.html')

    else:
        formulary = request.POST

        title = formulary.get("title")
        description = formulary.get("description")
        created_by = request.user.username

        new_post = Post(title=title, description=description,
                        created_by=created_by)
        new_post.save()

        return redirect("forum")


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'GET':
        form = EditPost(initial={"title": post.title,
                        "description": post.description})
        return render(request, 'forum/edit_post.html', {'form': form, 'post': post})
    else:
        form = EditPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            post.title = data.get('title')
            post.description = data.get('description')

            post.save()
            return redirect('forum')
        return render(request, 'forum/edit_post.html', {'form': form, 'post': post})


@login_required
def del_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    return redirect('forum')
