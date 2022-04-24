from django.contrib import admin

# Register your models here.

from . models import *

admin.site.register(Category)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(follower)



class Answeradmin(admin.StackedInline):
    model=Answer
class QuestionAdmin(admin.ModelAdmin):
    inlines=[Answeradmin]


