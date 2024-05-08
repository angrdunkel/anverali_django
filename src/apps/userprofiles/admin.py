from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile

@admin.register(User)
class ExtendedUserAdmin(UserAdmin):
    list_display = (
        'email', 'first_name',
        'last_name', 'is_staff', 'type', 'is_active'
    )
    search_fields = ("email", "first_name", "last_name")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
       'id', 'user', 'email', 'phone', 'address', 'experience'
    )
    list_display_links = ('id', 'user',)
    search_fields = (
        'phone', 'user__username', 'user__last_name', 'user__email'
    )

    def email(self, obj):
        return f'{obj.user.email}'
    def first_name(self, obj):
        return f'{obj.user.first_name}'
    def last_name(self, obj):
        return f'{obj.user.last_name}'
