"""User API"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_json_api import serializers

from geodjango_test.models import Address


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """Address model serializer"""

    class Meta:
        model = Address
        fields = [
            "street",
            "city",
            "zipcode",
        ]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["street", "city", "zipcode"]
