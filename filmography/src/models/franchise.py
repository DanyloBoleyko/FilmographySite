from django.db import models

from src.fields.large_text_field import LargeTextField


class Franchise(models.Model):
    chronology = models.ManyToManyField('Film')
    description = LargeTextField(max_length=1024, blank=True)
    plot = LargeTextField(max_length=8184, blank=True)
    rating = models.FloatField(default=0, null=True)

