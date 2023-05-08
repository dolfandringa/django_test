"""Person api"""
from django_property_filter import PropertyCharFilter, PropertyFilterSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_json_api import serializers

from geodjango_test.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """Person model serializer"""

    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Person
        fields = ["url", "first_name", "last_name", "email"]


class PersonFilterSet(PropertyFilterSet):
    class Meta:
        model = Person
        exclude = ["_email", "_firstname", "_lastname"]
        property_fields = [
            ("first_name", PropertyCharFilter, ["contains"]),
            ("last_name", PropertyCharFilter, ["contains"]),
            ("email", PropertyCharFilter, ["contains"]),
        ]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["first_name", "last_name", "email"]
    filterset_class = PersonFilterSet
