from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class ContattoForm(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}),
                                validators=[validators.MinLengthValidator(10)])

    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
