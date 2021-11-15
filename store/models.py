from django.db import models

# Create your models here.
class Materiel(models.Model):
    Designation = models.CharField(max_length=150)
    Emplacement = models.ForeignKey('Depot', on_delete=models.PROTECT)
    Code = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    Quantite = models.IntegerField()
    QuantiteEnService = models.IntegerField()
    QuantiteDisponible = models.IntegerField()
    PrixDAchat = models.BigIntegerField()
    PrixDeLocation = models.BigIntegerField()
    PrixDeCasse = models.BinaryField()
    Consigne = models.CharField(max_length=255)

class Depot(models.Model):
    Lieux = models.CharField(max_length=100) #Classe


# >>>> Utilisateur à créer. Besoin de configuration.
class Entre_Sortie(models.Model):
    Date_Sortie = models.DateTimeField(auto_now=False, auto_now_add=False)
    Date_Entree = models.DateTimeField(auto_now=False, auto_now_add=False)
    Magasinier = models.CharField(max_length=100) #Employer à encore congigurer avec employé. Besoin de FK

# class Casse(models.Model):
#     pass