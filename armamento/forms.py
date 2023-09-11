from django import forms
from django.forms import DateInput
from .models import Armamento, Institucion, Dependencia, Entidad, Municipio, LOC, Tipo, Calibre, Marca, Modelo, Edo_conservacion
from portadores.models import Portador

class ArmamentoForm(forms.ModelForm):
    class Meta:
        model = Armamento
        exclude = ['ID_ALTERNA', 'ultima_modificacion']       
        
    INSTITUCION = forms.ModelChoiceField(queryset=Institucion.objects.all().order_by('NOMBRE'),to_field_name='ID_INSTITUCION',label='Institucion')
    
    DEPENDENCIA = forms.ModelChoiceField(queryset=Dependencia.objects.all().order_by('DEPENDENCIA'),to_field_name='ID_DEPENDENCIA',label='DEPENDENCIA')
    
    ENTIDAD = forms.ModelChoiceField(queryset=Entidad.objects.all(),to_field_name='ID_ENTIDAD',label='ENTIDAD')
    
    MUNICIPIO = forms.ModelChoiceField(queryset=Municipio.objects.all().order_by('MUNICIPIO'), label="MUNICIPIO", to_field_name='id')
    
    NUMERO_LOC = forms.ModelChoiceField(queryset=LOC.objects.all(),to_field_name='id',label='NO_LICENCIA')
    
    CLASE_TIPO_ARMA = forms.ModelChoiceField(queryset=Tipo.objects.all(),to_field_name='ID_TIPO',label='CLASE_TIPO_ARMA')
    
    CALIBRE_ARMA = forms.ModelChoiceField(queryset=Calibre.objects.all(),to_field_name='ID_CALIBRE',label='CALIBRE_ARMA')
    
    MARCA_ARMA = forms.ModelChoiceField(queryset=Marca.objects.all(),to_field_name='ID_MARCA',label='MARCA_ARMA')
    
    MODELO_ARMA = forms.ModelChoiceField(queryset=Modelo.objects.all(),to_field_name='ID_MODELO',label='MODELO_ARMA')
    
    ESTADO_ARMA = forms.ModelChoiceField(queryset=Edo_conservacion.objects.all(),to_field_name='ID_ESTADO',label='ESTADO_ARMA')
    
    CUIP_PORTADOR = forms.ModelChoiceField(queryset=Portador.objects.all(),to_field_name='CUIP',label='PORTADORES')
    
    CUIP_RESPONSABLE = forms.ModelChoiceField(queryset=Portador.objects.all(),to_field_name='CUIP',label='PORTADORES')
     
    FECHA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    
    FECHA_LOC = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_CAPTURA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_BAJA_LOGICA = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
        
    FECHA_BAJA_DOCUMENTO = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        CUIP_PORTADOR = cleaned_data.get('CUIP_PORTADOR')
        CUIP_RESPONSABLE = cleaned_data.get('CUIP_RESPONSABLE')

        if CUIP_PORTADOR == CUIP_RESPONSABLE:
            raise forms.ValidationError("Los campos no pueden tener el mismo registro seleccionado.")

        return cleaned_data

class BusquedaArmamentoForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': '     Buscar registros...'}))
    
    CAMPOS_BUSQUEDA = (
        ('ID_ARMA', 'ID'),
        ('INSTITUCION_id__NOMBRE__icontains', 'Institución'),
        ('DEPENDENCIA_id__DEPENDENCIA__icontains', 'Dependencia'),
        ('ENTIDAD_id__ENTIDAD__icontains', 'Entidad'),
        ('MUNICIPIO_id__MUNICIPIO__icontains', 'Municipio'),
        ('NUMERO_LOC_id__NO_LICENCIA__icontains', 'LOC'),
        ('CLASE_TIPO_ARMA_id__TIPO__icontains', 'Tipo de arma'),
        ('CALIBRE_ARMA_id__CALIBRE__icontains', 'Calibres'),
        ('MARCA_id__MARCA__icontains', 'Marcas'),
        ('MODELO_id__MODELO__icontains', 'Modelos')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='ID_ARMA'
        )


