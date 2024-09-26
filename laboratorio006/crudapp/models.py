# crudapp/models.py
from django.db import models

# Definimos el modelo para un "Item"
class Item(models.Model):
    nombre = models.CharField(max_length=100)  # Campo para el nombre del item
    descripcion = models.TextField()  # Campo para la descripción del item

    # Método para representar el objeto en texto, útil en el administrador de Django
    def __str__(self):
        return self.nombre
