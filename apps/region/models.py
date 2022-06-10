from django.db import models
from apps.country.models import Country
from language.models import Language
from own_packages.abstractclass import AbstractCLass
from relation.models import PrimaryKeysOfImages
from gallery.models import Image


class Region(AbstractCLass):
    region_name = models.CharField(max_length=255)
    # region_info = models.TextField()
    region_url = models.CharField(max_length=500)
    region_meta_keywords = models.TextField()

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    region_images = models.ManyToManyField(Image, db_table="region_table")

    def __str__(self):
        return self.region_name


class ContentRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    region_name = models.CharField(max_length=255)
    region_info = models.TextField()
