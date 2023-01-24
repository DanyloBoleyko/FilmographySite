from django.contrib import admin

from src.models.film import Film
from src.models.actor import Actor
from src.models.director import Director
from src.models.producer import Producer
from src.models.related_films import RelatedFilms

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Producer)
admin.site.register(RelatedFilms)
