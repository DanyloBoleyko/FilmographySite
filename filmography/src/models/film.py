from django.db import models

from src.models.actor import Actor


class Genres(models.TextChoices):
    NONE = 'Undefined'
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    COMEDY = 'Comedy'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    HORROR = 'Horror'
    MUSICALS = 'Musicals'
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    SCIENCE_FICTION = 'Science fiction'
    SPORTS = 'Sports'
    THRILLER = 'Thriller'
    WESTERN = 'Western'


class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=1024)
    plot = models.CharField(blank=True, max_length=4092)
    rating = models.FloatField(default=0)
    producers = models.CharField(max_length=255)
    directors = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)
    poster = models.ImageField(upload_to="photos/films/%Y-%m-%d/")
    genre = models.CharField(
        max_length=255,
        choices=Genres.choices,
        default=Genres.NONE,
    )
    age_rating = models.FloatField(blank=True)
    announced_at = models.DateField(blank=True)
    published_at = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
