from django.shortcuts import render, get_object_or_404
from .models import Emission, TypeEmission

def liste(request):
    emissions = Emission.objects.filter(publie=True)
    types = TypeEmission.objects.all()

    type_slug = request.GET.get('type')
    mois = request.GET.get('mois')
    q = request.GET.get('q')

    if type_slug:
        emissions = emissions.filter(type_emission__slug=type_slug)
    if mois:
        emissions = emissions.filter(date_diffusion__month=mois)
    if q:
        emissions = emissions.filter(titre__icontains=q)

    return render(request, 'emissions/liste.html', {
        'emissions': emissions,
        'types': types,
    })

def detail(request, pk):
    emission = get_object_or_404(Emission, pk=pk, publie=True)
    Emission.objects.filter(pk=pk).update(nb_ecoutes=emission.nb_ecoutes + 1)
    return render(request, 'emissions/detail.html', {'emission': emission})