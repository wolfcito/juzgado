from django.shortcuts import render, get_object_or_404
from .models import Afectado

def lista_afectados(request):
	listado = Afectado.objects.order_by('cedula_afectado')
	return render(request, 'afectado/lista_afectados.html', {'listado':listado})

def detalle_afectado(request,id):
	detalle = get_object_or_404(Afectado, id_afectado=id)
	return render(request, 'afectado/detalle_afectado.html',{'detalle':detalle})