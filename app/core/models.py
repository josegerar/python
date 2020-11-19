from django.db import models
from datetime import datetime

# Create your models here.




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
