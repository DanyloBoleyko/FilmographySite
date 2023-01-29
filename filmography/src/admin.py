from django.contrib import admin

from src.models.film import Film
from src.models.franchise import Franchise
from src.models.genre import Genre
from src.models.human import Human
from src.models.porfession import Profession

admin.site.register(Film)
admin.site.register(Franchise)
admin.site.register(Genre)
admin.site.register(Human)
admin.site.register(Profession)
