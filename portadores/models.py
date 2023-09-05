from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
# Create your models here.
class Portador(models.Model):
    CUIP = models.CharField(max_length=20, primary_key=True)
    NOMBRE = models.CharField(max_length=30,blank=False)
    APELLIDO_PATERNO = models.CharField(max_length=30,blank=False)
    APELLIDO_MATERNO = models.CharField(max_length=30,blank=False)
    CORREO = models.EmailField(max_length=254,blank=False)
    TELEFONO = models.CharField(max_length=10,blank=False)
    IMAGEN = models.FileField(upload_to='portadores/',blank=False)
    
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=False)
    
    ultima_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.CUIP} - {self.NOMBRE} {self.APELLIDO_PATERNO} {self.APELLIDO_MATERNO}"
 
class PortadorLog(models.Model):
    id = models.AutoField(primary_key=True)
    id_portador = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    usuario = models.CharField(max_length=50)
    ultima_modificacion = models.DateTimeField()