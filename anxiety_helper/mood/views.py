from rest_framework import viewsets
from .models import MoodEntry
from .serializers import MoodEntrySerializer


class MoodEntryViewSet(viewsets.ModelViewSet):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodEntrySerializer