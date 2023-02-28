from django.shortcuts import render

from src.models.film import Film
from src.models.franchise import Franchise


def film_details(request, key):
    assert key is not None, 'Key is null'
    film = Film.objects.get(id=key)
    franchise = Franchise.objects.filter(chronology__in=[film]).first()
    return render(request, 'film_details.html', {
        'film': film,
        'franchise': franchise
    })
