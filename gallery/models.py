from django.db import models
# from country.models import Country
# from region.models import Region
# from shrine.models import Shrine
# from tour.models import Tour
from language.models import Language
from own_packages.abstractclass import AbstractCLass


class TypeImage(models.Model):
    type_image = models.CharField(max_length=255)

    def __str__(self):
        return self.type_image


class ContentTypeImage(models.Model):
    type_image = models.ForeignKey(TypeImage, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    type_name = models.CharField(max_length=255)


class Image(AbstractCLass):
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    # region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    # shrine = models.ForeignKey(Shrine, on_delete=models.SET_NULL, null=True)
    # tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    type_image = models.ForeignKey(TypeImage, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')
    # alt_text = models.CharField(max_length=500)
    # description = models.TextField()

    def __str__(self):
        return self.name


class ContentImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    image_name = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=500)
    description = models.TextField()
