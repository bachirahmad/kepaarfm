from django.shortcuts import render
from .models import Programme
from datetime import datetime

def liste(request):
    JOURS = [
        ('lundi', 'Lundi'), ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'), ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'), ('samedi', 'Samedi'),
        ('dimanche', 'Dimanche'),
    ]

    # Jour actuel en français
    jours_map = {
        0: 'lundi', 1: 'mardi', 2: 'mercredi', 3: 'jeudi',
        4: 'vendredi', 5: 'samedi', 6: 'dimanche'
    }
    jour_aujourd_hui = jours_map[datetime.now().weekday()]
    jour_actif = request.GET.get('jour', jour_aujourd_hui)

    programmes = Programme.objects.filter(jour=jour_actif, actif=True)

    # Marquer le programme en cours
    now = datetime.now().time()
    for prog in programmes:
        prog.is_current = prog.heure_debut <= now <= prog.heure_fin

    return render(request, 'programmes/liste.html', {
        'programmes': programmes,
        'jours': JOURS,
        'jour_actif': jour_actif,
    })