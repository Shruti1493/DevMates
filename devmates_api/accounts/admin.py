from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class User_Profile(admin.ModelAdmin):

    list_display = ("email","username","get_full_name","phone")
    ordering = ("email", "username", "phone")
