from rest_framework import viewsets
from .models import EmergencyContact
from .serializers import EmergencyContactSerializer


class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer