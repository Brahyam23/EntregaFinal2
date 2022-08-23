from django.urls import path
from forum.views import *

urlpatterns = [
    path('', forum, name='forum'),
    path('new_post/', new_post, name='new_post')
]
