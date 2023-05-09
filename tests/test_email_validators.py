"""Test the email validator"""
import pytest
from rest_framework.serializers import ValidationError

from geodjango_test.validators.email_validator import email_validator


def test_email_invalid_domain():
    """Test the domain is valid (no yahoo, gmail, hotmail"""
    with pytest.raises(ValidationError):
        email_validator("dolf@gmail.com")
    with pytest.raises(ValidationError):
        email_validator("dolf@hotmail.com")
    with pytest.raises(ValidationError):
        email_validator("dolf@yahoo.com")


def test_email_valid():
    """Test that the email"""
    assert email_validator("dolf@scene.community") is None
