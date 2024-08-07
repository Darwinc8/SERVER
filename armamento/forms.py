from django import forms
from django.forms import DateInput
from .models import Armamento, ArmamentoLog, Institucion, Dependencia, Entidad, Municipio, LOC, Tipo, Calibre, Marca, Modelo, Edo_conservacion, TipoFuncinamiento, Propiedad
from django.utils.translation import gettext_lazy as _

class ArmamentoForm(forms.ModelForm):
    
    class Meta:
        model = Armamento
        exclude = ['ID_ALTERNA', 'ultima_modificacion', 'usuario']
                   
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
    
    TIPO_FUNCIONAMIENTO = forms.ModelChoiceField(queryset=TipoFuncinamiento.objects.all(),to_field_name='ID',label='TIPO_FUNCIONAMIENTO')
    
    PROPIEDAD = forms.ModelChoiceField(queryset=Propiedad.objects.all(),to_field_name='ID',label='PROPIEDAD')
    
    FECHA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    
    FECHA_LOC = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_CAPTURA = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
        
    FECHA_BAJA_LOGICA = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)
        
    FECHA_BAJA_DOCUMENTO = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)

    def __init__(self, *args, **kwargs):
        super(ArmamentoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'rows': 1,'class': 'form-control'})

class BusquedaArmamentoForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('Buscar registros...')})
    )
    
    CAMPOS_BUSQUEDA = (
        ('ID_ARMA', _('ID')),
        ('MATRICULA__icontains', _('Matricula')),
        ('INSTITUCION_id__NOMBRE__icontains', _('Institución')),
        ('DEPENDENCIA_id__DEPENDENCIA__icontains', _('Dependencia')),
        ('ENTIDAD_id__ENTIDAD__icontains', _('Entidad')),
        ('MUNICIPIO_id__MUNICIPIO__icontains', _('Municipio')),
        ('CLASE_TIPO_ARMA_id__TIPO__icontains', _('Clase')),
        ('CALIBRE_ARMA_id__CALIBRE__icontains', _('Calibres')),
        ('MARCA_ARMA__MARCA__icontains', _('Marcas')),
        ('CUIP_PORTADOR__icontains', _('CUIP Portador')),
        ('CUIP_RESPONSABLE__icontains', _('CUIP Responsable')),
        ('MODELO_ARMA__MODELO__icontains', _('Modelos'))
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='MATRICULA__icontains'
    )
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})
        self.fields['query'].widget.attrs.update({'class': 'form-control input-placeholder', 'style': 'width: 100%; max-width: 300px;'})

class ArmamentoLogForm(forms.ModelForm):
    class Meta:
        model = ArmamentoLog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ArmamentoLogForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'rows': 1, 'class': 'form-control'})

class ExcelUploadForm(forms.Form):
    archivo_excel = forms.FileField(
        label=_('Seleccione un archivo Excel'),
        required=True,
        widget=forms.FileInput(attrs={'accept': '.xlsx'})
    )

class BajaArmamentoForm(forms.ModelForm):
    class Meta:
        model = Armamento
        fields = ['MATRICULA','MOTIVO_BAJA', 'OBSERVACIONES_BAJA', 'DOCUMENTO_BAJA', 'FECHA_BAJA_LOGICA', 'FECHA_BAJA_DOCUMENTO']
        widgets = {
            'FECHA_BAJA_LOGICA': forms.DateInput(attrs={'type': 'date'}),
            'FECHA_BAJA_DOCUMENTO': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['MATRICULA'].widget = forms.Textarea(attrs={'rows': 1, 'class': 'form-control','required': True})
        self.fields['MOTIVO_BAJA'].widget = forms.Textarea(attrs={'rows': 1, 'class': 'form-control','required': True})
        self.fields['OBSERVACIONES_BAJA'].widget = forms.Textarea(attrs={'rows': 1, 'class': 'form-control','required': True})
        self.fields['DOCUMENTO_BAJA'].widget.attrs.update({'class': 'form-control', 'required': True})
        self.fields['FECHA_BAJA_LOGICA'].widget.attrs.update({'class': 'form-control', 'required': True})
        self.fields['FECHA_BAJA_DOCUMENTO'].widget.attrs.update({'class': 'form-control', 'required': True})