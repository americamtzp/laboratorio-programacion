# crudapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item

# Leer: Mostrar todos los items
def index(request):
    items = Item.objects.all()  # Trae todos los items
    return render(request, 'crudapp/index.html', {'items': items})

# Crear: Agregar un nuevo item
def crear_item(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        item = Item(nombre=nombre, descripcion=descripcion)
        item.save()
        return redirect('index')
    return render(request, 'crudapp/crear_item.html')

# Actualizar: Editar un item existente
def editar_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.nombre = request.POST['nombre']
        item.descripcion = request.POST['descripcion']
        item.save()
        return redirect('index')
    return render(request, 'crudapp/editar_item.html', {'item': item})

# Eliminar: Borrar un item existente
def eliminar_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'crudapp/eliminar_item.html', {'item': item})
