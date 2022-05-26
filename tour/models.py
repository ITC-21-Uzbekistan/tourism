from django.db import models

from language.models import Language
from relation.models import PrimaryKeysOfImages
from shrine.models import Shrine
from gallery.models import Image


class TypeTour(models.Model):
    type_name = models.CharField(max_length=255)


class ContentTypeTour(models.Model):
    type_tour = models.ForeignKey(TypeTour, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    type_name = models.CharField(max_length=255)


class Tour(models.Model):
    tour_name = models.CharField(max_length=255)
    # tour_info = models.TextField()
    tour_price = models.FloatField(null=True)
    tour_type = models.ForeignKey(TypeTour, on_delete=models.SET_NULL, null=True)
    tour_url = models.CharField(max_length=1000)

    tour_shrines = models.ManyToManyField(Shrine)

    tour_images = models.ManyToManyField(Image, db_table="tour_images")

    def __str__(self):
        return self.tour_name


class ContentTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    tour_name = models.CharField(max_length=255)
    tour_info = models.TextField()
