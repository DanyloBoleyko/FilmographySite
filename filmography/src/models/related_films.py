from django.db import models

from src.models.film import Film


class RelatedFilms(models.Model):
    chronology = models.ManyToManyField(Film)
    description = models.CharField(max_length=1024)
    plot = models.CharField(max_length=4092)
    rating = models.FloatField(default=0)

