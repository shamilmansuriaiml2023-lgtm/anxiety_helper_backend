from django.contrib import admin
from .models import Affirmation


@admin.register(Affirmation)
class AffirmationAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]
    search_fields = ["text"]
