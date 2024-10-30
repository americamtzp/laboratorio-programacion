from django.urls import path
from . import views

urlpatterns = [
    path('', views.league_list, name='league_list'),
    path('create/', views.league_create, name='league_create'),
    path('update/<int:pk>/', views.league_update, name='league_update'),
    path('delete/<int:pk>/', views.league_delete, name='league_delete'),
]
