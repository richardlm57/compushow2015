from django.db import models
from django.contrib.auth.models import User

# Estudiantes, profesores, agrupaciones.
class Computista(models.Model):
    carnet = models.CharField(max_length=8)
    nombre = models.CharField(max_length=70)

class Foto(models.Model):
    imagen = models.ImageField(upload_to = "images/")

# # Total de categorias del CompuShow
class Categoria(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128)

class Nominacion(models.Model):
    nominador = models.ForeignKey(User)
    nominado  = models.ForeignKey(Computista)
    categoria = models.ForeignKey(Categoria)
    foto      = models.ForeignKey(Foto, null=True)
    descrp    = models.CharField(max_length=80, null=True)