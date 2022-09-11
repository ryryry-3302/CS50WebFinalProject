from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse

def register(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)
    f = CustomUserCreationForm(request.POST, request.FILES)
    if f.is_valid():
        # save the form data to model
        result = f.save()

    if request.method == "POST":

        

        # Check if authentication successful
        if f is not None:
            username = request.POST["username"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    
    return render(request, 'studymain/register.html', {
        "form" : form,
    }
    )

def index(request):
    if request.user.is_authenticated:
        message = request.user
        return render(request, 'studymain/index.html', {
            "message" : message
        }
        )
    
    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def logout_lol(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def login_lol(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "studymain/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "studymain/login.html")

def todolist(request):
    if request.method == "GET":
        return render(request, "studymain/todolist.html")