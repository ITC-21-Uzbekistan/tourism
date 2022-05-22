from django.db import models
from country.models import Country
from language.models import Language
from relation.models import PrimaryKeysOfImages


class Region(models.Model):
    region_name = models.CharField(max_length=255)
    region_info = models.TextField()
    region_url = models.CharField(max_length=500)
    region_meta_keywords = models.TextField()

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    region_images = models.ManyToManyField(PrimaryKeysOfImages)

    def __str__(self):
        return self.name


class ContentRegion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    region_name = models.CharField(max_length=255)
    region_info = models.TextField()
