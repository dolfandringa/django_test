"""Test the password validator"""
import pytest
from rest_framework.serializers import ValidationError

from geodjango_test.validators.password_validator import secure_password


def test_insecure_password():
    """Test the password is insecure"""
    with pytest.raises(ValidationError):
        secure_password("blablabla")


def test_secure_password():
    """Test a secure password"""
    assert secure_password("bla1bla") is None
