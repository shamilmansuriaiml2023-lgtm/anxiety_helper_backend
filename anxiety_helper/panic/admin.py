from django.contrib import admin
from .models import PanicSession


@admin.register(PanicSession)
class PanicSessionAdmin(admin.ModelAdmin):
    list_display = ["user", "intensity", "duration_minutes", "trigger", "created_at"]
    list_filter = ["intensity", "created_at"]
    search_fields = ["user__email", "trigger"]
