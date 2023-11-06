from django.db import models
from catalogos.models import Institucion, Dependencia, Entidad, Tipo_Imagen
from armamento.models import Armamento
from django.contrib.auth.models import User

class Imagenes(models.Model):
    ID_ALTERNA = models.AutoField(primary_key=True)
    ID_ARMA = models.ForeignKey(Armamento, to_field='MATRICULA', on_delete=models.RESTRICT)
    IMAKEY = models.DecimalField(max_digits=10, decimal_places=0)
    DESIMA = models.CharField(max_length=80)
    FOLIO = models.DecimalField(max_digits=10, decimal_places=0)
    GRUPO = models.CharField(max_length=1)
    IMAGEN = models.CharField(unique=True, max_length=100)
    DEPENDENCIA = models.ForeignKey(Dependencia, models.DO_NOTHING)
    ENTIDAD = models.ForeignKey(Entidad, models.DO_NOTHING)
    INSTITUCION = models.ForeignKey(Institucion, models.DO_NOTHING)
    TIPO = models.ForeignKey(Tipo_Imagen, models.DO_NOTHING)
    ultima_modificacion = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class ImagenesLog(models.Model):
    imakey = models.DecimalField(max_digits=10, decimal_places=0)
    desima = models.CharField(max_length=80)
    folio = models.DecimalField(max_digits=10, decimal_places=0)
    grupo = models.CharField(max_length=1)
    imagen = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)
    ultima_modificacion = models.DateTimeField()
    institucion = models.CharField(max_length=80)
    dependencia = models.CharField(max_length=80)
    entidad = models.CharField(max_length=50)
    id_alterna = models.DecimalField(max_digits=10, decimal_places=0)
    id_arma = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
