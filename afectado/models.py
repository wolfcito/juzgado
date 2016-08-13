from django.db import models

class Afectado(models.Model):
	id_afectado = models.AutoField(primary_key=True)
	cedula_afectado = models.CharField(max_length = 100)
	telf_afecto = models.CharField(max_length = 16)
	nombre = models.CharField(max_length = 32)
	apellido = models.CharField(max_length = 32)
	direccion = models.TextField()
	"""docstring for Afectado"""
	def envio(self):
		self.save()
	def __afectado__(self):
		return self.nombre
