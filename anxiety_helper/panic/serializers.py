from rest_framework import serializers
from .models import PanicSession


class PanicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanicSession
        fields = ["id", "intensity", "trigger", "duration_minutes", "notes", "created_at"]
        read_only_fields = ["id", "created_at"]
