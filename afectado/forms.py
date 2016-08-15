from django.utils.translation import ugettext_lazy as _
from django.forms import widgets, TextInput, Textarea
from django import forms
from .models import Afectado

class FrmAfectado(forms.ModelForm):
	"""docstring for FrmAfectado"""
	class Meta:
		model = Afectado
		fields = ('cedula_afectado','telf_afectado','nombre_afectado','apellido_afectado','direccion_afectado',)
		labels = {	'cedula_afectado': _('Cédula'),
					'telf_afectado': _('Teléfono/Celular'),
					'nombre_afectado': _('Nombre(s)'),
					'apellido_afectado': _('Apellido(s)'),
					'direccion_afectado': _('Dirección'),}
		widgets = {	'cedula_afectado':TextInput(attrs={'class': 'form-control'}),
					'telf_afectado':TextInput(attrs={'class': 'form-control'}),
					'nombre_afectado':TextInput(attrs={'class': 'form-control'}),
					'apellido_afectado':TextInput(attrs={'class': 'form-control'}),
					'direccion_afectado':Textarea(attrs={'class': 'form-control','rows': 2}),}