from rest_framework import serializers
from .models import BreathingExercise


class BreathingExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BreathingExercise
        fields = ["id", "title", "inhale_seconds", "hold_seconds", "exhale_seconds", "repeat_count", "description"]
