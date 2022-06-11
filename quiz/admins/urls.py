
from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [


    path('', views.admin,name="context"),
    path('leaders', views.leaders,name="context"),
    path('users', views.users,name="context"),
    path('questions', views.question,name="context"),







]
