from django.shortcuts import render_to_response, redirect
from django.http import Http404,HttpResponse,HttpRequest
from django.template import RequestContext
from django.views.generic import View
from compushow_app.forms import *
from compushow_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.

def login(request):
    nominaciones=[  'CompuChill',
                    'CompuGordito',
                    'CompuProductista',
                    'CompuCartoon',
                    'CompuComadre',
                    'CompuCompadre',
                    'CompuLove',
                    'CompuCuchi',
                    'CompuIntenso',
                    'CompuPregunton',
                    'CompuFitness',
                    'CompuTeam',
                    'CompuMaster',
                    'CompuPro',
                    'CompuPapi',
                    'CompuMami']
    nombre_nominacion="CompuChill"
    if request.method == 'POST':
        form = Login_Signup_Form(request.POST)
        if form.is_valid():
            carnet=form.cleaned_data['Carnet']
            password=form.cleaned_data['Password']
            user = authenticate(username=carnet, password=password)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    auth_login(request,user)
                    # return render_to_response('nominaciones.html',{'form':form,'nominaciones':nominaciones,'nombre_nominacion':nombre_nominacion},context_instance=RequestContext(request))
                    return redirect('nombre_nominacion', nombre='CompuChill')
                else:
                    print("The password is valid, but the account has been disabled!")
                    return render_to_response('login.html',{'form':form,'nominaciones':nominaciones,'nombre_nominacion':nombre_nominacion},context_instance=RequestContext(request))
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
                return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))
    else:
        form = Login_Signup_Form()
    return render_to_response('login.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url='')
def Nominacion(request,nombre):
    nominaciones=[  'CompuChill',
                    'CompuGordito',
                    'CompuProductista',
                    'CompuCartoon',
                    'CompuComadre',
                    'CompuCompadre',
                    'CompuLove',
                    'CompuCuchi',
                    'CompuIntenso',
                    'CompuPregunton',
                    'CompuFitness',
                    'CompuTeam',
                    'CompuMaster',
                    'CompuPro',
                    'CompuPapi',
                    'CompuMami']
    if nombre in nominaciones:
        nombre_nominacion = nombre
        return render_to_response('nominaciones.html',locals(),context_instance=RequestContext(request))
    else:
        auth_logout(request)
        return redirect('compushow_app.views.login')

def signup(request):
	if request.method == 'POST':
		form = Login_Signup_Form(request.POST)
		if form.is_valid():
			carnet=form.cleaned_data['Carnet']
			password=form.cleaned_data['Password']
			user = User.objects.create_user(carnet, '', password)
			user.save()
			return redirect('compushow_app.views.login')
	else:
		form = Login_Signup_Form()
	return render_to_response('signup.html',{'form':form},context_instance=RequestContext(request))

@login_required(login_url='')
def logout(request):
    auth_logout(request)
    return redirect('compushow_app.views.login')
