from django.db import models


class BreathingExercise(models.Model):
    title = models.CharField(max_length=100)
    inhale_seconds = models.PositiveIntegerField()
    hold_seconds = models.PositiveIntegerField()
    exhale_seconds = models.PositiveIntegerField()
    repeat_count = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
