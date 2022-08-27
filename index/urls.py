from django.urls import path
from .views import *

urlpatterns = [
    path('new/', new_notice, name='new_notice'),
    path('edit/<int:notice_id>', edit_notice, name='edit_notice'),
    path('del/<int:notice_id>', del_notice, name='del_notice'),
]
