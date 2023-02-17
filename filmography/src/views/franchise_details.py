from django.shortcuts import render

from src.models.franchise import Franchise


def franchise_details(request, key):
    franchise = Franchise.objects.get(id=key)
    return render(request, 'franchise_details.html', {
        'franchise': franchise
    })
