from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BreathingExercise
from .serializers import BreathingExerciseSerializer


class BreathingExerciseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BreathingExerciseSerializer
    permission_classes = [IsAuthenticated]
    queryset = BreathingExercise.objects.all()
