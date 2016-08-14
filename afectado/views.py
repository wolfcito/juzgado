from django.shortcuts import render

def lista_afectados(request):
	return render(request, 'afectado/lista_afectados.html', {})
	