from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:perro_id>/', views.detalle, name='detalle'),
    path('inicio', views.cargarInicio, name='cargarInicio'),
    path('inicio/formulario', views.cargarFormulario, name='cargarFormulario'),
]