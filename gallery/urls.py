from django.urls import path
from .views import *

urlpatterns = [
    path('', gallery, name='gallery'),
    path('add/', add_image, name='add_image'),
    path('edit/<int:image_id>', edit_image, name='edit_image'),
    path('del/<int:image_id>', del_image, name='del_image'),
]
