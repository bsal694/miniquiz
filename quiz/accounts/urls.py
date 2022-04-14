from django.contrib import admin
from django.urls import path,include
from . import views
from accounts.views import(
    register_view,
    home,
)
urlpatterns = [
    path('register/',register_view,name="register"),
    path('login/',views.login),

    path('',home,name="home")

]

