from django.db import models

from src.fields.large_text_field import LargeTextField
from src.utils.url_friendly import url_friendly


class Franchise(models.Model):
    name = models.CharField(max_length=255)
    chronology = models.ManyToManyField('Film')
    description = LargeTextField(max_length=4096, blank=True)
    plot = LargeTextField(max_length=16368, blank=True)
    rating = models.FloatField(default=0, null=True)

    def __str__(self):
        return f"{self.name}"

    def key(self):
        return url_friendly(self.name)

    def description_as_list(self):
        return [s for s in self.description.split('\n') if s.rstrip()]

    def plot_as_list(self):
        return [s for s in self.plot.split('\n') if s.rstrip()]

