# For tenant-specific schemas
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Tenant API Documentation",
        default_version='v1',
        description="Tenant-specific endpoints",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api-tenant/', include('school.urls')),
    path('swagger/tenant/', schema_view.with_ui('swagger', cache_timeout=0), name='tenant-schema-swagger'),
]