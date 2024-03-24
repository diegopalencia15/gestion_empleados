from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name="inicio"),
    path('salarios/', views.salario, name="salarios"),
    path('crear_salario/', views.crear_salario, name = "crear_salario"),
    path('puestos/', views.puesto, name="puestos"),
    path('crear_puesto/', views.crear_puesto, name = "crear_puesto"),
]