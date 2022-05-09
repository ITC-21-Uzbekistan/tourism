from django.db import models

from relation.models import PrimaryKeysOfImages
from shrine.models import Shrine


class TypeTour(models.Model):
    name = models.CharField(max_length=255)


class Tour(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    price = models.FloatField(null=True)
    type = models.ForeignKey(TypeTour, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)

    shrines = models.ManyToManyField(Shrine)

    images = models.ManyToManyField(PrimaryKeysOfImages)

    def __str__(self):
        return self.name
