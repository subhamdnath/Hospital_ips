from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from home.models import *



class UserAdmin(BaseUserAdmin):

    list_display = ["first_name", "last_name", "email", "phone_number", "role_id", "is_superuser"]
    list_filter = ["is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "phone_number", "role_id"]}),
        ("Permissions", {"fields": ["is_superuser"]}),
    ]
  
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["first_name", "last_name", "email", "phone_number", "role_id", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)