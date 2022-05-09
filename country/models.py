from django.db import models
from relation.models import PrimaryKeysOfImages


class Country(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    url = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)

    images = models.ManyToManyField(PrimaryKeysOfImages)

    def __str__(self):
        return self.name
