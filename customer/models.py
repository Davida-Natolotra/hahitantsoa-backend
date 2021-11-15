from django.db import models
#Configuration des storages et path encore nécessaire

class Societe(models.Model):
    Nom = models.CharField(max_length=120)
    Representant_Nom = models.CharField(max_length=120)
    Representant_Prenoms = models.CharField(max_length=120)
    Domiciliation = models.CharField(max_length=300)
    Contact = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    NIF = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    STAT = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    RCS = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)


class Particulier(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    Lieu_naissance = models.CharField(max_length=300)
    CIN = models.BigIntegerField(null=False)
    CIN_date_delivrance = models.DateField(auto_now=False, auto_now_add=False)
    CIN_recto = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    CIN_verso = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    Certificat_residence = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    Lieu_residence = models.CharField(max_length=300)
    Contact1 = models.CharField(max_length=10)
    Contact2 = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)

class Guest(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Contact = models.CharField(max_length=10)
        
class RendezVous(models.Model):
    #Toutes les entités qui prennent des rdv seront considéré comme des guests.
    #Les opérations à effectuer sont à indiquer dessus.

    CHOIX_ETAT = [
        ('ANN', 'Annuler'),
        ('REP', 'Reporter'),
        ('ACT', 'Actif')
    ]

    MOTIF = [
        ('VIS', 'Visite'),
        ('CON', 'Signature de Contrat'),
        ('PAI', 'Paiement')
    ]
    
    Customer = models.ForeignKey('Guest', on_delete=models.CASCADE, default='None')
    Date_Darrivé = models.DateTimeField(auto_now=False, auto_now_add=False)
    Date_Depart = models.DateTimeField(auto_now=False, auto_now_add=False)
    Disponibilite = models.BooleanField(default=True)
    Motif = models.CharField(max_length=3, choices=CHOIX_ETAT, default="VIS")
    Etat = models.CharField(max_length=3, choices=CHOIX_ETAT, default="ACT")
    