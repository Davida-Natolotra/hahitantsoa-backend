from django.db import models

class Personnel(models.Model):
    Nom = models.CharField(max_length=120)
    Prenoms = models.CharField(max_length=120)
    Date_naissance = models.DateField(auto_now=False, auto_now_add=False)
    Lieu_naissance = models.CharField(max_length=300)
    CIN = models.BigIntegerField()
    CIN_date_delivrance = models.DateField(auto_now=False, auto_now_add=False)
    CIN_recto = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    CIN_verso = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    Certificat_residence = models.ImageField(upload_to=None) #Configuration à faire (storage, path...)
    Lieu_residence = models.CharField(max_length=300)
    Contact1 = models.CharField(max_length=10)
    Contact2 = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)

class Salaire(models.Model):
    salaire = models.IntegerField()
    avance = models.IntegerField()


class Congee(models.Model):
    jour_congé = models.IntegerField()
    date_congé = models.DateField(auto_now=False)

class Historique(models.Model):
    date_recrutement = models.DateTimeField(auto_now=False)
    date_demission = models.DateField(auto_now=False)

