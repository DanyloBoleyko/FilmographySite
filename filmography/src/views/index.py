from django.shortcuts import render

routes = {
    'First': '/first',
    'Second': '/second',
    'Third': '/third',
}


def index(request):
    return render(request, 'index.html', {
        'title': 'Home',
        'links': [{'name': k, 'url': v} for k, v in routes.items()]
    })
