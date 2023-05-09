"""Person api"""
from django_property_filter import PropertyCharFilter, PropertyFilterSet
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from geodjango_test.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """Person model serializer"""

    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    addresses = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ["url", "first_name", "last_name", "email", "addresses"]


class PersonFilterSet(PropertyFilterSet):
    first_name = PropertyCharFilter(field_name="first_name", lookup_expr="contains")
    last_name = PropertyCharFilter(field_name="last_name", lookup_expr="contains")
    email = PropertyCharFilter(field_name="email", lookup_expr="contains")

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["first_name", "last_name", "email"]
    filterset_class = PersonFilterSet
