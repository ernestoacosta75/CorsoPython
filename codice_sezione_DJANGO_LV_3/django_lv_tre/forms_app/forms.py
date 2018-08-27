from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

''' - La validazione avviente tutta LATO SERVER. Per disabilitarla, si aggiunge l'attributo novalidate al tag formù
      nella pagina html.
    - Per fare che un campo del form non sia obbligatorio, nella classe che eredita da forms.Form basta aggiungere
      required=false per il capo desiderato:
      Ex.: nome = forms.CharField(required=false)

    - Il modo più comune per validare un campo del form e sovrascrivere il metodo clean_<nome_campo> (Vedere
      clean_contenuto nella classe di sotto).
    - Il metodo cleaned_data permette di leggere il valore di un campo del form.
      Ex.: dati = self.cleaned_data["contenuto"]

    - Per lanciare un errore di validazione si usa raise ValidationError(<messaggio>).
    - Per fare la integrazione con Bootstrap, quando si definiscono i campi del form, nel dizionario attrs
      basta specificare la classe di Bootstrap che vogliamo:
      Ex.: nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))'''
class ContattoForm(forms.Form):

    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cognome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}))
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!",
                                                             "class": "form-control"}),
                                                             validators=[validators.MinLengthValidator(10)])

    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
