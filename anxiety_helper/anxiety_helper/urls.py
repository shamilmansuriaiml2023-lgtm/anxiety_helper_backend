from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
def home(request):
    return HttpResponse("Backend Running Successfully")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # Authgit add .
    path("api/auth/", include("accounts.urls")),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Profile
    path("api/", include("accounts.profile_urls")),

    # Feature apps
    path("api/", include("mood.urls")),
    path("api/", include("panic.urls")),
    path("api/", include("journal.urls")),
    path("api/", include("emergency.urls")),
    path("api/", include("affirmations.urls")),
    path("api/", include("breathing.urls")),
    path("api/", include("chatbot.urls")),
    path("api/", include("dashboard.urls")),
]
