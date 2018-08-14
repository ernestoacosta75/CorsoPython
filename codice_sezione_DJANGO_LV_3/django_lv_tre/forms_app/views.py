from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContattoForm

# Create your views here.

def homepage(request):
    return render(request, "forms_app/home.html")

# def contatti(request):
#     form = ContattoForm
#     context = {"form": form}
#     return render(request, "forms_app/contatto.html", context)

def contatti(request):
    
    if request.method == "POST":
        form = ContattoForm(request.POST)
        if form.is_valid():
            print("Il Form è valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("E-MAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])

            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    else:
        form = ContattoForm()

    context = {"form": form}
    return render(request, "forms_app/contatto.html", context)
