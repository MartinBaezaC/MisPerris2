from django.shortcuts import render
from .models import Perro, Usuario
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return HttpResponse("Hola mundo. Aplicación perris.")

def detalle(request, perro_id):
    return HttpResponse("You're looking at dog %s." % perro_id)

def cargarInicio(request):
    return render(request, 'perris/index.html')

def cargarFormulario(request):
    return render(request, 'perris/formulario.html')

@user_passes_test(lambda u: u.is_superuser)
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

def grabarUsuario(request):
    correo = request.POST['txtEmail']
    run = request.POST['txtRun']
    nombre_completo = request.POST['txtNombre']
    fecha_nac = request.POST['txtFechaNac']
    telefono =request.POST['txtTelefono']
    region =request.POST['txtRegion']
    ciudad =request.POST['txtCity']
    vivienda =request.POST['cmbVivienda']
    #d = Departamento(nombre = 'El nombre del depto')
    u = Usuario(correo = correo, run = run, nombre_completo = nombre_completo, fecha_nac = fecha_nac, telefono = telefono, region = region, ciudad= ciudad, vivienda = vivienda)
    u.save()
    return render(request, 'perris/grabarUsuario.html',
                  {'nombre_completo' : nombre_completo})

def cargarRescatados(request):	
	#Obtenemos los departamentos ordenados de manera descendente.
	#[Z-A] Se antepone el signo menos (-)
    rescatadosRecuperados = Perro.objects.exclude(estado='A')

    #Cargamos el archivo index.html que se encuentra en la carpeta 'templates'
    template = loader.get_template('perris/cargarRescatados.html')

    #Creamos el nombre 'deptos' para reutilizarlo en el archivo 'index.html'
    context = {
        'perros': rescatadosRecuperados,
    }

    #Invocamos la página de respuesta 'index.html'
    return HttpResponse(template.render(context, request))
# Create your views here.
