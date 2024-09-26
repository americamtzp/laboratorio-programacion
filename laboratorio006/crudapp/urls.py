# crudapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Leer
    path('crear/', views.crear_item, name='crear_item'),  # Crear
    path('editar/<int:id>/', views.editar_item, name='editar_item'),  # Actualizar
    path('eliminar/<int:id>/', views.eliminar_item, name='eliminar_item'),  # Eliminar
]
