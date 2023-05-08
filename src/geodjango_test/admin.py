"""Admin model."""
from django.contrib.gis import admin

from geodjango_test.models import Address, Person, WorldBorder


@admin.register(Address)
class AddressAdmin(admin.OSMGeoAdmin):
    """Address admin with OSM background."""

    pass


admin.site.register(WorldBorder)
admin.site.register(Person)

# Register your models here.
