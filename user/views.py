from http.client import HTTPResponse
from xml.dom import UserDataHandler
from django.shortcuts import render, redirect
# Formularios para iniciar sesion o registrar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Funciones para autenticar e iniciar sesion
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import Register, Edit
from django.contrib.auth.models import User


def log_in(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, "user/login.html", {'form': form})
    else:
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get(
                "username"), password=data.get("password"))

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form = AuthenticationForm()
                return render(request, "user/login.html", {"error": "Incorrect password or username", "form": form})
        else:
            form = AuthenticationForm()
            return render(request, "user/login.html", {"error": "Incorrect password or username", "form": form})


def new_user(request):
    form = Register()
    if request.method == 'GET':
        return render(request, 'user/register.html', {'form': form})
    else:
        form = Register(request.POST)  # Posiblemente traiga problemas
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "user/register.html", {'error': 'Invalid form or already exist', 'form': form})


@login_required
def profile(request):
    if request.method == 'GET':
        form = Edit(initial={"email": request.user.email})
        return render(request, 'user/profile.html', {'form': form})
    else:
        form = Edit(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = request.user

            user.email = data['email']
            user.password1 = data['password1']
            user.password2 = data['password2']
            user.save()
            return redirect('index')
        return render(request, 'user/profile.html', {'form': form})


@ login_required
def del_user(request):

    user = User.objects.get(id=request.user.id)

    user.delete()

    return redirect('index')
