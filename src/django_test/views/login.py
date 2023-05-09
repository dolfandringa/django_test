"""Login View"""
import logging

from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.serializers import empty

from .serializers import LoginSerializer

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(views.APIView):
    """Login view"""

    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    schema = None

    def post(self, request):
        """Login POST"""
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data is None or isinstance(
            serializer.validated_data, empty
        ):
            raise ValidationError("No validated data.")
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
