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
    
       