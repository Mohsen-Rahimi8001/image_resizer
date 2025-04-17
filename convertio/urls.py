from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/docs/', SpectacularSwaggerView.as_view(), name="docs"),
    path('token/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/', TokenRefreshView.as_view(), name="refresh"),
    path('image/', include("converter.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
