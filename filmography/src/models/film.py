from django.db import models

from src.fields.large_text_field import LargeTextField


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = LargeTextField(blank=True, max_length=1024)
    plot = LargeTextField(blank=True, max_length=8184)
    rating = models.FloatField(default=0)
    producers = models.ManyToManyField('Human', related_name='producer', blank=True)
    directors = models.ManyToManyField('Human', related_name='director', blank=True)
    actors = models.ManyToManyField('Human', related_name='actor', blank=True)
    voice_actors = models.ManyToManyField('Human', related_name='voice_actor', blank=True)
    screenwriters = models.ManyToManyField('Human', related_name='screenwriter', blank=True)
    poster = models.ImageField(blank=True, upload_to="photos/films/%Y-%m-%d/")
    genres = models.ManyToManyField('Genre', blank=True)
    age_rating = models.FloatField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    announce_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def description_as_list(self):
        return [s for s in self.description.split('\n') if s.rstrip()]

    def plot_as_list(self):
        return [s for s in self.plot.split('\n') if s.rstrip()]

    def starring_list(self):
        return self.voice_actors.all() | self.actors.all()
