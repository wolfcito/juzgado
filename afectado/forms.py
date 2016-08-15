from django.utils.translation import ugettext_lazy as _
from django.forms import widgets, TextInput, Textarea
from django import forms
from .models import Afectado

class FrmAfectado(forms.ModelForm):
	"""docstring for FrmAfectado"""
	class Meta:
		model = Afectado
		fields = ('cedula_afectado','telf_afectado','nombre','apellido','direccion',)
		labels = {	'cedula_afectado': _('Cédula'),
					'telf_afectado': _('Teléfono/Celular'),
					'nombre': _('Nombre(s)'),
					'apellido': _('Apellido(s)'),
					'direccion': _('Dirección'),}
		widgets = {	'cedula_afectado':TextInput(attrs={'class': 'form-control'}),
					'telf_afectado':TextInput(attrs={'class': 'form-control'}),
					'nombre':TextInput(attrs={'class': 'form-control'}),
					'apellido':TextInput(attrs={'class': 'form-control'}),
					'direccion':Textarea(attrs={'class': 'form-control','rows': 2}),}