"""Login Serializer"""
import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers

logger = logging.getLogger(__name__)


class LoginSerializer(serializers.Serializer):
    """Login Serializer"""

    email = serializers.EmailField(label="Email", write_only=True)
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user_model = get_user_model()
            try:
                user = user_model.objects.get(email=email)
            except user_model.DoesNotExist:
                msg = "Access denied: wrong email or password."
                raise serializers.ValidationError(msg, code="authorization")
            # Try to authenticate the user using Django auth framework.
            if not user or not user.check_password(password):
                msg = "Access denied: wrong email or password."
                raise serializers.ValidationError(msg, code="authorization")
            attrs["user"] = user
            return attrs
        msg = 'Both "email" and "password" are required.'
        raise serializers.ValidationError(msg, code="authorization")
