
from django.urls import path
from requests import post

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
