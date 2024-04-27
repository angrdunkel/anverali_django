from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    list_display = (
        'email', 'first_name',
        'last_name', 'is_staff', 'type', 'is_active'
    )
    search_fields = ("email", "first_name", "last_name")