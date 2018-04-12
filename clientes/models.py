from django.db import models


# Create your models here.

class Client(models.Model):
	nombre = models.CharField(max_length=255)
	telefono = models.IntegerField(unique=True)
	email = models.EmailField(max_length=255)
	direccion = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('id',)
