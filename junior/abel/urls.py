from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD de Roles
    path('roles/', views.roles_list, name='roles'),
    path('roles/nuevo/', views.rol_create, name='rol_create'),
    path('roles/editar/<int:pk>/', views.rol_edit, name='rol_edit'),
    path('roles/eliminar/<int:pk>/', views.rol_delete, name='rol_delete'),

    # CRUD de Usuarios
    path('usuarios/', views.usuarios_list, name='usuarios'),
    path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),
    path('usuarios/editar/<int:pk>/', views.usuario_edit, name='usuario_edit'),
    path('usuarios/eliminar/<int:pk>/', views.usuario_delete, name='usuario_delete'),

    # CRUD de Ajustes
    path('ajustes/', views.ajustes_list, name='ajustes'),
    path('ajustes/nuevo/', views.ajuste_create, name='ajuste_create'),
    path('ajustes/editar/<int:pk>/', views.ajuste_edit, name='ajuste_edit'),
    path('ajustes/eliminar/<int:pk>/', views.ajuste_delete, name='ajuste_delete'),
]