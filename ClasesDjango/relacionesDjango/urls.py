from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_registrar/', views.mostrar_registrar, name="mostrar_registrar"),
    path('registrar_curso_url/<str:cn>/<str:d>/<str:m>', views.registrar_curso_url, name="registrar_curso_url"),
    path('registrar_curso_form/', views.registrar_curso_form, name="registrar_curso_form"),
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
    path('mostrar_editar/', views.mostrar_editar, name="mostrar_editar"),
    path('editar_curso/', views.editar_curso, name="editar_curso"),
    path('eliminar_curso/<int:id>/', views.eliminar_curso, name="eliminar_curso"),
    path('mostrar_registrar_estudiante/', views.mostrar_registrar_estudiante, name="mostrar_registrar_estudiante"),
    path('registrar_estudiante/', views.registrar_estudiante, name="registrar_estudiante"),
    path('crear_registros/', views.crear_registros, name="crear_registros"),
]