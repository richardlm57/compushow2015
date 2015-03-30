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
			return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))
	else:
		form = LoginForm()
	return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
