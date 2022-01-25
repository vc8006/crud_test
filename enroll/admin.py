from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')