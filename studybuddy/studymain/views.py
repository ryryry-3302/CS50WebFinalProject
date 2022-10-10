from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import CustomUser, Task
from .forms import CustomUserCreationForm, TaskForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone

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

@login_required
def todolist(request):
    if request.method == "GET":
        tasks = Task.objects.filter(poster=request.user).all()
        form = TaskForm(request.POST or None, request.FILES or None)

        return render(request, "studymain/todolist.html", {
            'tasks' : tasks,
            'today' : timezone.now(),
            'form'  : form
        })

@login_required
def createtask(request):
    if request.method == "POST":
        f = TaskForm(request.POST, request.FILES)
        if f.is_valid():
        # save the form data to model
            result = f.save(commit=False)
            result.poster = request.user
            result.save()
        return HttpResponseRedirect(reverse("todo"))

@login_required
@csrf_exempt
def edittask(request, task_id):

    try:
        task = Task.objects.get(poster=request.user, pk=task_id)
    except task.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("title") is not None:
            task.title = data["title"]
        if data.get("body") is not None:
            task.body = data["body"]
        task.save()
        return HttpResponse(status=204)

@login_required
@csrf_exempt
def completetask(request, task_id):
    try:
        task = Task.objects.get(poster=request.user, pk=task_id)

    except task.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("done") is not None:
            task.done = data["done"]
        task.save()
        return HttpResponse(status=204)