from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def mostrar_registrar(request):
    return render(request, 'registrar.html', {})

def registrar_curso_url(request, cn, d, m): # cn = curso_nombre // d=descripcion // m=materia
    nuevo_curso = Curso(curso_nombre=cn, descripcion=d, materia=m)
    nuevo_curso.save()
    return HttpResponse("Se registró el curso")

def registrar_curso_form(request):
    curso_nombre = request.POST['curso_nombre']
    descripcion = request.POST['descripcion']
    materia = request.POST['materia']
    Curso.objects.create(curso_nombre=curso_nombre, descripcion=descripcion, materia=materia)
    return HttpResponse("Se registró el curso por formulario")