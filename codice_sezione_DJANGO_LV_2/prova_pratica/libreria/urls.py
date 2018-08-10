from django.urls import path
import libreria.views as view

urlpatterns = [
    path('', view.home, name="homeview"),
    # path('profilo_autore/<int:pk>', view.AutoreDetailViewCB.as_view(), name="articolo_detail"),
    # path('lista_articoli/', view.ArticoloListViewCB.as_view(), name="lista_articoli")
]
