from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AniUser

admin.site.register(AniUser, UserAdmin)
