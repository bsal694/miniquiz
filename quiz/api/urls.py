from django.contrib import admin
from django.urls import path,include
from . import views
from .views import RegisterAPI
urlpatterns = [
    path("register/",views.RegisterAPI),
]
