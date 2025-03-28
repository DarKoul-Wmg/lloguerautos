from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from lloguer.models import Automobil
from .forms import ReservaForm

def lista_autos(request):
    autos = Automobil.objects.all()  # Obtener todos los autos de la base de datos
    return render(request, "lloguer/autos.html", {"autos": autos})


def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_autos') 
    else:
        form = ReservaForm()

    return render(request, 'lloguer/crear_reserva.html', {'form': form})