from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class PanicSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="panic_sessions")
    intensity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    trigger = models.CharField(max_length=255, blank=True)
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.email} – intensity {self.intensity} ({self.created_at.date()})"
