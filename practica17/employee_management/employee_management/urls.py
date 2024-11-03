# employee_management/urls.py

from django.contrib import admin
from django.urls import path
from employees import views as employee_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee_views.home, name='home'),
    path('register/', employee_views.register, name='register'),
    path('login/', employee_views.login_view, name='login'),
    path('logout/', employee_views.logout_view, name='logout'),
    path('profile/', employee_views.profile, name='profile'),
]
