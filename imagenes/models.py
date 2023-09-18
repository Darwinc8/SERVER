from django.db import models
from armamento.models import Armamento
from catalogos.models import Institucion, Entidad, Dependencia, Tipo_Imagen
from django.contrib.auth.models import User

# Create your models here.
class Imagenes(models.Model):
    ID_ALTERNA = models.AutoField(primary_key=True)
    
    ID_ARMA = models.ForeignKey(Armamento, on_delete=models.SET_NULL, blank=True, null=True, to_field='ID_ARMA')
    
    INSTITUCION = models.ForeignKey(Institucion,on_delete=models.RESTRICT)
    
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.RESTRICT)
    
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.RESTRICT)
    
    IMAKEY = models.DecimalField(max_digits=10, decimal_places=0)
    
    DESIMA = models.CharField(max_length=80)
    
    TIPO = models.ForeignKey(Tipo_Imagen,on_delete=models.RESTRICT)
    
    FOLIO = models.DecimalField(max_digits=10, decimal_places=0)
    
    GRUPO = models.CharField(max_length=1)
    
    IMAGEN = models.FileField(upload_to='images/imagenes/',blank=False)
    
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=True)
    
    ultima_modificacion = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
      return f"{self.ID_ALTERNA} - {self.ID_ARMA}" 
   
class ImagenesLog(models.Model):
    id = models.AutoField(primary_key=True)
    id_alterna = models.ForeignKey(Imagenes, on_delete=models.SET_NULL, blank=True, null=True)
    id_arma = models.ForeignKey(Armamento, on_delete=models.SET_NULL, blank=True, null=True, to_field='ID_ARMA')
    estado = models.CharField(max_length=20)
    institucion = models.CharField(max_length=80)
    entidad = models.CharField(max_length=50)
    dependencia = models.CharField(max_length=80)
    imakey = models.DecimalField(max_digits=10, decimal_places=0)
    desima = models.CharField(max_length=80)
    tipo = models.CharField(max_length=50)
    folio = models.DecimalField(max_digits=10, decimal_places=0)
    grupo = models.CharField(max_length=1)
    imagen = models.FileField(upload_to='respaldo/imagenes/',null=False)
    usuario = models.CharField(max_length=50)
    ultima_modificacion = models.DateTimeField()
    
    def __str__(self):
      return f"{self.id} - {self.estado} - {self.id_alterna}"