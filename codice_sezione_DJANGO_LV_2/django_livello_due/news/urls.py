from django.urls import path
import news.views as view

urlpatterns = [
    path('', view.home, name="homeview")
]
