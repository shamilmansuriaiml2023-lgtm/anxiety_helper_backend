from django.db import models


class Affirmation(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:80]
