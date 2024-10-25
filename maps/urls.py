# maps/urls.py
from django.urls import path
from .views import get_coordinates

urlpatterns = [
    path('api/coordinates/', get_coordinates, name='get_coordinates'),
]
