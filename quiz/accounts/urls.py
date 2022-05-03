from django.contrib import admin
from django.urls import path,include,re_path as url

from . import views
from accounts.views import(
    register_view,
    home,
)
urlpatterns = [
    path('register/',register_view),
    path('login/',views.login),
    path('otpverification/',views.otpverification,name="otp"),
    # url(r'^otpverification/', views.otpverification, name = 'otp')


]

