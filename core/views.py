from django.shortcuts import render
from django.conf import settings
from emissions.models import Emission
from actualites.models import Actualite
from animateurs.models import Animateur

def accueil(request):
    emissions_recentes = Emission.objects.filter(publie=True)[:4]
    actualites = Actualite.objects.filter(publie=True)[:3]
    animateurs = Animateur.objects.filter(actif=True)
    context = {
        'stream_url': settings.RADIO_STREAM_URL,
        'emissions_recentes': emissions_recentes,
        'actualites': actualites,
        'animateurs': animateurs,
    }
    return render(request, 'core/accueil.html', context)