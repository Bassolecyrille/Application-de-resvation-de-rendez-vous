from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = ['nom', 'date_rdv', 'email']
        fields = ['nom', 'email', 'date_rdv', 'description']
