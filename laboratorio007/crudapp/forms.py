# crudapp/forms.py
from django import forms
from .models import Registro  # Modelo del cual vas a crear el formulario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'descripcion']  # Asegúrate de que coincidan con los campos del modelo
