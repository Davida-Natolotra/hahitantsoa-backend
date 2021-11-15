from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField
from customer.models import Guest


class Offre_Hahitantsoa(models.Model): #Création offre
    package_Hahitantsoa = models.ForeignKey('Package_Hahitantsoa', on_delete=models.PROTECT)
    type_Fete_Hahitantsoa = models.ForeignKey('Type_Fete_Hahitantsoa', on_delete=models.PROTECT)
    choix_Sol_Hahitantsoa = models.ForeignKey('Choix_Sol_Hahitantsoa', on_delete=models.PROTECT)
    draperie_Hahitantsoa = models.ForeignKey('Draperie_Hahitantsoa', on_delete=models.PROTECT)
    decoration_Hahitantsoa = models.ForeignKey('Decoration_Hahitantsoa', on_delete=models.PROTECT)
    lumieres_Hahitantsoa = models.ForeignKey('Lumieres_Hahitantsoa', on_delete=models.PROTECT)
    effet_Sepciaux_Hahitantsoa = models.ForeignKey('Effet_Sepciaux_Hahitantsoa', on_delete=models.PROTECT)

class Paiement_Hahitantsoa(models.Model):
    commande = models.ForeignKey('Commande_Hahitantsoa', on_delete=models.PROTECT)
    client = models.ForeignKey(Guest, on_delete=models.PROTECT) #Trouver une solution pour integrer les models particulier et societe, permettre un choix
    total_Payer = models.IntegerField()
    paiement_Effectuer = models.IntegerField()
    reste_Payer = models.ImageField()
    date = models.DateField(auto_now=True)

class Commande_Hahitantsoa(models.Model): #Création commande
    client = models.ForeignKey(Guest, on_delete=models.PROTECT)
    date_Event_Debut = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_Event_Fin = models.DateTimeField(auto_now=False, auto_now_add=False)
    paiement = models.ForeignKey('Paiement_Hahitantsoa', on_delete=models.PROTECT)
    husband_Nom = models.CharField(max_length=120)
    husband_Prenom = models.CharField(max_length=120)
    wife_Nom = models.CharField(max_length=120)
    wife_Prenom = models.CharField(max_length=120)
    offre_Hahitantsoa = models.CharField(max_length=120) #Numero Proformat link offre hahitantsoa
    pax = models.IntegerField()#Nombre de personne
    package = models.ForeignKey('Package_Hahitantsoa', on_delete=models.PROTECT)
    droit_Logistique = models.CharField(max_length=100)
    type_Fete = models.ForeignKey('Type_Fete_Hahitantsoa', on_delete=models.PROTECT)
    choix_Sol = models.ForeignKey('Choix_Sol_Hahitantsoa', on_delete=models.PROTECT)
    draperie = models.ForeignKey('Draperie_Hahitantsoa', on_delete=models.PROTECT)
    decoration = models.ForeignKey('Decoration_Hahitantsoa', on_delete=models.PROTECT)
    lumiere = models.IntegerField() #Longueur de guirlande à utiliser
    piste_Lumineuse = models.BooleanField()
    ciel_Etoile = models.BooleanField()
    effet_Speciaux = models.ForeignKey('Effet_Sepciaux_Hahitantsoa', on_delete=models.PROTECT)


    ########## >>>>>>>>>> Besoin d'un extra pour les surplus de commande, dans package <<<<<<<<<<<########


class Package_Hahitantsoa(models.Model):
    salle = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    set_Couverts = models.CharField(max_length=100)
    set_Assiettes = models.CharField(max_length=100)
    set_Verres = models.CharField(max_length=100)
    supplement = models.CharField(max_length=100)

class Choix_Sol_Hahitantsoa(models.Model):
    CHOIX_SOL = [
        ('GAZ', 'Gazon Synthétique'),
        ('CAR', 'Carrelage'),
        ('PAR', 'Parquet en bois')
    ]
    sol = models.CharField(max_length=3, choices=CHOIX_SOL, default="CAR")

class Draperie_Hahitantsoa(models.Model):
    CHOIX_DRAPERIE = [
        ('SANS', 'Sans voilages'),
        ('CENT', 'Voilage Centré'),
        ('DEUX', 'Voilages deux pentes')
    ]
    draperie = models.CharField(max_length=4, choices=CHOIX_DRAPERIE, default="SANS")

class Decoration_Hahitantsoa(models.Model):
    CHOIX_DECO = [
        ('STD', 'Offre standard'),
        ('PER', 'Offre personalisée'),
        ('PRE', 'Autre prestataire')
    ]
    decoration = models.CharField(max_length=3, choices=CHOIX_DECO, default="STD")

class Effet_Sepciaux_Hahitantsoa(models.Model):
    CHOIX_EFFET = [
        ('STD', 'Offre standard'),
        ('PER', 'Offre personalisée'),
        ('PRE', 'Autre prestataire') #Existence d'une droit d'effet spéciaux
    ]
    effet_Speciaux = models.CharField(max_length=3, choices=CHOIX_EFFET, default="STD")

    CHOIX_DISPOSITION = [
        ('SUS', 'Suspendu'),
        ('PIE', 'Sur pieds'),
    ]
    disposition = models.CharField(max_length=3, choices=CHOIX_DISPOSITION, default="SUS") #N'est pas valide si autre prestataire, à configurer

class Lumieres_Hahitantsoa(models.Model):
    CHOIX_LUMIERE = [
        ('ETOI', 'Ciel Etoile'),
        ('SANS', 'Sans ciel etoile'),
        ('PERS', 'Personalise') #Apparition d'une case pour entrer la longueur des guirlandes à utiliser.
    ]
    lumiere = models.CharField(max_length=4, choices=CHOIX_LUMIERE, default="SANS")

class Type_Fete_Hahitantsoa(models.Model):
    CHOIX_FETE = [
        ('JOU', 'Fete de jour'),
        ('NUI', 'Fete de nuit'),
    ]
    disposition = models.CharField(max_length=3, choices=CHOIX_FETE, default="JOU")

class Bon_Livraison_Hahitantsoa(models.Model): #Si payement effectué à 100% sortie d'un BL
    commande = models.ForeignKey('Commande_Hahitantsoa', on_delete=models.PROTECT)
    numero_BL = models.CharField(max_length=100)# En fonction de la date de sortie. Après paiement total.
    date_BL = models.DateField(auto_now=False, auto_now_add=False)