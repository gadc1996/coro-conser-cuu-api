from django.urls import path, include
from core.views import api_root

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("auth/", include("auth.urls")),
    path("", api_root),
]
