from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_a(request):
    return HttpResponse("<h1>Benvenuti alla prima view della prova pratica!</h1>")

def view_b(request):
    return HttpResponse("<h1>Benvenuti alla seconda view della prova pratica!</h1>")

def view_c(request):
    return HttpResponse("<h1>Benvenuti alla terza view della prova pratica!</h1>")
