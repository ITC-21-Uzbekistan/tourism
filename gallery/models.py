from django.db import models
from country.models import Country
from region.models import Region
from shrine.models import Shrine
from tour.models import Tour


class TypeImage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Image(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    shrine = models.ForeignKey(Shrine, on_delete=models.CASCADE, null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(TypeImage, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=255)
    image = models.TextField()
    altText = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name
