import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Affirmation
from .serializers import AffirmationSerializer


class RandomAffirmationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Affirmation.objects.count()
        if count == 0:
            return Response(
                {"detail": "No affirmations available."},
                status=status.HTTP_404_NOT_FOUND,
            )
        random_index = random.randint(0, count - 1)
        affirmation = Affirmation.objects.all()[random_index]
        serializer = AffirmationSerializer(affirmation)
        return Response(serializer.data)
