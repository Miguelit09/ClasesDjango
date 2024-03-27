from django.db import models
from datetime import date
# Create your models here.




class Curso(models.Model):
    OPCIONES_MATERIAS = [
        ("Programación", "Opción 1"),
        ("Comunicacion", "Opción 2"),
        ("Diseño", "Opción3"),
    ]
    curso_nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    materia = models.CharField(choices=OPCIONES_MATERIAS, max_length=50)


class Estudiante(models.Model):
    estudiante_nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

class Perfil(models.Model):
    fecha_registro = models.DateField(default=date.today)
    contraseña = models.CharField(max_length=100)
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)

class Instructor(models.Model):
    instructor_nombre = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso)