from django.db import models

from src.fields.large_text_field import LargeTextField


class Human(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pseudonym = models.CharField(max_length=255, blank=True)
    biography = LargeTextField(max_length=8184, blank=True)
    profession = models.ManyToManyField('Profession', blank=True)
    rating = models.FloatField(default=0, null=True)
    birth_day = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="photos/people/%Y-%m-%d/")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def biography_as_list(self):
        return [s for s in self.biography.split('\n') if s.rstrip()]
