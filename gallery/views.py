from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewImage
from .models import Image


def gallery(request):
    image = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'images': image})


@login_required
def add_image(request):

    if request.method == 'GET':
        form = NewImage()
        return render(request, 'gallery/add_image.html', {'form': form})

    else:
        form = NewImage(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            new_image = Image(image=data.get("image"))
            new_image.save()

            return redirect("gallery")
        return render(request, 'gallery/new_image.html', {'form': form})


@ login_required
def edit_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    if request.method == 'GET':
        form = NewImage(initial={"image": image.image})
        return render(request, 'gallery/edit_image.html', {'form': form, 'image': image})
    else:
        form = NewImage(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            image.image = data.get('image')
            image.save()

            return redirect('gallery')
        return render(request, 'gallery/edit_image.html', {'form': form, 'image': image})


@ login_required
def del_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    image.delete()

    return redirect('gallery')
