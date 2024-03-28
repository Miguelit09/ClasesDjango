from django.urls import path
from . import views

urlpatterns = [
    path('mostrar_registrar/', views.mostrar_registrar, name="mostrar_registrar"),
    path('registrar_curso_url/<str:cn>/<str:d>/<str:m>', views.registrar_curso_url, name="registrar_curso_url"),
    path('registrar_curso_form/', views.registrar_curso_form, name="registrar_curso_form"),
]