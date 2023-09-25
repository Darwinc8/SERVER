from django.forms import ModelForm
from django import forms
from .models import Portador

class CrearPortadorForm(ModelForm):
    class Meta:
        model = Portador
        exclude = ['ultima_modificacion', 'usuario']

class EditarPortadorForm(ModelForm):
    class Meta:
        model = Portador
        exclude = ['CUIP','ultima_modificacion', 'usuario']
    
                     
class BusquedaPortadoresForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': '     Buscar registros...'}))
    
    CAMPOS_BUSQUEDA = (
        ('CUIP__icontains', 'CUIP'),
        ('NOMBRE__icontains', 'Nombre'),
        ('APELLIDO_PATERNO__icontains', 'Apellido Paterno'),
        ('APELLIDO_MATERNO__icontains', 'Apellido Materno'),
        ('CORREO__icontains', 'Correo'),
        ('TELEFONO__icontains', 'Telefono')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='CUIP__icontains'
        )