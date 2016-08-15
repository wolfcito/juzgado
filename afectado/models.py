from django.db import models

class Afectado(models.Model):
	id_afectado = models.AutoField(primary_key=True)
	cedula_afectado = models.CharField(max_length = 100)
	telf_afectado = models.CharField(max_length = 16)
	nombre_afectado = models.CharField(max_length = 32)
	apellido_afectado = models.CharField(max_length = 32)
	direccion_afectado = models.TextField()
	"""docstring for Afectado"""
	def envio(self):
		self.save()
	def __str__(self):
		return self.nombre_afectado
