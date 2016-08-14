from django import forms
from .models import Afectado

class FrmAfectado(forms.ModelForm):
	"""docstring for FrmAfectado"""
	class Meta:
		model = Afectado
		fields = ('cedula_afectado','telf_afecto','nombre','apellido','direccion',)