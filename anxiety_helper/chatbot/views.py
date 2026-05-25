from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


RESPONSES = {
    "anxious": (
        "Take a slow, deep breath. You are safe right now. "
        "Anxiety is uncomfortable, but it is not dangerous. "
        "Try breathing in for 4 counts, holding for 4, and exhaling for 4. "
        "This feeling will pass — it always does."
    ),
    "panic": (
        "You are safe. Look around and name 5 things you can see, "
        "4 things you can touch, 3 things you can hear, 2 things you can smell, "
        "and 1 thing you can taste. Grounding yourself in the present moment "
        "will help this feeling pass."
    ),
    "sad": (
        "I hear you — feeling sad is hard. It's okay to feel this way. "
        "Be gentle with yourself. Consider reaching out to someone you trust, "
        "or writing your feelings in your journal. You are not alone."
    ),
    "stress": (
        "Stress is your body's way of responding to demands. "
        "Try taking a short break, stretching, or doing a breathing exercise. "
        "You don't have to handle everything at once."
    ),
    "help": (
        "I'm here for you. You can log your mood, record a panic session, "
        "write in your journal, or try a breathing exercise. "
        "Remember — asking for help is a sign of strength."
    ),
}

GENERIC_RESPONSE = (
    "Thank you for sharing that with me. Remember, you are not alone. "
    "Whatever you're feeling right now is valid. "
    "Take a moment to breathe, and know that brighter moments are ahead. "
    "You are doing better than you think."
)


def get_rule_based_reply(message: str) -> str:
    message_lower = message.lower()
    for keyword, reply in RESPONSES.items():
        if keyword in message_lower:
            return reply
    return GENERIC_RESPONSE


class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message", "").strip()
        if not message:
            return Response(
                {"detail": "A 'message' field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        reply = get_rule_based_reply(message)
        return Response({"reply": reply})
