from django.db import models
from catalogos.models import Institucion, Dependencia, Calibre, Edo_conservacion, Entidad, Estatus_Arma, LOC, Marca, Modelo, Municipio, Tipo, TipoFuncinamiento
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

def validate_fecha_no_anterior_1990(value):
    if value < datetime(1990, 1, 1).date():
        raise ValidationError('No puede ser anterior al 01 de enero de 1990.')

def validate_cuip_formato(value):
    if not (14 <= len(value) <= 20):
        raise ValidationError('lOS CUIPs debe tener entre 14 y 20 caracteres.')
    if not value[0:4].isalpha():
        raise ValidationError('Los primeros 4 caracteres de CUIPs deben ser letras.')

    if not value[4:10].isdigit():
        raise ValidationError('Los caracteres del 5 al 10 de los CUIPs deben ser todos dígitos.')

    if value[10] not in ['H', 'M']:
        raise ValidationError('El carácter en la posición 11 de CUIPs debe ser H o M.')

    if not (value[11:13].isdigit() and value[11:13] in [str(i).zfill(2) for i in range(1, 33)] + ['98', '99']):
        raise ValidationError('Los caracteres del 12 al 13 de CUIPs deben estar entre 01 y 32 o ser 98 o 99.')

    if not value[13:].isdigit():
        raise ValidationError('Los caracteres a partir del 14 de CUIPs deben ser todos dígitos.')
        
def save(self, *args, **kwargs):
        self.clean()
        super(Armamento, self).save(*args, **kwargs)
    
class Armamento(models.Model):
    ID_ALTERNA= models.AutoField(primary_key=True)
    ID_ARMA = models.DecimalField(max_digits=10, decimal_places=0, unique=False, null=True, blank=True)
    INSTITUCION = models.ForeignKey(Institucion, on_delete=models.RESTRICT, null=False, blank=False)
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT, null=False, blank=False)
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT, null=False, blank=False)
    
    MUNICIPIO = models.ForeignKey(
        Municipio,
        on_delete=models.RESTRICT,
        to_field='id', null=False, blank=False
    )
    
    NUMERO_LOC = models.ForeignKey(LOC, on_delete=models.RESTRICT, null=False, blank=False)
    FOLIO_C = models.CharField(max_length=20, null=False, blank=False)
    FOLIO_D = models.CharField(max_length=20, null=False, blank=False)
    CLASE_TIPO_ARMA = models.ForeignKey(Tipo, on_delete=models.RESTRICT, null=False, blank=False)
    CALIBRE_ARMA = models.ForeignKey(Calibre, on_delete=models.RESTRICT, null=False, blank=False)
    MARCA_ARMA = models.ForeignKey(Marca, on_delete=models.RESTRICT, null=False, blank=False)
    MODELO_ARMA = models.ForeignKey(Modelo, on_delete=models.RESTRICT, null=False, blank=False)
    MATRICULA = models.CharField(max_length=20, null=False, blank=False, unique=True)
    MATRICULA_CANON = models.CharField(max_length=40, null=True, blank=True)
    FECHA = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    FECHA_LOC = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    ESTADO_ARMA = models.ForeignKey(Edo_conservacion, on_delete=models.RESTRICT, null=False, blank=False)
    FECHA_CAPTURA = models.DateField(null=False, blank=False, validators=[validate_fecha_no_anterior_1990])
    OBSERVACIONES = models.TextField(null=False, blank=False)
    ESTATUS_ARMA = models.ForeignKey(Estatus_Arma, on_delete=models.RESTRICT, null=False, blank=False)
    CUIP_PORTADOR = models.TextField(null=False, validators=[validate_cuip_formato])
    CUIP_RESPONSABLE = models.TextField(null=False, validators=[validate_cuip_formato])
    CIHB = models.CharField(max_length=20, null=True, blank=True)
    TIPO_FUNCIONAMIENTO = models.ForeignKey(TipoFuncinamiento, on_delete=models.RESTRICT, null=False, default=4)
    FECHA_BAJA_LOGICA = models.DateField(null=True, blank=True, validators=[validate_fecha_no_anterior_1990])
    MOTIVO_BAJA = models.TextField(null=True, blank=True)
    DOCUMENTO_BAJA = models.CharField(max_length=20, null=True, blank=True)
    OBSERVACIONES_BAJA = models.TextField(null=True, blank=True)
    FECHA_BAJA_DOCUMENTO = models.DateField(null=True, blank=True, validators=[validate_fecha_no_anterior_1990])
    
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=True)
    
    ultima_modificacion = models.DateTimeField(auto_now=True)

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
    cihb = models.CharField(max_length=20, null=True, blank=True)
    fecha_baja_logica = models.DateField(null=True, blank=True)
    motivo_baja = models.TextField(null=True, blank=True)
    documento_baja = models.CharField(max_length=20, null=True, blank=True)
    observaciones_baja = models.TextField(null=True, blank=True)
    fecha_baja_documento = models.DateField(null=True, blank=True)
    
    usuario = models.CharField(max_length=50)
    
    ultima_modificacion = models.DateTimeField()

    def __str__(self):
        return f"{self.id}-{self.estado}-{self.id_alterna}"