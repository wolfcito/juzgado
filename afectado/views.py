from django.shortcuts import render
from .models import Afectado

def lista_afectados(request):
	return render(request, 'afectado/lista_afectados.html', {})
	