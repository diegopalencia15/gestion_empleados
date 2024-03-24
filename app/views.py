from django.shortcuts import render
from django.http import HttpResponse
from .models import Salarios,Puestos

# Create your views here.
def index(request):

  return render(request, 'index.html', {})

def salario(request):

  return render(request, "salarios.html", {})

def crear_salario(request):
  valor = request.GET['valor']
  if 'extra_jun' in request.GET:
    extra_jun = True
  else:
    extra_jun = False

  if 'extra_dic' in request.GET:
    extra_dic = True
  else:
    extra_dic = False

  salario = Salarios(valor = valor, extra_jun=extra_jun, extra_dic=extra_dic)

  salario.save()

  print(valor)
  return HttpResponse("Hola")

def puesto(request):
  salario=Salarios.objects.all()
  return render (request,'puestos.html',{'salario':salario})

def crear_puesto(request):
  cargo = request.GET['cargo']
  descripcion = request.GET["descripcion"]
  salario = Salarios.objects.get(id=request.GET["salario"])

  puesto = Puestos(cargo=cargo, descripcion=descripcion, salario=salario)
  puesto.save()
  return HttpResponse("Puesto de trabajo creado")

