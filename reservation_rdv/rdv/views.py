from django.shortcuts import render, redirect
from .models import RendezVous
from .forms import RendezVousForm
from django.utils import timezone


# Vue pour lister les rendez-vous

def liste_rdv(request):
    rdvs = RendezVous.objects.all().order_by('date_rdv')
    return render(request, 'rdv/liste_rdv.html', {'rdvs': rdvs})





# Vue pour ajouter un rendez-vous


def ajouter_rdv(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        description = request.POST.get('description')
        date_rdv = request.POST.get('date_rdv')

        # Vérifie si tous les champs nécessaires sont remplis
        if not nom or not email or not date_rdv:
            return render(request, 'ajouter_rdv.html', {'error': "Tous les champs sont obligatoires."})

        # Créer et sauvegarder un nouvel objet RendezVous
        nouveau_rdv = RendezVous(nom=nom, email=email, description=description, date_rdv=date_rdv)
        nouveau_rdv.save()

        # Rediriger vers la liste des rendez-vous après l'ajout
        return redirect('liste_rdv')

    return render(request, 'ajouter_rdv.html')

