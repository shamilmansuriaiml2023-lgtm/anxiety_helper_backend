from django.contrib import admin
from .models import EmergencyContact


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ["name", "relationship", "phone_number", "user"]
    search_fields = ["name", "user__email"]
