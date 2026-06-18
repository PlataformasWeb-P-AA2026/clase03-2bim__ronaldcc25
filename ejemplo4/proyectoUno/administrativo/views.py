from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext

# importar los formularios de forms.py
from administrativo.forms import *

# importar las clases de models.py
from administrativo.models import *

# Create your views here.

"""
agregar el metodo de pais creado
"""


def index(request):
    """
    Listar los registros de Estudiante
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    paises = Pais.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {
        "estudiantes": estudiantes,
        "numero_estudiantes": len(estudiantes),
        "paises": paises,
    }
    return render(request, "index.html", informacion_template)


def obtener_estudiante(request, id):
    """
    Listar los registros del modelo Estudiante,
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiante = Estudiante.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {"estudiante": estudiante}
    return render(request, "obtener_estudiante.html", informacion_template)


def crear_estudiante(request):
    """ """
    print(request)
    if request.method == "POST":
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearEstudiante.html", diccionario)


def editar_estudiante(request, id):
    """ """
    print("---------------")
    print(request)
    print("---------------")
    estudiante = Estudiante.objects.get(pk=id)
    # Deber: consultar
    if request.method == "POST":
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {"formulario": formulario}

    return render(request, "editarEstudiante.html", diccionario)


def eliminar_estudiante(request, id):
    """ """
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)


def obtener_pais(request, id):
    pais = Pais.objects.get(pk=id)
    informacion_template = {"pais": pais}
    return render(request, "obtener_pais.html", informacion_template)


def crear_pais(request):
    """ """
    print(request)
    if request.method == "POST":
        formulario = PaisForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PaisForm()
    diccionario = {"formulario": formulario}

    return render(request, "crear_pais.html", diccionario)
