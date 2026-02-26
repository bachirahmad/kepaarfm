from django.shortcuts import render
from .models import Animateur

def liste(request):
    animateurs = Animateur.objects.filter(actif=True)
    return render(request, 'animateurs/liste.html', {
        'animateurs': animateurs,
    })