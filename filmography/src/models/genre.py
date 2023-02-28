from django.db import models


class Genres(models.TextChoices):
    ACTION = 'action'
    ADVENTURE = 'adventure'
    COMEDY = 'comedy'
    DRAMA = 'drama'
    FANTASY = 'fantasy'
    HORROR = 'horror'
    MUSICALS = 'musicals'
    MYSTERY = 'mystery'
    ROMANCE = 'romance'
    SCIENCE_FICTION = 'science_fiction'
    SPORTS = 'sports'
    THRILLER = 'thriller'
    WESTERN = 'western'


class Genre(models.Model):
    genre = models.CharField(
        max_length=255,
        choices=Genres.choices,
        unique=True
    )

    def __str__(self):
        return f"{self.genre.capitalize().replace('_', ' ')}"
