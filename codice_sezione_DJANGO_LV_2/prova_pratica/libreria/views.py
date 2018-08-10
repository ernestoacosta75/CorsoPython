from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Genere, Autore, Libro

# Create your views here.
def home(request):
    generi = Genere.objects.all()
    autori = Autore.objects.all()
    libri = Libro.objects.all()
    context = {"generi": generi, "autori": autori, "libri": libri }

    return render(request, "homepage.html", context)
