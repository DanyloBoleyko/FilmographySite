from django.shortcuts import render

from src.models.film import Film


def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
        'films': films,
    })
