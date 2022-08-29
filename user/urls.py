from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView

urlpatterns = [
    path('register/', new_user, name='register'),
    path('login/', log_in, name='login'),
    path('profile/', profile, name='profile'),
    path('del/', del_user, name='del_user'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path('reset/', PasswordResetView.as_view(template_name='user/password_reset_form.html',
         email_template_name="user/password_reset_email.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),

]
