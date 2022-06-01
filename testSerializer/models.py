from django.db import models


class Lang(models.Model):
    name = models.CharField(max_length=255)
    short = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Content(models.Model):
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=255)
    country_info = models.TextField()

    def __str__(self):
        return self.country.name
