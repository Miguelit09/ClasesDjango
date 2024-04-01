from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso, Estudiante, Instructor, Perfil
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

def listar_cursos(request):
    obtener_cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {
        'lista_cursos': obtener_cursos
    })

def mostrar_editar(request):
    return render(request, 'editar_curso.html', {})

def editar_curso(request):
    id_curso = request.POST['id_curso']
    curso_nombre = request.POST['curso_nombre']
    descripcion = request.POST['descripcion']
    materia = request.POST['materia']

    editar = Curso.objects.get(id=id_curso)
    editar.curso_nombre = curso_nombre
    editar.descripcion = descripcion
    editar.materia = materia

    editar.save()

    return HttpResponse("Se editó el curso por formulario")

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('mostrar_registrar')

def mostrar_registrar_estudiante(request):
    cursos = Curso.objects.all()
    return render(request, 'registrar_estudiante.html', {
        'cursos': cursos
    })

def registrar_estudiante(request):
    estudiante_nombre = request.POST['estudiante_nombre']
    edad = request.POST['edad']
    direccion = request.POST['direccion']
    curso_id = request.POST['curso_id']
    curso = Curso.objects.get(id=curso_id)
    Estudiante.objects.create(estudiante_nombre=estudiante_nombre, edad=edad, direccion=direccion, curso=curso)
    return HttpResponse("Se registró el estudiante.")



def crear_registros(request):

# CREAR REGISTROS 

    # Instructor.objects.create(instructor_nombre="Jhon")
    # Instructor.objects.create(instructor_nombre="Enzy")
    # Instructor.objects.create(instructor_nombre="Otro instructor")
    # Perfil.objects.create(contraseña="pepito", estudiante=estudiante)

# CONSULTAS UNO A UNO Y UNO A MUCHOS
    
    # valentina = Estudiante.objects.get(id=1)

    # return HttpResponse(f"El curso de valentina se llama: {valentina.curso.curso_nombre}. Este curso trata de: {valentina.curso.descripcion}. De la materia: {valentina.curso.materia}.\nLa contraseña de valentina es: {valentina.perfil.contraseña}. Se registro en la fecha: {valentina.perfil.fecha_registro}")

# INSTRUCTORES
    jhon = Instructor.objects.get(id=1)
    enzy = Instructor.objects.get(id=2)
    otro_instructor = Instructor.objects.get(id=3)

# CURSOS
    actualizando = Curso.objects.get(id=2)
    clasesitas_django = Curso.objects.get(id=3)
    intermedio = Curso.objects.get(id=6)

    cursos = enzy.cursos.all()

    instructores = actualizando.instructor_set.all()
# RELACIONAR REGISTROS MUCHOS A MUCHOS

    # jhon.cursos.add(actualizando)
    # enzy.cursos.add(actualizando, clasesitas_django)
    # otro_instructor.cursos.add(actualizando, clasesitas_django, intermedio)
    return render(request, 'instructor_curso.html', {
        'instructores':instructores,
        'curso': actualizando,
        'cursos': cursos,
        'instructor': enzy
    })