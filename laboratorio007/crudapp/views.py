# crudapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Registro
from .forms import RegistroForm

# Vista para la lista de registros
class RegistroListView(View):
    def get(self, request):
        items = Registro.objects.all()  # Obtener todos los registros
        return render(request, 'crudapp/index.html', {'items': items})

# Vista para crear un nuevo item
def crear_item(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm()
    return render(request, 'crudapp/crear_item.html', {'form': form})

# Vista para editar un item existente
def editar_item(request, pk):
    item = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroForm(instance=item)
    
    return render(request, 'crudapp/editar_item.html', {'form': form, 'item': item})

# Vista para eliminar un item existente
def eliminar_item(request, pk):
    item = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_registros')
    
    return render(request, 'crudapp/eliminar_item.html', {'item': item})
