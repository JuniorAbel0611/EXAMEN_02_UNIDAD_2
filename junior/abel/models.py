from django.db import models

class Rol(models.Model):

    descripcion = models.CharField(max_length=100)

    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion


class Usuario(models.Model):

    nombre = models.CharField(max_length=100)

    email = models.EmailField()

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE
    )

    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Ajuste(models.Model):

    nombre_aplicacion = models.CharField(max_length=100)

    estado_sitio = models.BooleanField(default=True)

    paginacion = models.IntegerField()

    logs_mantenimiento = models.TextField(blank=True, default='')

    def __str__(self):
        return self.nombre_aplicacion