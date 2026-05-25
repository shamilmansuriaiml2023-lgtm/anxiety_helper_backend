from django.contrib import admin
from .models import MoodEntry


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ["user", "mood", "trigger", "created_at"]
    list_filter = ["mood", "created_at"]
    search_fields = ["user__email", "trigger"]
