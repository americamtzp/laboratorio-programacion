# crudapp/urls.py

from django.urls import path
from .views import (
    CategoriaListView, crear_categoria, editar_categoria, eliminar_categoria,
    ProductoListView, crear_producto, editar_producto, eliminar_producto,
    ProveedorListView, crear_proveedor, editar_proveedor, eliminar_proveedor
)
from .import views

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/crear/', crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),
    
    path('producto/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    
    path('proveedores/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/crear/', crear_proveedor, name='crear_proveedor'),
   path('proveedores/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),
]
