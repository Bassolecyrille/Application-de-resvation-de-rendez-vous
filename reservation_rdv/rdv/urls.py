from django.urls import path
from .views import ajouter_rdv, liste_rdv

urlpatterns = [
    path('ajouter/', ajouter_rdv, name='ajouter_rdv'),
    path('', liste_rdv, name='liste_rdv'),
]

