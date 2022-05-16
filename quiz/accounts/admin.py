from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from .models import tempProfile
from .models import Account
# Register your models here.

class Accountadmin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff','is_verified','otp')
    search_fields=('email','username')
    readonly_fields=('id','date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Account,Accountadmin)
admin.site.register(tempProfile)
