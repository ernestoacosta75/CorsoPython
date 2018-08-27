from django import forms
from .models import BlogPostModel

'''- Per facilitare il lavoro e rispettare il principio D.R.Y, Django ci fornisce la classe
     django.forms.ModelForm
   - Ciascun ModelForm dispone anche di un metodo save() che ci permette di creare e modificare
     oggeti dentro al database. '''
class BlogPostModelForm(forms.ModelForm):

    class Meta:
        model = BlogPostModel
        fields = "__all__"
