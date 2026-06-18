from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

# importar las clases de models.py
from administrativo.models import *

# Create your views here.


def index(request):
    # return HttpResponse("Hola mundo desde Python")
    return HttpResponse("Hola mundo desde Python en UTPL<br/><br/>%s" % (request.path))


def listadoEstudiantes(request):
    """
    Listar los registros del modelo Estudiante,
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    titulo = "Listado de estudiantes de mi aplicación"
    informacion_template = {
        "estudiantes": estudiantes,
        "numero_estudiantes": len(estudiantes),
        "mititulo": titulo,
    }
    return render(request, "listadoEstudiantes.html", informacion_template)


def listadoEstudiantesDos(request):
    """
    Listar los registros del modelo Estudiante,
    obtenidos de la base de datos.
    """
    estudiantes = Estudiante.objects.all()
    mis_numeros_telefonicos = NumeroTelefonico.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {
        "estudiantes": estudiantes,
        "numero_estudiantes": len(estudiantes),
        "mis_numeros_telefonicos": mis_numeros_telefonicos,
    }
    return render(request, "listadoEstudiantesDos.html", informacion_template)


def listadoEstudiantesTelefono(request):
    estudiantes = Estudiante.objects.all()
    mis_numeros_telefonicos = NumeroTelefonico.objects.all()
    informacion_template = {
        "estudiantes": estudiantes,
        "mis_numeros_telefonicos": mis_numeros_telefonicos,
    }
    return render(request, "listadoEstudiantesTres.html", informacion_template)
