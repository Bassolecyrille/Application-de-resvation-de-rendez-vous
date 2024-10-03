from django.db import models

class RendezVous(models.Model):
    nom = models.CharField(max_length=100)  # Nom de la personne
    email = models.EmailField()  # Email de la personne
    date_rdv = models.DateTimeField()  # Date et heure du rendez-vous
    description = models.TextField(null=True, blank=True)  # Description du rendez-vous

    def __str__(self):
        return f"Rendez-vous de {self.nom} le {self.date_rdv}"
