from rest_framework.serializers import ValidationError
import re


def secure_password(password):
    """Make sure the password is secure."""
    if not re.match(r".*[0-9]+.*", password):
        raise ValidationError(
            "Please make sure there is at least 1 number in the password"
        )
