from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('del/', del_user, name='del_user'),
]
