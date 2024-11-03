from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile_edit/<int:user_id>/', views.profile_edit, name='profile_edit'),
    path('profile_delete/<int:user_id>/', views.profile_delete, name='profile_delete'),
]
