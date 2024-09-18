from django.db import models

# Creación de modelo item.

class Item(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(max_length=100)
    descripcion = models.CharField(max_length=100)