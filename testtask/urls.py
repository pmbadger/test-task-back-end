"""
URL configuration for testtask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from asyncio import tasks

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view
from profiles.views import ProfileDetailView, CurrentProfileDetailView


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Test Task", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path("admin/", admin.site.urls),
    path("api/auth/", include("profiles.urls")),
    path("api/products/", include("products.urls")),
    path("api/profiles/<int:pk>", ProfileDetailView.as_view(), name="profile"),
    path("api/profiles/me", CurrentProfileDetailView.as_view(), name="current-profile"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
