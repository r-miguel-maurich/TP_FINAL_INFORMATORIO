from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from aplicacion.models import Usuario, Pregunta

def hola(request):
    return HttpResponse("Holasss")
"""
class Home(ListView):
    model = usuario
    template_name = "paginas/home.html"
"""

class Home(ListView):
    model = Usuario
    template_name = "paginas/home.html"

class Login(ListView):
    model = Usuario
    template_name = "paginas/login.html"

class Index(ListView):
    template_name = "template/paginas/admin.html"
    #template_name = "lib/python3.8/site-packages/bootstrap4/forms.py"

class Crear(CreateView):
    template_name = "paginas/crear.html"

class Listar(ListView):
#    model = Pregunta
    template_name = "paginas/listar.html"

    def get_queryset(self):
        return Pregunta.objects.all()
    #def get_context_data(self)
