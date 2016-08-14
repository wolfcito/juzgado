from django.shortcuts import render
from .models import Afectado

def lista_afectados(request):
	listado = Afectado.objects.order_by('cedula_afectado')
	return render(request, 'afectado/lista_afectados.html', {'listado':listado})
	