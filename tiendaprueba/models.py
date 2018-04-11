from django.db import models

# Create your models here.

class Product(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	categoria = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	imagen = models.ImageField(blank=True)
	
	def __str__(self): 
		return self.nombre

	class Meta:
		ordering = ('id',)
