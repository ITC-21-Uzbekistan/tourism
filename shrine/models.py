from django.db import models
from apps.country.models import Country
from language.models import Language
from own_packages.abstractclass import AbstractCLass
from apps.region.models import Region
from relation.models import PrimaryKeysOfImages
from gallery.models import Image


class Shrine(AbstractCLass):
    shrine_name = models.CharField(max_length=255)
    # shrine_info = models.TextField()
    shrine_url = models.CharField(max_length=1000)
    shrine_location_longitude = models.FloatField()
    shrine_location_latitude = models.FloatField()
    shrine_meta_keywords = models.TextField()

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    shrine_images = models.ManyToManyField(Image, db_table="shrine_images")

    def __str__(self):
        return self.shrine_name


class ContentShrine(models.Model):
    shrine = models.ForeignKey(Shrine, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    shrine_name = models.CharField(max_length=255)
    shrine_info = models.TextField()
