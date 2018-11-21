from django.urls import path , include

from .models import Perro, Usuario
from rest_framework import routers, serializers, viewsets

from . import views

class PerroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perro
        fields = ('url', 'nombre', 'raza', 'descripcion')

# ViewSets define the view behavior.
class PerroViewSet(viewsets.ModelViewSet):
    queryset = Perro.objects.all()
    serializer_class = PerroSerializer

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('url', 'nombre_completo', 'correo', 'run')

# ViewSets define the view behavior.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

router = routers.DefaultRouter()
router.register(r'perros', PerroViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('salir', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('<int:perro_id>/', views.detalle, name='detalle'),
    path('inicio', views.cargarInicio, name='cargarInicio'),
    path('inicio/formulario', views.cargarFormulario, name='cargarFormulario'),
    path('inicio/grabarUsuario', views.grabarUsuario, name='grabarUsuario'),

    path('inicio/formularioPerros', views.cargarFormularioPerros, name='cargarFormularioPerros'),
    path('inicio/grabarPerro', views.grabarPerro, name='grabarPerro'),

    path('inicio/listadoRescatados', views.cargarRescatados, name='cargarRescatados'),

    path('mi-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]