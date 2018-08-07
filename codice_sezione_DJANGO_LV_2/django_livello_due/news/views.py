from django.shortcuts import render
from django.http import HttpResponse

from .models import Articolo, Giornalista

# Create your views here.
# # def home(request):
#     return HttpResponse("<h1>Homepage!</h1>")

def home(request):
    lista_articoli = ""
    lista_giornalisti = ""

    for articolo in Articolo.objects.all():
        lista_articoli += (articolo.titolo + "<br>")

    for giornalista in Giornalista.objects.all():
        lista_giornalisti += (giornalista.nome + "<br>")

    response = "Articoli:<br>" + lista_articoli + "<br>Giornalisti:<br>" + lista_giornalisti

    return HttpResponse("<h1>" + response + "</h1>")
