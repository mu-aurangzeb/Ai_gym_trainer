from importlib.resources import path
from unicodedata import name
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path("",views.index,name="index")
]