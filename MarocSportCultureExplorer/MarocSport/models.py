from django.db import models
from datetime import datetime 
# Modèle Utilisateur
class Utilisateur(models.Model):
    nom = models.CharField(max_length=255, default='')
    prénom = models.CharField(max_length=255, default='')
    email_adress = models.EmailField(max_length=255, default='')
    mot_de_passe = models.CharField(max_length=255, default='')
# Modèle Prestation
class Prestation(models.Model):
    libelle = models.CharField(max_length=255)
    caractere_long_variable = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=4, decimal_places=2)
# Modèle Réservation
class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_de_reservation = models.DateTimeField(default=datetime.now)
    statut_de_la_reservation = models.CharField(max_length=255)
# Modèle Destination
class Destination(models.Model):
    nom_de_la_destination = models.CharField(max_length=255)
    description = models.CharField(max_length=100)
    activites_disponibles = models.CharField(max_length=255)
    informations_geographiques = models.CharField(max_length=1024)
# Modèle Evenement
class Evenement(models.Model):
    nom_de_l_evenement = models.CharField(max_length=255)
    lieu = models.CharField(max_length=1024)
    date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=100)
    categorie_sportive = models.CharField(max_length=255)
    prix_d_inscription = models.DecimalField(max_digits=4, decimal_places=2)


