from django.http import HttpResponse

def index(response):
  return HttpResponse ('Inicio')

