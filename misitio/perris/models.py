from django.db import models

class Perro(models.Model):
	nombre = models.CharField(max_length=30)
	raza = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=60)
	ESTADOS=(('R','Rescatado'),('D','Disponible'),('A','Adoptado'))
	estado = models.CharField(max_length=1, choices=ESTADOS,default='R')
# Create your models here.
