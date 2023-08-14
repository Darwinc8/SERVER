from django import forms
from django.forms import DateInput
from .models import Armamento, Institucion, Dependencia, Entidad, Municipio, LOC, Tipo, Calibre, Marca, Modelo, Edo_conservacion

class ArmamentoForm(forms.ModelForm):
    class Meta:
        model = Armamento
        exclude = ['ID_ALTERNA'] #Se omite este campo porque es la pk y es autoincrementable
            
    
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
    
    FECHA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    
    FECHA_LOC = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_CAPTURA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_BAJA_LOGICA = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
        
    FECHA_BAJA_DOCUMENTO = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)

class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': '     Buscar registros...'}))


