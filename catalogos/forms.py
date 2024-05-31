from django import forms
from django.utils.translation import gettext_lazy as _

class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': _('Buscar registros...')}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({'class': 'form-control input-placeholder', 'style': 'width: 100%; max-width: 300px;'})

class BusquedaMunicipiosForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MUNICIPIO__icontains', _('Municipios')),
        ('ID_MUNICIPIO', _('ID del Municipio')),
        ('ID_ENTIDAD_id__ENTIDAD__icontains', _('Entidad'))
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='MUNICIPIO__icontains'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
        })

class BusquedaLOCsForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('NO_LICENCIA', _('Número de Licencia')),
        ('DEPENDENCIA__icontains', _('Dependencia')),
        ('ENTIDAD__icontains', _('Entidad'))
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='NO_LICENCIA'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})
    
class BusquedaInstitucionesForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('NOMBRE__icontains', _('Nombre')),
        ('ID_INSTITUCION', 'ID'),
        ('ID_DEPENDENCIA_id__DEPENDENCIA__icontains', _('Dependencias'))
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='NOMBRE__icontains'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})

class BusquedaTiposForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('TIPO__icontains', _('Tipo')),
        ('ID_TIPO', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='TIPO__icontains'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})

class BusquedaCalibreForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('CALIBRE__icontains', _('Calibre')),
        ('ID_CALIBRE', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='CALIBRE__icontains'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})

class BusquedaMarcasForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MARCA__icontains', _('Marcas')),
        ('ID_MARCA', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='MARCA__icontains'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})

class BusquedaModelosForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MODELO__icontains', _('Modelos')),
        ('ID_MODELO', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label=_("Filtrar por"),
        initial='MODELO__icontains'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campos_filtrados'].widget.attrs.update({
            'class': 'form-select',
            'style': 'width: 100%; max-width: 300px; font-weight: bold;'
})