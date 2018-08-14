from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Genere(models.Model):
    """ Modello generico di un genere """
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Autore(models.Model):
    """ Modello generico di un autore """
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse("profilo_autore", kwargs={"pk": self.pk})        

    class Meta():
        verbose_name = "Autore"
        verbose_name_plural = "Autori"


class Libro(models.Model):
    """ Modello generico di un libro """

    titolo = models.CharField(max_length=40)
    genere = models.CharField(max_length=20)
    isbn = models.CharField(max_length=16)
    autore =  models.ForeignKey(Autore, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.titolo

    class Meta():
        verbose_name = "Libro"
        verbose_name_plural = "libri"
