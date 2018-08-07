from django.urls import path
from .views import view_a, view_b, view_c

urlpatterns = [
    path('', view_a, name='primaview'),
    path('view_b/', view_b, name='viewb'),
    path('view_c/', view_c, name='viewc'),
]
