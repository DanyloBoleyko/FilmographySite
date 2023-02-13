from django.db.models import Q
from django.shortcuts import render

from src.models.film import Film
from src.models.human import Human
from src.models.porfession import Professions


def search(request, text=''):
    films = Film.objects.filter(name__contains=text)
    humans = {
        f'{prof}s': Human.objects.filter(
            Q(first_name__contains=text) | Q(last_name__contains=text),
            profession__profession=prof
        )
        for prof in Professions.values
    }
    return render(request, 'search.html', {
        'films': films,
        **humans
    })
