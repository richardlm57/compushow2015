from django.db import models
from django.contrib.auth.models import User

# Cada etapa establece restricciones distintas en el sistema.
# ETAPAS = (
#   ('0','CERRADO'),
#   ('1','NOMINANDO'),
#   ('2','FILTRANDO'),
#   ('3','VOTANDO'),
# )

# class Edicion(models.Model):
#     anio    = models.IntegerField(primary_key = True)
#     activa  = models.BooleanField(default=False)
#     etapa   = models.CharField(max_length = 1, choices = ETAPAS)

# Estudiantes, profesores, agrupaciones.
class Computista(models.Model):
    carnet = models.CharField(max_length=8)
    nombre = models.CharField(max_length=70)

class Foto(models.Model):
    imagen = models.ImageField(upload_to = "images/")
#     descripcion  = models.CharField(max_length = 128)

#     def vistaPrevia(self):
#         pass

#     def delete(self, *args, **kwargs):
#         self.imagen.delete(save = False)
#         super(Foto, self).delete(*args, **kwargs)

# # Total de categorias del CompuShow
class Categoria(models.Model):
    nombre      = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=128)

#     def nominados(self):
#         pass

class Nominacion(models.Model):
    nominador = models.ForeignKey(User)
    nominado  = models.ForeignKey(Computista)
    categoria = models.ForeignKey(Categoria)

# class Nominado(models.Model):
#     computista  = models.ForeignKey(Computista)
#     categoria = models.ForeignKey(Categoria)
#     foto        = models.ForeignKey(Foto)

# Faltan votaciones