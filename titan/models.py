from store.models import Materiel
from django.db import models
from customer.models import Guest
from store.models import Materiel

# Create your models here.
class Commande_Titan(models.Model):
    client = models.ForeignKey(Guest, on_delete=models.PROTECT)
    date_Reservation = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_Sortie_Matériel = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_Retour_Materiel = models.DateTimeField(auto_now=False, auto_now_add=False)
    materiel = models.ForeignKey(Materiel, on_delete=models.PROTECT)


class Bon_Livraison_Titan(models.Model):
    commande = models.CharField(max_length=100) #FK vers Commande_Titan
    numero_BL = models.CharField(max_length=100)# En fonction de la date de sortie. Après paiement total.
    date_BL = models.DateField(auto_now=False, auto_now_add=False)

