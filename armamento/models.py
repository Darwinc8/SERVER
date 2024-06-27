from django.db import models
from catalogos.models import Institucion, Dependencia, Calibre, Edo_conservacion, Entidad, Estatus_Arma, LOC, Marca, Modelo, Municipio, Tipo, TipoFuncinamiento, Propiedad
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re
import unicodedata
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_fecha_no_anterior_1990(value):
    if value < datetime(1990, 1, 1).date():
        raise ValidationError(_('La fecha no puede ser anterior al 01 de enero de 1990'))

def validate_FechaRegistro_FechaLOC(fecha_registro, fecha_loc):
    if fecha_registro < fecha_loc:
        raise ValidationError(_('La fecha de registro no puede ser menor a la Fecha de Alta del LOC'))

def validate_FechaCaptura_FechaLOC(fecha_captura, fecha_loc):
    if fecha_captura < fecha_loc:
        raise ValidationError(_('La fecha de Captura no puede ser menor a la Fecha de Alta del LOC'))    

def validate_FechaCaptura_FechaRegistro(fecha_captura, fecha_registro):
    if fecha_captura < fecha_registro:
        raise ValidationError(_('La fecha de Captura no puede ser menor a la Fecha de Registro'))

def validate_cuip_formato(value):
    if not (14 <= len(value) <= 20):
        raise ValidationError(_('El CUIP debe tener entre 14 y 20 caracteres'))

    if not value[0:4].isalpha():
        raise ValidationError(_('Los primeros 4 caracteres del CUIP deben ser letras'))

    if not value[4:10].isdigit():
        raise ValidationError(_('Los caracteres del 5 al 10 del CUIP deben ser todos dígitos'))

    if value[10] not in ['H', 'M']:
        raise ValidationError(_('El carácter en la posición 11 del CUIP debe ser H o M'))

    if not (value[11:13].isdigit() and value[11:13] in [str(i).zfill(2) for i in range(1, 33)] + ['98', '99']):
        raise ValidationError(_('Los caracteres del 12 al 13 del CUIP deben estar entre 01 y 32 o ser 98 o 99'))

    if not value[13:].isdigit():
        raise ValidationError(_('Los caracteres a partir del 14 del CUIP deben ser todos dígitos'))

def validate_AZ_09_Ñ(campo, permitir_ñ=True):
    """
    Función para validar un campo según los siguientes criterios:
    - Solo letras mayúsculas de A-Z
    - Números del 0-9
    - Opcionalmente, la letra 'Ñ' si se especifica permitir_ñ=True
    - Espacio en blanco
    """
    regex = r'^[A-Z0-9'
    if permitir_ñ:
        regex += 'Ñ'
    regex += r' ]+$'
    
    if not re.match(regex, campo):
        if permitir_ñ:
            raise ValidationError(
                'El campo solo puede contener letras mayúsculas de A-Z, la letra Ñ, números de 0-9.'
            )
        else:
            raise ValidationError(
                'El campo solo puede contener letras mayúsculas de A-Z, números de 0-9.'
            )        

def validate_especiales(campo):
    """
    Función para validar un campo que incluya letras mayúsculas de A-Z, Ñ,
    números de 0-9, y los caracteres especiales . / _ -, y espacio en blanco.
    """
    regex = r'^[A-Z0-9Ñ./_\- ]+$'
    
    if not re.match(regex, campo):
        raise ValidationError(
            _('El campo solo puede contener letras mayúsculas de A-Z, Ñ, números de 0-9, '
              'y los caracteres especiales . / _ - y espacio en blanco')
        )

def validate_09(campo):
    """
    Función para validar que un campo contenga solo números del 0 al 9.
    """
    regex = r'^[0-9]+$'
    
    if not re.match(regex, campo):
        raise ValidationError(
            'El campo solo puede contener números del 0 al 9'
        )

def validar_sin_acentos(texto):
    texto = str(texto)
    # Normalizar el texto en forma NFD (Descomposición Canónica)
    texto_normalizado = unicodedata.normalize('NFD', texto)
    
    # Comprobar si hay caracteres diacríticos (acentos) en el texto
    for char in texto_normalizado:
        if unicodedata.category(char) == 'Mn':
            raise ValidationError(_('El campo no puede contener caracteres con acentos'))

def convertir_a_mayusculas(texto):
    """
    Validator que convierte el valor a mayúsculas.
    """
    if texto is not None:
        return texto.upper()
    return texto

def save(self, *args, **kwargs):
        self.clean()
        super(Armamento, self).save(*args, **kwargs)
    
