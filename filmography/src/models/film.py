from django import forms
from django.db import models

from src.models.actor import Actor


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=1024)
    plot = models.TextField(blank=True, max_length=8184)
    rating = models.FloatField(default=0)
    producers = models.ManyToManyField('Producer', blank=True)
    directors = models.ManyToManyField('Director', blank=True)
    actors = models.ManyToManyField('Actor', blank=True)
    poster = models.ImageField(blank=True, upload_to="photos/films/%Y-%m-%d/")
    genres = models.ManyToManyField('Genre', blank=True)
    age_rating = models.FloatField(blank=True, null=True)
    announced_at = models.DateField(blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
