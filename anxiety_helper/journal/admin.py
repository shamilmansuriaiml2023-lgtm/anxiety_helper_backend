from django.contrib import admin
from .models import JournalEntry


@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "created_at", "updated_at"]
    search_fields = ["user__email", "title"]
    list_filter = ["created_at"]
