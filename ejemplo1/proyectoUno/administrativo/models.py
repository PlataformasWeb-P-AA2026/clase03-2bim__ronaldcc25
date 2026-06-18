from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%d) %s %s %s" % (self.id, self.nombre, self.apellido, self.cedula)

    def obtenerCantidadNumeros(self):
        return len(self.mis_numeros_telefonicos.all())


class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name="mis_numeros_telefonicos"
    )

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
