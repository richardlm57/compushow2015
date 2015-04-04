from django.shortcuts import render_to_response
from django.http import Http404,HttpResponse,HttpRequest
from django.template import RequestContext
from django.views.generic import View
from compushow_app.forms import *
import datetime


# Create your views here.

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			carnet=form.cleaned_data['Carnet']
			password=form.cleaned_data['Password']
			return render_to_response('CompuChill.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm()
	return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

def CompuChill(request):
	return render_to_response('CompuChill.html',locals(),context_instance=RequestContext(request))

def CompuGordito(request):
	return render_to_response('CompuGordito.html',locals(),context_instance=RequestContext(request))

def CompuProductista(request):
	return render_to_response('CompuProductista.html',locals(),context_instance=RequestContext(request))

def CompuCartoon(request):
	return render_to_response('CompuCartoon.html',locals(),context_instance=RequestContext(request))

def CompuComadre(request):
	return render_to_response('CompuComadre.html',locals(),context_instance=RequestContext(request))

def CompuCompadre(request):
	return render_to_response('CompuCompadre.html',locals(),context_instance=RequestContext(request))

def CompuLove(request):
	return render_to_response('CompuLove.html',locals(),context_instance=RequestContext(request))

def CompuCuchi(request):
	return render_to_response('CompuCuchi.html',locals(),context_instance=RequestContext(request))

def CompuIntenso(request):
	return render_to_response('CompuIntenso.html',locals(),context_instance=RequestContext(request))

def CompuPregunton(request):
	return render_to_response('CompuPregunton.html',locals(),context_instance=RequestContext(request))

def CompuFitness(request):
	return render_to_response('CompuFitness.html',locals(),context_instance=RequestContext(request))

def CompuTeam(request):
	return render_to_response('CompuTeam.html',locals(),context_instance=RequestContext(request))

def CompuMaster(request):
	return render_to_response('CompuMaster.html',locals(),context_instance=RequestContext(request))

def CompuPro(request):
	return render_to_response('CompuPro.html',locals(),context_instance=RequestContext(request))

def CompuPapi(request):
	return render_to_response('CompuPapi.html',locals(),context_instance=RequestContext(request))

def CompuMami(request):
	return render_to_response('CompuMami.html',locals(),context_instance=RequestContext(request))