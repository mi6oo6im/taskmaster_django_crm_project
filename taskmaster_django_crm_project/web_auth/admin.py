from django.contrib import admin
from .models import AppUser, Profile


# Register your models here.
@admin.register(AppUser)
class AuthAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