class Armamento(models.Model):
    ID_ALTERNA= models.AutoField(primary_key=True)
    ID_ARMA = models.DecimalField(max_digits=10, decimal_places=0, unique=False, null=True, blank=True)
    INSTITUCION = models.ForeignKey(Institucion, on_delete=models.RESTRICT, null=False, blank=False)
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT, null=False, blank=False)
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT, null=False, blank=False)
    MUNICIPIO = models.ForeignKey(Municipio,on_delete=models.RESTRICT,to_field='id', null=False, blank=False)
    NUMERO_LOC = models.ForeignKey(LOC, on_delete=models.RESTRICT, null=False, blank=False)
    FOLIO_C = models.CharField(max_length=20, null=False, blank=False, validators=[validate_AZ_09_Ñ])
    FOLIO_D = models.CharField(max_length=20, null=False, blank=False, validators=[validate_AZ_09_Ñ])
    CLASE_TIPO_ARMA = models.ForeignKey(Tipo, on_delete=models.RESTRICT, null=False, blank=False)
    CALIBRE_ARMA = models.ForeignKey(Calibre, on_delete=models.RESTRICT, null=False, blank=False)
    MARCA_ARMA = models.ForeignKey(Marca, on_delete=models.RESTRICT, null=False, blank=False)
    MODELO_ARMA = models.ForeignKey(Modelo, on_delete=models.RESTRICT, null=False, blank=False)
    MATRICULA_CANON = models.CharField(max_length=40, null=True, blank=True, validators=[validate_AZ_09_Ñ])
    MATRICULA = models.CharField(max_length=20, null=False, blank=False, unique=True, validators=[validate_AZ_09_Ñ, validar_sin_acentos])
    MATRICULA_CANON = models.CharField(max_length=40, null=True, blank=True, validators=[validate_AZ_09_Ñ])
    FECHA = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    FECHA_LOC = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    ESTADO_ARMA = models.ForeignKey(Edo_conservacion, on_delete=models.RESTRICT, null=False, blank=False)
    FECHA_CAPTURA = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    OBSERVACIONES = models.TextField(null=False, blank=False, validators=[validate_especiales])
    ESTATUS_ARMA = models.ForeignKey(Estatus_Arma, on_delete=models.RESTRICT, null=False, blank=False)
    CUIP_PORTADOR = models.TextField(null=False, validators=[validate_cuip_formato])
    CUIP_RESPONSABLE = models.TextField(null=False, validators=[validate_cuip_formato])
    CIHB = models.CharField(max_length=20, null=True, blank=True, validators=[validate_09])
    TIPO_FUNCIONAMIENTO = models.ForeignKey(TipoFuncinamiento, on_delete=models.RESTRICT, null=False, default=4)
    PROPIEDAD = models.ForeignKey(Propiedad, on_delete=models.RESTRICT, null=False, default=4)
    FECHA_BAJA_LOGICA = models.DateField(null=True, blank=True, validators=[validate_fecha_no_anterior_1990])
    MOTIVO_BAJA = models.TextField(null=True, blank=True)
    DOCUMENTO_BAJA = models.CharField(max_length=20, null=True, blank=True)
    OBSERVACIONES_BAJA = models.TextField(null=True, blank=True,)
    FECHA_BAJA_DOCUMENTO = models.DateField(null=True, blank=True, validators=[validate_fecha_no_anterior_1990])
    
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=True)
    
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def clean(self):
        # Llama al método clean() de la superclase para aplicar validaciones adicionales
        super().clean()
        self.FOLIO_C = convertir_a_mayusculas(self.FOLIO_C)
        self.FOLIO_D = convertir_a_mayusculas(self.FOLIO_D)
        self.MATRICULA = convertir_a_mayusculas(self.MATRICULA)
        self.MATRICULA_CANON = convertir_a_mayusculas(self.MATRICULA_CANON)
        self.OBSERVACIONES = convertir_a_mayusculas(self.OBSERVACIONES)
        self.CUIP_PORTADOR = convertir_a_mayusculas(self.CUIP_PORTADOR)
        self.CUIP_RESPONSABLE = convertir_a_mayusculas(self.CUIP_RESPONSABLE)
        self.OBSERVACIONES_BAJA = convertir_a_mayusculas(self.OBSERVACIONES_BAJA)
        validate_FechaRegistro_FechaLOC(self.FECHA, self.FECHA_LOC)
        validate_FechaCaptura_FechaLOC(self.FECHA_CAPTURA, self.FECHA_LOC)
        validate_FechaCaptura_FechaRegistro(self.FECHA_CAPTURA, self.FECHA)

    def __str__(self):
        return f"{self.MATRICULA}"

class ArmamentoLog(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    id_alterna= models.DecimalField(max_digits=10, decimal_places=0)
    id_arma = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    institucion = models.CharField(max_length=70, null=False)
    dependencia = models.CharField(max_length=70, null=False)
    entidad = models.CharField(max_length=70, null=False)  
    municipio = models.CharField(max_length=70, null=False)
    numero_loc = models.CharField(max_length=20, null=False)
    folio_c = models.CharField(max_length=20, null=False)
    folio_d = models.CharField(max_length=20, null=False)
    clase_tipo_arma = models.CharField(max_length=50, null=False)
    calibre_arma = models.CharField(max_length=50, null=False)
    marca_arma = models.CharField(max_length=50, null=False)
    modelo_arma = models.CharField(max_length=50, null=False)
    matricula = models.CharField(max_length=20, null=False)
    matricula_canon = models.CharField(max_length=40, null=True)
    fecha = models.DateField(null=False)
    fecha_loc = models.DateField(null=False, blank=False)
    estado_arma = models.CharField(max_length=20, null=True)
    fecha_captura = models.DateField(null=False)
    observaciones = models.TextField(null=False)
    estatus_arma = models.CharField(max_length=30, null=False)
    cuip_portador = models.CharField(max_length=20, null=False)
    cuip_responsable = models.CharField(max_length=20, null=False) 
    tipo_funcionamiento = models.CharField(max_length=20, null=False, default="OTRO")
    propiedad = models.CharField(max_length=20, null=False, default="OTRO")
    cihb = models.CharField(max_length=20, null=True, blank=True)
    fecha_baja_logica = models.DateField(null=True, blank=True)
    motivo_baja = models.TextField(null=True, blank=True)
    documento_baja = models.CharField(max_length=20, null=True, blank=True)
    observaciones_baja = models.TextField(null=True, blank=True)
    fecha_baja_documento = models.DateField(null=True, blank=True)
    
    usuario = models.CharField(max_length=50)
    
    ultima_modificacion = models.DateTimeField()

    def __str__(self):
        return f"{self.id}-{self.estado}-{self.matricula}"