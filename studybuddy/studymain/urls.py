
from django.urls import path
from requests import post
from django.views.i18n import JavaScriptCatalog

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_lol, name="logout"),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path("login", views.login_lol, name="login"),
    path("todolist", views.todolist, name="todo"),
    path("createtask", views.createtask, name="CreateTask"),
    path("edittask/<int:task_id>", views.edittask, name="edittask"),
    path("completetask/<int:task_id>", views.completetask, name="completetask"),
    path("find", views.find, name="find"),
]

