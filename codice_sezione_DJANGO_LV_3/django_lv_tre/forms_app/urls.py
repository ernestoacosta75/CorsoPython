from django.urls import path, include
from .views import contatti, homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contattaci/', contatti, name='contatti')
]
