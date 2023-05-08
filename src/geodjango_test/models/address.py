"""Address model"""
import re

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .person import Person


def zipcode_validator(value):
    """Validate zipcodes"""
    if not re.match(r"[0-9]{4}[A-Z]{2}", value):
        raise ValidationError(
            _("Zipcode %(value)s needs to be 4 numbers followed by 2 characters"),
            params={"value": value},
        )


class Address(models.Model):
    """Address"""

    def __str__(self):
        return f"{self.street} {self.city}"

    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="addresses"
    )
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6, validators=[zipcode_validator])
    location = models.PointField(default=Point(0, 0))
