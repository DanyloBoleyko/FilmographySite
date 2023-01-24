from django.db import models

from src.models.film import Film


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    films = models.ManyToManyField(Film)
    rating = models.FloatField(default=0)
    birth_day = models.DateField(blank=True)
    image = models.ImageField(blank=True, upload_to="photos/people/%Y-%m-%d/")

