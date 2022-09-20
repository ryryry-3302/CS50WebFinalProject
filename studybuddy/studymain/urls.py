
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
    path("todolist", views.todolist, name="todo")
]
