from django.db import models
from django.conf import settings


class MoodEntry(models.Model):
    MOOD_CHOICES = [
        ("very_happy", "Very Happy"),
        ("happy", "Happy"),
        ("neutral", "Neutral"),
        ("anxious", "Anxious"),
        ("sad", "Sad"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mood_entries")
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    trigger = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.email} – {self.mood} ({self.created_at.date()})"
