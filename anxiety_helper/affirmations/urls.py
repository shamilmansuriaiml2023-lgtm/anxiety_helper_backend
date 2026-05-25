from django.urls import path
from .views import RandomAffirmationView

urlpatterns = [
    path("affirmations/random/", RandomAffirmationView.as_view(), name="random-affirmation"),
]
