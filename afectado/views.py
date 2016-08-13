from django.shortcuts import render

def home(request):
	return render_to_response('afectado.html')
