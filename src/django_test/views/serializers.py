"""Login Serializer"""
import logging

from django.contrib.auth import get_user_model
from rest_framework_json_api import serializers

from geodjango_test.validators.email_validator import email_validator
from geodjango_test.validators.password_validator import secure_password

logger = logging.getLogger(__name__)


class LoginSerializer(serializers.Serializer):
    """Login Serializer"""

    class Meta:
        resource_name = "login"

    email = serializers.EmailField(
        label="Email", write_only=True, validators=[email_validator]
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
        validators=[secure_password],
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get("email")
        password = attrs.get("password")
        User = get_user_model()

        if email and password:
            users = User.objects.filter(email__iexact=email).all()
            if len(users) > 0:
                raise serializers.ValidationError("User already exists")
            user = User(email=email, password=password, username=email)
            user.save()
            attrs["user"] = user
            return attrs
        msg = 'Both "email" and "password" are required.'
        raise serializers.ValidationError(msg, code="authorization")
