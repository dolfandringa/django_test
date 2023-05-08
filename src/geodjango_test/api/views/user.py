"""User API"""
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_json_api import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """auth user model serializer"""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "url", "username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["username", "email"]
