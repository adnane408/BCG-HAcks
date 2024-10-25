from django.shortcuts import render

# Create your views here.
# maps/views.py
from django.http import JsonResponse

def get_coordinates(request):

    data = {
        "latitude": 48.8566,
        "longitude": 45.3522,
        "result" : True
    }
    return JsonResponse(data)

