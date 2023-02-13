from django.shortcuts import render

from src.models.film import Film
from src.models.human import Human
from src.models.porfession import Professions


def person_details(request, key):
    human = Human.objects.get(id=key)
    films = {
        f'films_{prof}': Film.objects.filter(**{f'{prof}s__in': [human]})
        for prof in Professions.values
    }
    actor_in = Film.objects.filter(actors__in=[human])
    voice_actor_in = Film.objects.filter(voice_actors__in=[human])
    producer_of = Film.objects.filter(producers__in=[human])
    screenwriter_of = Film.objects.filter(screenwriters__in=[human])
    director_of = Film.objects.filter(directors__in=[human])
    return render(request, 'person_details.html', {
        'human': human,
        # 'films_actor': actor_in,
        # 'films_voice_actor': voice_actor_in,
        # 'films_producer': producer_of,
        # 'films_screenwriter': screenwriter_of,
        # 'films_director': director_of,
        **films
    })
