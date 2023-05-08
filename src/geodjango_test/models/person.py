"""Person model"""
from django.conf import settings
from django.db import models


class Person(models.Model):
    """People"""

    _first_name = models.CharField(max_length=100, blank=True)
    _last_name = models.CharField(max_length=100, blank=True)
    _email = models.EmailField(max_length=100, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def save(self, *args, **kwargs):
        """Save current and user object."""
        if hasattr(self, "user") and self.user is not None:
            self.user.save(*args, **kwargs)
        super().save(*args, **kwargs)

    @property
    def email(self):
        """Email address."""
        if hasattr(self, "user") and self.user is not None:
            return self.user.email
        return self._email

    @email.setter
    def email(self, value):
        """Set email address."""
        if hasattr(self, "user") and self.user is not None:
            self.user.email = value
        else:
            self._email = value

    @property
    def first_name(self):
        """Email address."""
        if hasattr(self, "user") and self.user is not None:
            return self.user.first_name
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Set first name address."""
        if hasattr(self, "user") and self.user is not None:
            self.user.first_name = value
        else:
            self._first_name = value

    @property
    def last_name(self):
        """Email address."""
        if hasattr(self, "user") and self.user is not None:
            return self.user.last_name
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Set last name address."""
        if hasattr(self, "user") and self.user is not None:
            self.user.last_name = value
        else:
            self._last_name = value
