# laboratorio006/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='registros/', permanent=True)),  # Redirige la página de inicio a /registros/
    path('registros/', include('crudapp.urls')),  # Incluye las URLs de la app crudapp
]
