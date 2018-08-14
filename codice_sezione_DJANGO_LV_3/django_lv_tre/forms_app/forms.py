from django import forms

class ContattoForm(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}))
