from django.db import models
from django.conf import settings


class EmergencyContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emergency_contacts")
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.relationship}) – {self.user.email}"
