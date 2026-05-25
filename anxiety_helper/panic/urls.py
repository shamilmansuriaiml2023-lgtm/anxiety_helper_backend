from rest_framework.routers import DefaultRouter
from .views import PanicSessionViewSet

router = DefaultRouter()
router.register(r"panic-sessions", PanicSessionViewSet, basename="panic-session")

urlpatterns = router.urls
