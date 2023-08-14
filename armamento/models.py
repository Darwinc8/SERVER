from django.db import models
from catalogos.models import Institucion, Dependencia, Calibre, Edo_conservacion, Entidad, Estatus_Arma, LOC, Marca, Modelo, Municipio, Tipo
from portadores.models import Portador

# Create your models here.
class Armamento(models.Model):
    ID_ALTERNA= models.AutoField(primary_key=True)
    ID_ARMA = models.DecimalField(max_digits=10, decimal_places=0, unique=True, null=False, blank=False)
    INSTITUCION = models.ForeignKey(Institucion, on_delete=models.RESTRICT, null=False, blank=False)
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT, null=False, blank=False)
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT, null=False, blank=False)
    
    MUNICIPIO = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        to_field='id', null=False, blank=False
    )
    
    NUMERO_LOC = models.ForeignKey(LOC, on_delete=models.RESTRICT, null=False, blank=False)
    FOLIO_C = models.CharField(max_length=20, null=False, blank=False)
    FOLIO_D = models.CharField(max_length=20, null=False, blank=False)
    CLASE_TIPO_ARMA = models.ForeignKey(Tipo, on_delete=models.RESTRICT, null=False, blank=False)
    CALIBRE_ARMA = models.ForeignKey(Calibre, on_delete=models.RESTRICT, null=False, blank=False)
    MARCA_ARMA = models.ForeignKey(Marca, on_delete=models.RESTRICT, null=False, blank=False)
    MODELO_ARMA = models.ForeignKey(Modelo, on_delete=models.RESTRICT, null=False, blank=False)
    MATRICULA = models.CharField(max_length=20, null=False, blank=False)
    MATRICULA_CANON = models.CharField(max_length=40, null=True, blank=True)
    FECHA = models.DateField(null=False, blank=False)
    FECHA_LOC = models.DateField(null=False, blank=False)
    ESTADO_ARMA = models.ForeignKey(Edo_conservacion, on_delete=models.RESTRICT, null=False, blank=False)
    FECHA_CAPTURA = models.DateField(null=False, blank=False)
    OBSERVACIONES = models.TextField(null=False, blank=False)
    ESTATUS_ARMA = models.ForeignKey(Estatus_Arma, on_delete=models.RESTRICT, null=False, blank=False)
    CUIP_PORTADOR = models.ForeignKey(Portador, on_delete=models.RESTRICT, null=False, blank=False, related_name='armamento_portador')

    CIHB = models.CharField(max_length=20, null=True, blank=True)
    FECHA_BAJA_LOGICA = models.DateField(null=True, blank=True)
    MOTIVO_BAJA = models.TextField(null=True, blank=True)
    DOCUMENTO_BAJA = models.CharField(max_length=20, null=True, blank=True)
    OBSERVACIONES_BAJA = models.TextField(null=True, blank=True)
    FECHA_BAJA_DOCUMENTO = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.ID_ARMA}-{self.CUIP_PORTADOR}-{self.CUIP_RESPONSABLE}"