from django.shortcuts import render
from django.http import HttpResponse
from store.models import *

# Create your views here.
# def index(request):
#     return HttpResponse("Store Page")

def inventaire(request):
    query_set = Materiel.objects.all()

    for materiel in query_set:
        print(materiel)
 
    return render(request, 'store.html')