from rest_framework.serializers import ValidationError


def email_validator(email: str):
    """Validate the email address format"""
    domain = email.split("@")[-1]
    if "yahoo" in domain:
        raise ValidationError("No yahoo domain allowed")
    if "gmail" in domain:
        raise ValidationError("No gmail domain allowed")
    if "hotmail" in domain:
        raise ValidationError("No hotmail domain allowed")
    return
