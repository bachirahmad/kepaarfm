from django.shortcuts import render
from .models import Actualite

def liste(request):
    actualites = Actualite.objects.filter(publie=True)
    return render(request, 'actualites/liste.html', {
        'actualites': actualites,
    })