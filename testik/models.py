from django.db import models


class Ima(models.Model):
    image = models.ImageField(upload_to='images/')
