from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:perro_id>/', views.detalle, name='detalle'),
    path('inicio', views.cargarInicio, name='cargarInicio'),
    path('inicio/formulario', views.cargarFormulario, name='cargarFormulario'),
    path('inicio/grabarUsuario', views.grabarUsuario, name='grabarUsuario'),

    path('inicio/formularioPerros', views.cargarFormularioPerros, name='cargarFormularioPerros'),
    path('inicio/grabarPerro', views.grabarPerro, name='grabarPerro'),

    path('inicio/listadoRescatados', views.cargarRescatados, name='cargarRescatados'),
    
]