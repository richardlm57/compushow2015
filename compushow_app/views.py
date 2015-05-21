from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from django.http import Http404,HttpResponse,HttpRequest
from django.template import RequestContext
from django.views import generic
from django.views.generic import View,ListView
from compushow_app.forms import *
from compushow_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
import json

# Create your views here.

def login(request):
    mensaje = 'El evento del trimestre!!'
    # if request.session.get('mensaje') is not None:
    #     mensaje=request.session.get('mensaje')
    if request.method == 'POST':
        form = Login_Signup_Form(request.POST)
        if form.is_valid():
            carnet   = form.cleaned_data['Carnet']
            password = form.cleaned_data['Password']
            user     = authenticate(username=carnet, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('bien', idU=user.pk)
                else:
                    return render_to_response('login-registro/login.html',{
                        'form':form
                        }, context_instance=RequestContext(request))
            else:
                return render_to_response('login-registro/login.html',{
                    'form':form,
                    'mensaje':"El usuario o la contraseña fue incorrecta"
                    }, context_instance=RequestContext(request))
    else:
        form = Login_Signup_Form()
    return render_to_response('login-registro/login.html', {
        'form':form,
        'mensaje':mensaje
        }, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            compu    = form.cleaned_data['Computista']
            comp     = list(Computista.objects.filter(nombre=compu))[0]
            password = form.cleaned_data['Password']
            cpword   = form.cleaned_data['Cpassword']
            
            exist = User.objects.filter(username=comp.carnet)
            if exist:
                return render_to_response('login-registro/signup.html', {
                'form':form,
                'mensaje': "Usuario registrado. Contacta por cualquier problema"
                }, context_instance=RequestContext(request))
            if password == cpword:
                user = User.objects.create_user(comp.carnet, '', password)
                user.save()
                return HttpResponseRedirect('/')
        else:
            return render_to_response('login-registro/signup.html', {
                'form':form,
                'mensaje': "No coincide la clave"
                }, context_instance=RequestContext(request))
    else:
        form = SignupForm()
    return render_to_response('login-registro/signup.html', {
        'form':form
        }, context_instance=RequestContext(request))

def get_computistas(request):
    if request:
        term = request.GET.get('term', '')
        cs = Computista.objects.all()
        results = []
        for c in cs:
            if term in c.carnet:
                c_json = {}
                c_json['id'] = c.pk
                c_json['label'] = c.carnet
                c_json['value'] = c.nombre
                results.append(c_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def get_computistas_nombre(request):
    if request:
        term = request.GET.get('term', '')
        cs = Computista.objects.all()
        results = []
        split = []
        for c in cs:
            split = c.nombre.split()
            for s in split:
                if term.lower() in s.lower():
                    c_json = {}
                    c_json['id'] = c.pk
                    c_json['label'] = c.nombre
                    c_json['value'] = c.nombre
                    results.append(c_json)
                    break
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

@login_required(login_url='')
def welcome(request, idU):
    nominaciones = Categoria.objects.all()
    mensaje = "Bienvenido a las nominaciones del Compushow"

    return render_to_response('welcome.html', {
        'mensaje':mensaje,
        'userId':idU,
        'nominaciones':nominaciones
        }, context_instance=RequestContext(request))

@login_required(login_url='')
def nominacion(request, idU, name):
    nominaciones = Categoria.objects.all()
    lista        = list(Categoria.objects.filter(nombre=name))
    if lista:
        if request.POST:
            form = NominacionForm(request.POST)
            if form.is_valid():
                nmdr = list(User.objects.filter(pk=idU))[0]
                nmdo = list(Computista.objects.filter(nombre=form.cleaned_data['nominado']))[0]
                catg = name
                nmin = Nominacion.objects.create(nominador=nmdr,
                                                 nominado=nmdo,
                                                 categoria=catg)
                #nmin.save()
        else:
            form = NominacionForm()
        return render_to_response('nominar/nominaciones.html', {
            'form': form,
            'nombre_nominacion':lista[0],
            'nominaciones':nominaciones
            }, context_instance=RequestContext(request))
    return HttpResponseRedirect('/nominacion/CompuChill')

@login_required(login_url='')
def logout(request):
    auth_logout(request)
    request.session['mensaje'] = 'El cierre de sesión ha sido exitoso'
    return redirect('compushow_app.views.login')
