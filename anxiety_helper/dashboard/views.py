from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from mood.models import MoodEntry
from mood.serializers import MoodEntrySerializer
from journal.models import JournalEntry
from journal.serializers import JournalEntrySerializer
from emergency.models import EmergencyContact
from panic.models import PanicSession


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Latest mood entry
        latest_mood_qs = MoodEntry.objects.filter(user=user).order_by("-created_at").first()
        latest_mood = MoodEntrySerializer(latest_mood_qs).data if latest_mood_qs else None

        # 5 most recent journal entries (title + date only)
        recent_journal_qs = JournalEntry.objects.filter(user=user).order_by("-created_at")[:5]
        recent_journal = JournalEntrySerializer(recent_journal_qs, many=True).data

        # Counts
        emergency_count = EmergencyContact.objects.filter(user=user).count()
        panic_count = PanicSession.objects.filter(user=user).count()

        return Response(
            {
                "latest_mood": latest_mood,
                "recent_journal_entries": recent_journal,
                "emergency_contacts_count": emergency_count,
                "panic_sessions_count": panic_count,
            }
        )
