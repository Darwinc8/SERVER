from django import forms
from .models import Imagenes, Institucion, Entidad, Dependencia, Tipo_Imagen, Armamento

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = ['ID_ARMA',
            'INSTITUCION',
            'ENTIDAD',
            'DEPENDENCIA',
            'IMAKEY',
            'DESIMA',
            'TIPO',
            'FOLIO',
            'GRUPO',
            'IMAGEN'
            ]
    
    ID_ARMA = forms.ModelChoiceField(queryset=Armamento.objects.all(),to_field_name='ID_ARMA',label='Armamento')
    
    INSTITUCION = forms.ModelChoiceField(queryset=Institucion.objects.all(),to_field_name='ID_INSTITUCION',label='Institucion')
    
    ENTIDAD = forms.ModelChoiceField(queryset=Entidad.objects.all(),to_field_name='ID_ENTIDAD',label='Entidad')
    
    DEPENDENCIA = forms.ModelChoiceField(queryset=Dependencia.objects.all().order_by('DEPENDENCIA'),to_field_name='ID_DEPENDENCIA',label='Dependencia')
    
    TIPO = forms.ModelChoiceField(queryset=Tipo_Imagen.objects.all().order_by('DESCRIPCION'),to_field_name='ID_IMAGEN',label='Tipo de Imagen')

class BusquedaImagenesForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': '     Buscar registros...'}))
    
    CAMPOS_BUSQUEDA = (
        ('ID_ARMA__icontains', 'ID'),
        ('INSTITUCION_id__NOMBRE__icontains', 'Institución'),
        ('ENTIDAD_id__ENTIDAD__icontains', 'Entidad'),
        ('DEPENDENCIA_id__DEPENDENCIA__icontains', 'Dependencia'),
        ('TIPO_id__DESCRIPCION__icontains', 'Tipo de Imagen')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='ID_ARMA__icontains'
        )    
       