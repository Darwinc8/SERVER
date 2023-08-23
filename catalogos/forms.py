from django import forms

class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': '     Buscar registros...'}))

class BusquedaMunicipiosForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MUNICIPIO__icontains', 'Nombre de Municipio'),
        ('ID_MUNICIPIO__icontains', 'ID del Municipio'),
        ('ID_ENTIDAD_id__ENTIDAD__icontains', 'Entidad')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='MUNICIPIO__icontains'
        )
    
class BusquedaLOCsForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('NO_LICENCIA__icontains', 'Número de Licencia'),
        ('DEPENDENCIA__icontains', 'Dependencia'),
        ('ENTIDAD__icontains', 'Entidad')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='NO_LICENCIA__icontains'
        )
    
class BusquedaInstitucionesForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('NOMBRE__icontains', 'Instituciones'),
        ('ID_INSTITUCION__icontains', 'ID'),
        ('ID_DEPENDENCIA_id__DEPENDENCIA__icontains', 'Dependencias')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='NOMBRE__icontains'
        )
    
class BusquedaTiposForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('TIPO__icontains', 'Tipo de arma'),
        ('ID_TIPO__icontains', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='TIPO__icontains'
        )

class BusquedaCalibreForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('CALIBRE__icontains', 'Calibre'),
        ('ID_CALIBRE__icontains', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='CALIBRE__icontains'
        )

class BusquedaMarcasForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MARCA__icontains', 'Marcas'),
        ('ID_MARCA__icontains', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='MARCA__icontains'
        )

class BusquedaModelosForm(BusquedaForm):
    CAMPOS_BUSQUEDA = (
        ('MODELO__icontains', 'Modelos'),
        ('ID_MODELO__icontains', 'ID')
    )
    
    OPCIONES_ORDENADAS = sorted(CAMPOS_BUSQUEDA, key=lambda option: option[1])
    
    campos_filtrados = forms.ChoiceField(
        choices=OPCIONES_ORDENADAS,
        label="Filtrar por",
        initial='MODELO__icontains'
        )