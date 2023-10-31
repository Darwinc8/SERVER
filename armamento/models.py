from django.db import models
from catalogos.models import Institucion, Dependencia, Calibre, Edo_conservacion, Entidad, Estatus_Arma, LOC, Marca, Modelo, Municipio, Tipo
from portadores.models import Portador
from django.contrib.auth.models import User

# Create your models here.
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
    FECHA = models.DateField(null=False, blank=False)
    FECHA_LOC = models.DateField(null=False, blank=False)
    ESTADO_ARMA = models.ForeignKey(Edo_conservacion, on_delete=models.RESTRICT, null=False, blank=False)
    FECHA_CAPTURA = models.DateField(null=False, blank=False)
    OBSERVACIONES = models.TextField(null=False, blank=False)
    ESTATUS_ARMA = models.ForeignKey(Estatus_Arma, on_delete=models.RESTRICT, null=False, blank=False)
    CUIP_PORTADOR = models.TextField(null=False)
    CUIP_RESPONSABLE = models.TextField(null=False)
    CIHB = models.CharField(max_length=20, null=True, blank=True)
    FECHA_BAJA_LOGICA = models.DateField(null=True, blank=True)
    MOTIVO_BAJA = models.TextField(null=True, blank=True)
    DOCUMENTO_BAJA = models.CharField(max_length=20, null=True, blank=True)
    OBSERVACIONES_BAJA = models.TextField(null=True, blank=True)
    FECHA_BAJA_DOCUMENTO = models.DateField(null=True, blank=True)
    
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=True)
    
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.MATRICULA}"

class ArmamentoLog(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)
    id_alterna= models.DecimalField(max_digits=10, decimal_places=0)
    id_arma = models.DecimalField(max_digits=10, decimal_places=0)
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
    cihb = models.CharField(max_length=20, null=False, blank=False)
    fecha_baja_logica = models.DateField(null=True, blank=True)
    motivo_baja = models.TextField(null=True, blank=True)
    documento_baja = models.CharField(max_length=20, null=True, blank=True)
    observaciones_baja = models.TextField(null=True, blank=True)
    fecha_baja_documento = models.DateField(null=True, blank=True)
    
    usuario = models.CharField(max_length=50)
    
    ultima_modificacion = models.DateTimeField()

    def __str__(self):
        return f"{self.id}-{self.estado}-{self.id_alterna}"