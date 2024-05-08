from django.contrib import admin
from django import forms

from .models import Task, TaskRoom

class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title', 'comment', 'is_active', 'is_complite'
        ]

class TaskRoomInline(admin.TabularInline):
    model = TaskRoom
    extra = 0

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    inlines = [
        TaskRoomInline,
    ]
    list_display = ('title', 'created_at', 'is_active', 'is_complite')

@admin.register(TaskRoom)
class TaskRoomAdmin(admin.ModelAdmin):
    list_display = ('task', 'customer', 'performer')