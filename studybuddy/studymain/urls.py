
from django.urls import path
from requests import post

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("logout", views.logout_lol, name="logout"),
    path("login", views.login_lol, name="login")
]
