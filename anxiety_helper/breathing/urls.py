from rest_framework.routers import DefaultRouter
from .views import BreathingExerciseViewSet

router = DefaultRouter()
router.register(r"breathing-exercises", BreathingExerciseViewSet, basename="breathing-exercise")

urlpatterns = router.urls
