from django.shortcuts import render

# Create your views here.
from landing.models import Peticion, Galeria_fotos


def index_view(request):
    return render(request, 'index.html')


def servicios(request):
    return render(request, 'servicios.html')


def produccion(request):
    return render(request, 'produccion.html')


def galeria(request):
    fotos = Galeria_fotos.objects.all()
    return render(request, 'galeria.html', {'fotos':fotos})


def peticion(request):
    """Procesa una petición y guarda los datos en la BBDD"""
    if request.method == 'POST':
        peticion = Peticion()
        peticion.nombre = request.POST['nombre']
        peticion.telefono = request.POST['telefono']
        peticion.email = request.POST['email']
        peticion.texto = request.POST['texto']
        if request.POST['emailcomercial'] == 'on':
            peticion.emailcomercial = True
        else:
            peticion.emailcomercial = False
        if request.POST['consentimiento'] == 'on':
            peticion.consentimiento = True
        peticion.save()
        
    return render(request, 'contacto.html', {'peticion': peticion})