from django import forms
from .models import  Institucion, Entidad, Dependencia, Tipo_Imagen, Armamento, Imagenes
from django.utils.translation import gettext_lazy as _

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = [
            'ID_ARMA',
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
        
    ID_ARMA = forms.ModelChoiceField(queryset=Armamento.objects.all(),to_field_name='MATRICULA',label='Matricula')
    
    INSTITUCION = forms.ModelChoiceField(queryset=Institucion.objects.all(),to_field_name='ID_INSTITUCION',label='Institucion')
    
    ENTIDAD = forms.ModelChoiceField(queryset=Entidad.objects.all(),to_field_name='ID_ENTIDAD',label='Entidad')
    
    DEPENDENCIA = forms.ModelChoiceField(queryset=Dependencia.objects.all().order_by('DEPENDENCIA'),to_field_name='ID_DEPENDENCIA',label='Dependencia')
    
    TIPO = forms.ModelChoiceField(queryset=Tipo_Imagen.objects.all().order_by('DESCRIPCION'),to_field_name='ID_IMAGEN',label='Tipo de Imagen')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ID_ARMA'].widget.attrs.update({'class': 'form-control'})
        self.fields['INSTITUCION'].widget.attrs.update({'class': 'form-control'})
        self.fields['ENTIDAD'].widget.attrs.update({'class': 'form-control'})
        self.fields['DEPENDENCIA'].widget.attrs.update({'class': 'form-control'})
        self.fields['TIPO'].widget.attrs.update({'class': 'form-control'})
        self.fields['IMAGEN'].widget.attrs.update({'class': 'form-control'})

class BusquedaImagenesForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('Buscar registros...')})
    )
    
    CAMPOS_BUSQUEDA = (
        ('ID_ARMA__ID_ARMA__icontains', _('ID')),
        ('INSTITUCION_id__NOMBRE__icontains', _('Institucion')),
        ('ENTIDAD_id__ENTIDAD__icontains', _('Entidad')),
        ('DEPENDENCIA_id__DEPENDENCIA__icontains', _('Dependencia')),
        ('TIPO_id__DESCRIPCION__icontains', _('Tipos de Imagen'))
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='ID_ARMA__ID_ARMA__icontains'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})
        self.fields['query'].widget.attrs.update({'class': 'form-control input-placeholder', 'style': 'width: 100%; max-width: 300px;'})    

            