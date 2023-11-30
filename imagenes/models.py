from django.db import models
from django.core.validators import FileExtensionValidator
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
    IMAGEN = models.ImageField(upload_to='images/imagenes/',blank=False, unique=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'])])
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT)
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT)
    INSTITUCION = models.ForeignKey(Institucion, on_delete=models.RESTRICT)
    TIPO = models.ForeignKey(Tipo_Imagen, on_delete=models.RESTRICT)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f"{self.ID_ARMA} - {self.TIPO}"

class ImagenesLog(models.Model):
    imakey = models.DecimalField(max_digits=10, decimal_places=0)
    desima = models.CharField(max_length=80)
    folio = models.DecimalField(max_digits=10, decimal_places=0)
    grupo = models.CharField(max_length=1)
    imagen = models.ImageField(upload_to='respaldo/imagenes/',null=False)
    usuario = models.CharField(max_length=50)
    ultima_modificacion = models.DateTimeField()
    institucion = models.CharField(max_length=80)
    dependencia = models.CharField(max_length=80)
    entidad = models.CharField(max_length=50)
    id_alterna = models.DecimalField(max_digits=10, decimal_places=0)
    id_arma = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
