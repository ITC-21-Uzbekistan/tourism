from django.db import models


class Language(models.Model):
    language_name = models.CharField(max_length=255)
    language_short = models.CharField(max_length=10)

    def __str__(self):
        return self.language_name

    class Meta:
        ordering = ['id']
