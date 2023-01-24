from django.db import models


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


class Genre(models.Model):
    genre = models.CharField(
        max_length=255,
        choices=Genres.choices,
        default=Genres.NONE,
    )
