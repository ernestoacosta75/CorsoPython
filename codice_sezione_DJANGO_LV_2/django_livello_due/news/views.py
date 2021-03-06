from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Articolo, Giornalista

# Create your views here.
# # def home(request):
#     return HttpResponse("<h1>Homepage!</h1>")

# def home(request):
#     lista_articoli = ""
#     lista_giornalisti = ""
#
#     for articolo in Articolo.objects.all():
#         lista_articoli += (articolo.titolo + "<br>")
#
#     for giornalista in Giornalista.objects.all():
#         lista_giornalisti += (giornalista.nome + "<br>")
#
#     response = "Articoli:<br>" + lista_articoli + "<br>Giornalisti:<br>" + lista_giornalisti
#
#     return HttpResponse("<h1>" + response + "</h1>")

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"giornalisti": giornalisti, "articoli": articoli }

    return render(request, "homepage.html", context)

# def articoloDetailView(request, pk):
#     # articolo = Articolo.objects.get(pk=pk)
#     articolo = get_object_or_404(Articolo, pk=pk)
#     context = {"articolo": articolo }
#
#     return render(request, "articolo_detail.html", context)

### GCBV Generic Class Based Views
# Documentazione ufficiale: https://docs.djangoproject.com/en/2.1/ref/class-based-views/

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = "articolo_detail.html"

class ArticoloListViewCB(ListView):
    model = Articolo
    template_name = "lista_articoli.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articoli"] = Articolo.objects.all()
        return context
