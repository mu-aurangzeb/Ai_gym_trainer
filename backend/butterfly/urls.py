from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('butterfly', views.butterfly, name='butterfly'),
]