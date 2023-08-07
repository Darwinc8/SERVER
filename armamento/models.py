from django.db import models
from catalogos.models import Institucion, Dependencia, Calibre, Edo_conservacion, Entidad, Estatus_Arma, LOC, Marca, Modelo, Municipio, Tipo

# Create your models here.
class Armamento(models.Model):
    ID_ALTERNA= models.AutoField(primary_key=True)
    ID_ARMA = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    INSTITUCION = models.ForeignKey(Institucion, on_delete=models.RESTRICT)
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT)
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT)
    
    MUNICIPIO = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        to_field='id'
    )
    
    NUMERO_LOC = models.ForeignKey(LOC, on_delete=models.RESTRICT)
    FOLIO_C = models.CharField(max_length=20)
    FOLIO_D = models.CharField(max_length=20)
    CLASE_TIPO_ARMA = models.ForeignKey(Tipo, on_delete=models.RESTRICT)
    CALIBRE_ARMA = models.ForeignKey(Calibre, on_delete=models.RESTRICT)
    MARCA_ARMA = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    MODELO_ARMA = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    MATRICULA = models.CharField(max_length=20)
    MATRICULA_CANON = models.CharField(max_length=40, blank=True)
    FECHA = models.DateField()
    FECHA_LOC = models.DateField()
    ESTADO_ARMA = models.ForeignKey(Edo_conservacion, on_delete=models.RESTRICT)
    FECHA_CAPTURA = models.DateField()
    OBSERVACIONES = models.TextField()
    ESTATUS_ARMA = models.ForeignKey(Estatus_Arma, on_delete=models.RESTRICT)
    CUIP_PORTADOR = models.CharField(max_length=20)
    CUIP_RESPONSABLE = models.CharField(max_length=20)
    CIHB = models.CharField(max_length=20)
    FECHA_BAJA_LOGICA = models.DateField()
    MOTIVO_BAJA = models.TextField()
    DOCUMENTO_BAJA = models.CharField(max_length=20)
    OBSERVACIONES_BAJA = models.TextField()
    FECHA_BAJA_DOCUMENTO = models.DateField()

    def __str__(self):
        return f"{self.ID_ARMA}-{self.CUIP_PORTADOR}-{self.CUIP_RESPONSABLE}"