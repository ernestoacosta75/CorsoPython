from django.urls import path
import news.views as view

urlpatterns = [
    path('', view.home, name="homeview"),
    # path('articoli/<int:pk>', view.articoloDetailView, name="articolo_detail"),
    path('articoli/<int:pk>', view.ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path('lista_articoli/', view.ArticoloListViewCB.as_view(), name="lista_articoli")
]
