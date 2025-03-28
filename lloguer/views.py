from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from lloguer.models import Automobil

def lista_autos(request):
    autos = Automobil.objects.all()  # Obtener todos los autos de la base de datos
    return render(request, "lloguer/autos.html", {"autos": autos})
