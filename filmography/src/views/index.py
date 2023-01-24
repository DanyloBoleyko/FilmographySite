from django.shortcuts import render

from src.models.film import Film

routes = {
    'First': '/first',
    'Second': '/second',
    'Third': '/third',
}


def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {
        'title': 'Home',
        'films': films,
        'links': [{'name': k, 'url': v} for k, v in routes.items()]
    })
