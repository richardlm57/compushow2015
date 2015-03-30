from django.shortcuts import render_to_response
from django.http import Http404,HttpResponse
from django.template import RequestContext
from django.views.generic import View
import datetime


# Create your views here.

def login(request):
	return render_to_response('login.html',locals(),context_instance=RequestContext(request))
