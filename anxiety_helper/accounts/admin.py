from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "username", "is_active", "created_at"]
    ordering = ["-created_at"]
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Metadata", {"fields": ("created_at",)}),
    )
    readonly_fields = ["created_at"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "age", "gender", "anxiety_level", "emergency_enabled"]
    list_filter = ["gender", "anxiety_level", "emergency_enabled"]
