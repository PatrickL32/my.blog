from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = [
        "username", "email", "role", "is_staff"
    ]
    add_fieldsets = (
        (
            None, {
                "classes": ("wide", ),
                "fields": ("email", "role", "password1", "password2"),
            }
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", )}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
