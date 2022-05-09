from django.db import models
from country.models import Country
from region.models import Region
from relation.models import PrimaryKeysOfImages


class Shrine(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    url = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    images = models.ManyToManyField(PrimaryKeysOfImages)

    def __str__(self):
        return self.name
