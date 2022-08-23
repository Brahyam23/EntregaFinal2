from http.client import HTTPResponse
from xml.dom import UserDataHandler
from django.shortcuts import render, redirect
from .forms import Register
# Formularios para iniciar sesion o registrar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Funciones para autenticar e iniciar sesion
from django.contrib.auth import login, authenticate


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
                return render(request, "user/login.html", {"error": "Incorrect credentials", "form": form})
        else:
            form = AuthenticationForm()
            return render(request, "user/login.html", {"error": "Invalid form", "form": form})


def new_user(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'user/register.html', {"form": form})
    else:
        form = UserCreationForm(request.POST)  # Posiblemente traiga problemas
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "user/register.html", {"error": "Invalid form or already exist"})
