from django.urls import path
import libreria.views as view

urlpatterns = [
    path('', view.LibriListViewCB.as_view(), name="homepage"),
    path('profilo_autore/<int:pk>', view.AutoreDetailViewCB.as_view(), name="profilo_autore")
    # path('lista_articoli/', view.ArticoloListViewCB.as_view(), name="lista_articoli")
]
