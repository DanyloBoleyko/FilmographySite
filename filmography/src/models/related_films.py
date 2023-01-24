from django.db import models


class RelatedFilms(models.Model):
    chronology = models.ManyToManyField('Film')
    description = models.CharField(max_length=1024)
    plot = models.CharField(max_length=8184)
    rating = models.FloatField(default=0)

