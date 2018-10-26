from django.db import models

class Perro(models.Model):
	nombre = models.CharField(max_length=30)
	raza = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=60)
	ESTADOS=(('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
	estado = models.CharField(max_length=1, choices=ESTADOS,default='R')
	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	correo = models.CharField(max_length=60)
	run = models.CharField(max_length=10)
	nombre_completo = models.CharField(max_length=60)
	fecha_nac = models.DateField()
	telefono = models.IntegerField()
	VIVIENDAS=(('CPG','Casa con patio grande'),('CPP','Casa con patio pequeño'),('CSP','Casa sin patio'),('DEP','Departamento'))
	vivienda = models.CharField(max_length=3, choices=VIVIENDAS,default='CPG')
	def __str__(self):
		return self.nombre_completo
# Create your models here.
