"""Profile View"""
import logging

from rest_framework import generics, permissions

from geodjango_test.api.views.user import UserSerializer

logger = logging.getLogger(__name__)


class ProfileView(generics.RetrieveAPIView):
    """Profile view"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
