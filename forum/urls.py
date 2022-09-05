from django.urls import path
from .views import *

urlpatterns = [
    path('', forum, name='forum'),
    path('new_post/', new_post, name='new_post'),
    path('edit/<int:post_id>', edit_post, name='edit_post'),
    path('del/<int:post_id>', del_post, name='del_post'),
    path('<int:post_id>/', post_detail, name='post_detail')
]
