from django.shortcuts import render
from .models import Perro
from django.template import loader
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. Aplicación perris.")

def detalle(request, perro_id):
    return HttpResponse("You're looking at dog %s." % perro_id)

def cargarInicio(request):
    return render(request, 'perris/index.html')

def cargarFormulario(request):
    return render(request, 'perris/formulario.html')

def cargarFormularioPerros(request):
    return render(request, 'perris/formularioPerros.html')

def grabarPerro(request):
    nombre = request.POST['txtNombre']
    raza = request.POST['txtRaza']
    descr = request.POST['txtDescrip']
    estado = request.POST['cmbEstado']
    #d = Departamento(nombre = 'El nombre del depto')
    p = Perro(nombre = nombre, raza = raza, descripcion = descr, estado = estado)
    p.save()
    return render(request, 'perris/grabarPerro.html',
                  {'nombre' : nombre})
# Create your views here.
