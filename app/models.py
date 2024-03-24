from django.db import models
from datetime import date

# Create your models here.

class Paises(models.Model):
    nombre_pais = models.CharField(max_length=50)

class Poblaciones(models.Model):
    nombre_poblacion = models.CharField(max_length=50)
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)

class Fabricas(models.Model):
    nombre_fabrica = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    codigo_postal = models.IntegerField(max_length=10)
    poblacion = models.ForeignKey(Poblaciones, on_delete=models.CASCADE)

class Salarios(models.Model):
    valor = models.IntegerField(max_length=10)
    extra_jun = models.BooleanField(default=False)
    extra_dic = models.BooleanField(default=False)

class Puestos(models.Model):
    cargo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    salario = models.ForeignKey(Salarios, on_delete=models.CASCADE)

class Empleados(models.Model):
    documento = models.IntegerField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    puesto = models.ForeignKey(Puestos, on_delete=models.CASCADE)
    fabrica = models.ForeignKey(Fabricas, on_delete=models.CASCADE)