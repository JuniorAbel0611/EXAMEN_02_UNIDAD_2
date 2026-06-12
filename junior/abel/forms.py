from django import forms
from .models import Rol, Usuario, Ajuste

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej. Administrador, Operador, etc.',
                'required': 'required'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'rolEstado'
            }),
        }
        labels = {
            'descripcion': 'Descripción del Rol',
            'estado': 'Estado Activo',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'rol', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre completo del usuario',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'ejemplo@correo.com',
                'required': 'required'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'estado': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'usuarioEstado'
            }),
        }
        labels = {
            'nombre': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'rol': 'Rol Asignado',
            'estado': 'Estado Activo',
        }

class AjusteForm(forms.ModelForm):
    class Meta:
        model = Ajuste
        fields = ['nombre_aplicacion', 'estado_sitio', 'paginacion', 'logs_mantenimiento']
        widgets = {
            'nombre_aplicacion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre del sistema / empresa',
                'required': 'required'
            }),
            'estado_sitio': forms.CheckboxInput(attrs={
                'class': 'form-check-input', 
                'id': 'estadoSitio'
            }),
            'paginacion': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': '1', 
                'max': '100',
                'required': 'required'
            }),
            'logs_mantenimiento': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': '4', 
                'placeholder': 'Escribe aquí los logs de mantenimiento...'
            }),
        }
        labels = {
            'nombre_aplicacion': 'Nombre de la Aplicación',
            'estado_sitio': 'Estado del Sitio (En línea / Mantenimiento)',
            'paginacion': 'Paginación por Defecto',
            'logs_mantenimiento': 'Logs de Mantenimiento',
        }
