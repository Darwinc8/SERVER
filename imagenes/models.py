from django.db import models
from armamento.models import Armamento
from catalogos.models import Institucion, Entidad, Dependencia, Tipo_Imagen

# Create your models here.
class Imagenes(models.Model):
    ID_ALTERNA = models.AutoField(primary_key=True)
    
    ID_ARMA = models.ForeignKey(Armamento, on_delete=models.CASCADE, to_field='ID_ARMA')
    
    INSTITUCION = models.ForeignKey(Institucion,on_delete=models.CASCADE)
    
    ENTIDAD = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    
    DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    
    IMAKEY = models.DecimalField(max_digits=10, decimal_places=0)
    
    DESIMA = models.CharField(max_length=80)
    
    TIPO = models.ForeignKey(Tipo_Imagen,on_delete=models.CASCADE)
    
    FOLIO = models.DecimalField(max_digits=10, decimal_places=0)
    
    GRUPO = models.CharField(max_length=1)
    
    IMAGEN = models.FileField(upload_to='images/imagenes/',blank=False)
    
    def __str__(self):
       return f"{self.ID_ALTERNA} - {self.ID_ARMA}" 
   
