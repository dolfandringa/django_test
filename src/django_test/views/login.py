"""Login View"""
import logging

from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status, views
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import LoginSerializer

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(views.APIView):
    """Login view"""

    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    schema = None

    def post(self, request: Request):
        """Login POST"""
        logging.debug("Post: %s", request.data)
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)