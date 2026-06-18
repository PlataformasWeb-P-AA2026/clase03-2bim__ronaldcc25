"""
Manejo de urls para la aplicación
administrativo
"""

from django.urls import path

# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listado-estudiantes", views.listadoEstudiantes, name="listadoEstudiates"),
    path(
        "listado/estudiantes/dos",
        views.listadoEstudiantesDos,
        name="listadoEstudiatesDos",
    ),
    path(
        "listado/estudiantes/personalizado",
        views.listadoEstudiantesTelefono,
        name="listadoEstudiantesTelefono",
    ),
]
