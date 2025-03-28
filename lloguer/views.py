from django.shortcuts import render
from lloguer.models import Automobil  # Asegúrate de que este es el modelo correcto

def autos(request):
    automoviles = Automobil.objects.all()  # Obtiene todos los automóviles
    return render(request, 'autos.html', {'automoviles': automoviles})