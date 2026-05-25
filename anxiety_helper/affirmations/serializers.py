from rest_framework import serializers
from .models import Affirmation


class AffirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affirmation
        fields = ["id", "text"]
