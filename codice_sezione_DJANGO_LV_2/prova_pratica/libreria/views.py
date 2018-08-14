from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Genere, Autore, Libro

# Create your views here.
def home(request):
    generi = Genere.objects.all()
    autori = Autore.objects.all()
    libri = Libro.objects.all()
    context = {"generi": generi, "autori": autori, "libri": libri }

    return render(request, "homepage.html", context)

class AutoreDetailViewCB(DetailView):
    model = Autore
    template_name = "profilo_autore.html"

class LibriListViewCB(ListView):
    model = Libro
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro.objects.all()
        return context
