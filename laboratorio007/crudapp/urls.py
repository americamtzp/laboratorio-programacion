# crudapp/urls.py
from django.urls import path
from .views import RegistroListView, crear_item, editar_item, eliminar_item

urlpatterns = [
    path('', RegistroListView.as_view(), name='lista_registros'),  # Ruta para la lista de registros
    path('crear/', crear_item, name='crear_item'),  # Ruta para crear un nuevo registro
    path('editar/<int:pk>/', editar_item, name='editar_item'),  # Ruta para editar un item
    path('eliminar/<int:pk>/', eliminar_item, name='eliminar_item'),  # Ruta para eliminar un item
]
