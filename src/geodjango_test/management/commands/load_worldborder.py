"""Load world borders data."""

from pathlib import Path

from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand

from geodjango_test.models import WorldBorder


class Command(BaseCommand):
    """Load the world borders."""

    help = "Loads the world borders in the database"

    def handle(self, *args, **options):
        world_mapping = {
            "fips": "FIPS",
            "iso2": "ISO2",
            "iso3": "ISO3",
            "un": "UN",
            "name": "NAME",
            "area": "AREA",
            "pop2005": "POP2005",
            "region": "REGION",
            "subregion": "SUBREGION",
            "lon": "LON",
            "lat": "LAT",
            "mpoly": "MULTIPOLYGON",
        }

        world_shp = (
            Path(__file__).resolve().parent.parent.parent
            / "data"
            / "TM_WORLD_BORDERS-0.3.shp"
        )
        layermapping = LayerMapping(
            WorldBorder, world_shp, world_mapping, transform=False
        )
        layermapping.save(strict=True)
        self.stdout.write("Successfully loaded data")
