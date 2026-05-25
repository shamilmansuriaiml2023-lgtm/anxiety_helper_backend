from django.contrib import admin
from .models import BreathingExercise


@admin.register(BreathingExercise)
class BreathingExerciseAdmin(admin.ModelAdmin):
    list_display = ["title", "inhale_seconds", "hold_seconds", "exhale_seconds", "repeat_count"]
