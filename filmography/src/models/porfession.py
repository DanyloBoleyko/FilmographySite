from django.db import models


class Professions(models.TextChoices):
    ACTOR = 'actor'
    VOICE_ACTOR = 'voice_actor'
    DIRECTOR = 'director'
    PRODUCER = 'producer'
    SCREENWRITER = 'screenwriter'
    STORY_WRITER = 'story_writer'
    MUSICIAN = 'musician'


class Profession(models.Model):
    profession = models.CharField(
        max_length=255,
        choices=Professions.choices
    )

    def __str__(self):
        return f"{self.profession}"
