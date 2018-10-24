from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. Aplicación perris.")

def detalle(request, perro_id):
    return HttpResponse("You're looking at dog %s." % perro_id)

def cargarInicio(request):
    return render(request, 'perris/index.html')

def cargarFormulario(request):
    return render(request, 'perris/formulario.html')

# Create your views here.
