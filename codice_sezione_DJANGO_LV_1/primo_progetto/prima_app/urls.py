from django.urls import path

from prima_app import views as prima_app_views

urlpatterns = [
    path('spam/', prima_app_views.homepage, name='home')
]
