from datetime import datetime

from django.db import models


# Create your models here.

class Solicitante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de solicitante")
    cedula = models.CharField(max_length=10, verbose_name="Numero de cedula")
    telefono = models.CharField(max_length=10, verbose_name="Numero de telefono")
    email = models.EmailField(verbose_name="Correo electronico")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Solicitante"
        verbose_name_plural = "Solicitantes"
        db_table = "solicitante"
        ordering = ["id"]

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de categoria")
    descripcion = models.CharField(max_length=500, verbose_name="Descripcion")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"
        ordering = ["id"]

class Solicitud(models.Model):
    categoria_id = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    solicitante_id = models.ForeignKey(Solicitante, on_delete=models.PROTECT)
    fecha_registro = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
        db_table = "solicitud"
        ordering = ["id"]


class Sustancia(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de sustancia")
    fecha_creacion = models.DateTimeField(default=datetime.now)
    url_documentacion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Sustancia"
        verbose_name_plural = "Sustancias"
        db_table = "sustancia"
        ordering = ["id"]

class Inventario(models.Model):
    sustancia_id = models.ForeignKey(Sustancia, on_delete=models.PROTECT)

    def __str__(self):
        return self.sustancia_id

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventariados"
        db_table = "inventario"
        ordering = ["id"]
