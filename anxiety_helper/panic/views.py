from rest_framework import viewsets
from .models import PanicSession
from .serializers import PanicSessionSerializer


class PanicSessionViewSet(viewsets.ModelViewSet):
    queryset = PanicSession.objects.all()
    serializer_class = PanicSessionSerializer