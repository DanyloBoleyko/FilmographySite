from django.shortcuts import render

from src.models.film import Film


def film_details(request, key):
    film = Film.objects.get(id=key)
    return render(request, 'film_details.html', {
        'film': film,
    })
