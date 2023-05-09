"""Api urls"""
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_json_api.schemas.openapi import SchemaGenerator

from .views import AddressViewSet, PersonViewSet, UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("person", PersonViewSet)
router.register("address", AddressViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "openapi",
        get_schema_view(
            title="ZUoS API",
            description="API for all things …",
            version="1.0.0",
            generator_class=SchemaGenerator,
        ),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
