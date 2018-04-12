from django.db import models
from clientes.models import Client
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

class Favorite(models.Model):
	user = models.ForeignKey(Client, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.user.nombre, self.product.nombre)

	class Meta:
		verbose_name='Favorite'
		verbose_name_plural = 'Favorites'

