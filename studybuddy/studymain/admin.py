from asyncio import tasks
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Task

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]


class TaskAdmin(admin.ModelAdmin):
#to list out non-editable fields in admin website, write the field name in the bracket    
    readonly_fields=('create_time',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Task, TaskAdmin)