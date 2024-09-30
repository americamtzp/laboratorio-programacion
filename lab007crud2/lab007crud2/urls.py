from django.contrib import admin
from django.urls import path, include
from crudapp import views  # Importa las vistas necesarias si aún no lo has hecho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ProductoListView.as_view(), name='producto_list'),  # Define la vista principal
    path('categorias/', include('crudapp.urls')),  # Puedes seguir incluyendo el resto de las rutas de la app
]
