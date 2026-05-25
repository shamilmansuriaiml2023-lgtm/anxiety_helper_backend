from django.core.management.base import BaseCommand
from affirmations.models import Affirmation
from breathing.models import BreathingExercise


AFFIRMATIONS = [
    "You are safe.",
    "This feeling will pass.",
    "Breathe in calm, breathe out fear.",
    "You are stronger than you think.",
    "You are not alone in this.",
    "It's okay to feel anxious. You can still move forward.",
    "You have overcome hard times before.",
    "Your feelings are valid, and they will pass.",
    "One breath at a time.",
    "You are enough, exactly as you are.",
    "Be gentle with yourself today.",
    "You are doing the best you can.",
    "This moment will not last forever.",
    "You deserve peace and calm.",
    "You are worthy of love and support.",
    "Let go of what you cannot control.",
    "Every small step forward matters.",
    "You have the strength to get through this.",
    "Calm is just one breath away.",
    "Choose progress over perfection.",
]

BREATHING_EXERCISES = [
    {
        "title": "4-4-4 Breathing",
        "inhale_seconds": 4,
        "hold_seconds": 4,
        "exhale_seconds": 4,
        "repeat_count": 5,
        "description": (
            "Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds. "
            "This balanced breathing technique helps reduce acute stress and anxiety."
        ),
    },
    {
        "title": "Box Breathing",
        "inhale_seconds": 4,
        "hold_seconds": 4,
        "exhale_seconds": 4,
        "repeat_count": 4,
        "description": (
            "Used by Navy SEALs and athletes. Inhale for 4 seconds, hold for 4 seconds, "
            "exhale for 4 seconds, hold empty for 4 seconds. Repeat 4 times."
        ),
    },
    {
        "title": "4-7-8 Breathing",
        "inhale_seconds": 4,
        "hold_seconds": 7,
        "exhale_seconds": 8,
        "repeat_count": 4,
        "description": (
            "A powerful relaxation technique. Inhale for 4 seconds, hold for 7 seconds, "
            "exhale slowly for 8 seconds. Activates the parasympathetic nervous system."
        ),
    },
]


class Command(BaseCommand):
    help = "Seed the database with affirmations and breathing exercises"

    def handle(self, *args, **options):
        # Affirmations
        created_count = 0
        for text in AFFIRMATIONS:
            _, created = Affirmation.objects.get_or_create(text=text)
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Affirmations: {created_count} created, {len(AFFIRMATIONS) - created_count} already existed."))

        # Breathing exercises
        created_count = 0
        for exercise_data in BREATHING_EXERCISES:
            _, created = BreathingExercise.objects.get_or_create(
                title=exercise_data["title"],
                defaults=exercise_data,
            )
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Breathing exercises: {created_count} created, {len(BREATHING_EXERCISES) - created_count} already existed."))

        self.stdout.write(self.style.SUCCESS("Seed data loaded successfully!"))
