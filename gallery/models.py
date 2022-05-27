from unittest import mock
from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=80, unique= True)

    class Meta:
        ordering = ["location"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


