from django.shortcuts import render, redirect
from .models import Don

def faire_don(request):
    if request.method == 'POST':
        don = Don.objects.create(
            nom_donateur=request.POST.get('nom', 'Anonyme'),
            email=request.POST.get('email', ''),
            telephone=request.POST.get('telephone', ''),
            montant=request.POST.get('montant'),
            methode=request.POST.get('methode'),
            message=request.POST.get('message', ''),
        )
        return redirect('dons:confirmation', pk=don.pk)
    return render(request, 'dons/faire_don.html')

def confirmation(request, pk):
    don = Don.objects.get(pk=pk)
    return render(request, 'dons/confirmation.html', {'don': don})