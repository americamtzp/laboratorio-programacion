from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Categoria, Producto, Proveedor


# List Views
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'crudapp/categoria_list.html'
    context_object_name = 'categorias'  # Añade un nombre para el contexto

class ProductoListView(ListView):
    model = Producto
    template_name = 'crudapp/producto_list.html'
    context_object_name = 'productos'

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'crudapp/proveedor_list.html'
    context_object_name = 'proveedores'  # Añade un nombre para el contexto

# CRUD Functions for Categoria
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('categoria_list')
    return render(request, 'crudapp/crear_categoria.html')

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.descripcion = request.POST['descripcion']
        categoria.save()
        return redirect('categoria_list')
    return render(request, 'crudapp/editar_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'crudapp/eliminar_categoria.html', {'categoria': categoria})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria_id = request.POST['categoria']
        proveedor_id = request.POST['proveedor']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']
        
        # Obtener objetos relacionados
        categoria = Categoria.objects.get(id=categoria_id)
        proveedor = Proveedor.objects.get(id=proveedor_id)

        # Crear y guardar el nuevo producto
        Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            proveedor=proveedor,
            precio=precio,
            cantidad=cantidad
        )
        
        return redirect('producto_list')
    
    # Obtener categorías y proveedores para el formulario
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, 'crudapp/crear_producto.html', {
        'categorias': categorias,
        'proveedores': proveedores
    })
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.categoria_id = request.POST.get('categoria')
        producto.proveedor_id = request.POST.get('proveedor')
        producto.precio = request.POST.get('precio')
        producto.cantidad = request.POST.get('cantidad')
        producto.save()
        return redirect('producto_list')

    return render(request, 'crudapp/editar_producto.html', {
        'producto': producto,
        'categorias': categorias,
        'proveedores': proveedores
    })

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'crudapp/eliminar_producto.html', {'producto': producto})

# CRUD Functions for Proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        Proveedor.objects.create(nombre=nombre, direccion=direccion)
        return redirect('proveedor_list')
    return render(request, 'crudapp/crear_proveedor.html')

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)

    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.save()
        return redirect('proveedor_list')

    return render(request, 'crudapp/editar_proveedor.html', {'proveedor': proveedor})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request, 'crudapp/eliminar_proveedor.html', {'proveedor': proveedor})
