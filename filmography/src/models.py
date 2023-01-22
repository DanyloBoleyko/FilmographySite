from django.db import models

# Create your models here.


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
    rating = models.FloatField()
    producers = models.CharField(max_length=255)
    directors = models.CharField(max_length=255)
    actors = models.CharField(max_length=255)
    poster = models.ImageField(upload_to="photos/%Y-%m-%d/")
    genre = models.CharField(
        max_length=255,
        choices=Genres.choices,
        default=Genres.NONE,
    )
    age_rating = models.FloatField()
    announced_at = models.DateField(blank=True)
    published_at = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
