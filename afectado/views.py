from django.shortcuts import render, get_object_or_404, redirect
from .models import Afectado
from .forms import FrmAfectado

def inicio(request):
	usuario = "Invitado"
	return render(request, 'afectado/inicio.html',{'usuario':usuario})

def lista_afectados(request):
	listado = Afectado.objects.order_by('cedula_afectado')
	return render(request, 'afectado/lista_afectados.html', {'listado':listado})

def detalle_afectado(request,id):
	detalle = get_object_or_404(Afectado, id_afectado=id)
	return render(request, 'afectado/detalle_afectado.html',{'detalle':detalle})

def nuevo_afectado(request):
	if request.method == "POST":
		form = FrmAfectado(request.POST)
		if form.is_valid():
			unAfectado = form.save()
			return redirect('afectado.views.detalle_afectado',id=unAfectado.id_afectado)
	else:
		form = FrmAfectado()
	return render(request,'afectado/nuevo_afectado.html',{'form':form})

def editar_afectado(request,id):
	edicion = get_object_or_404(Afectado, id_afectado = id)
	if request.method == "POST":
		form = FrmAfectado(request.POST, instance = edicion)
		if form.is_valid():
			edicion = form.save()
			return redirect('afectado.views.detalle_afectado',id=edicion.id_afectado)
	else:
		form = FrmAfectado(instance=edicion)
	return render(request,'afectado/nuevo_afectado.html',{'form':form})
