from django.db import models

from own_packages.abstractclass import AbstractCLass
from relation.models import PrimaryKeysOfImages
from apps.language.models import Language
from apps.gallery.models import Image


class Country(AbstractCLass):
    country_name = models.CharField(max_length=255)
    # country_info = models.TextField()
    country_url = models.CharField(max_length=255, null=True, blank=True)
    country_meta_keywords = models.TextField()

    country_images = models.ManyToManyField(Image, db_table="country_images")

    def __str__(self):
        return self.country_name


class ContentCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    country_name = models.CharField(max_length=255)
    country_info = models.TextField()

    class Meta:

        ordering = ['id']

