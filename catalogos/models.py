from django.db import models
from django.contrib.auth.models import User

# Creando los modelos de los catalogos
class Emisor(models.Model):
    Id_Emisor = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    Tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Tipo
    
class Entidad(models.Model):
    ID_ENTIDAD = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    ENTIDAD = models.CharField(max_length=50)
    SIGLAS = models.CharField(max_length=3)
    
    def __str__(self):
        return self.ENTIDAD

class LOC(models.Model):
    ID_ENTIDAD =  models.DecimalField(max_digits=10, decimal_places=0)
    ENTIDAD = models.CharField(max_length=50)
    DEPENDENCIA = models.CharField(max_length=5)
    NO_LICENCIA = models.CharField(max_length=20)
    
    def __str__(self):
        return self.NO_LICENCIA

class Edo_conservacion(models.Model):
    ID_ESTADO = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    DESCRIPCION = models.CharField(max_length=20)
    
    def __str__(self):
        return self.DESCRIPCION

class Tipo(models.Model):
    ID_TIPO = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    TIPO = models.CharField(max_length=50)
    
    OPCIONES = (
        (0, 'Opción 0'),
        (1, 'Opción 1'),
        (2, 'Opción 2'),
    )
    
    ID_CLASIFICACION = models.IntegerField(choices=OPCIONES)
    
    def __str__(self):
        return self.TIPO
    
class Calibre(models.Model):
    ID_CALIBRE = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    CALIBRE = models.CharField(max_length=50)
    
    def __str__(self):
        return self.CALIBRE

class Marca(models.Model):
    ID_MARCA = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    MARCA = models.CharField(max_length=50)
    
    def __str__(self):
        return self.MARCA
    
class Modelo(models.Model):
    ID_MODELO = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    MODELO = models.CharField(max_length=50)
    
    def __str__(self):
        return self.MODELO

class Estatus_Arma(models.Model):
    ID_ESTATUS = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    DESCRIPCION = models.CharField(max_length=30)
    
    def __str__(self):
        return self.DESCRIPCION

class Tipo_Alta(models.Model):
    ID_ALTA = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    DESCRIPCION = models.CharField(max_length=20)
    
    def __str__(self):
        return self.DESCRIPCION    

class Tipo_Dependencia(models.Model):
    ID_TIPO_DEPENEDIENCIA = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    TIPO_DEPENEDENCIA = models.CharField(max_length=30)
    
    def __str__(self):
        return self.TIPO_DEPENEDENCIA

class Tipo_Imagen(models.Model):
    ID_IMAGEN = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    DESCRIPCION = models.CharField(max_length=50)
    
    def __str__(self):
        return self.DESCRIPCION

class Dependencia(models.Model):
    ID_TIPO_DEPENDENCIA = models.ForeignKey(Tipo_Dependencia, on_delete=models.CASCADE)
    ID_DEPENDENCIA = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    DEPENDENCIA = models.CharField(max_length=70)
    
    def __str__(self):
        return self.DEPENDENCIA  
    
class Institucion(models.Model):
    ID_INSTITUCION = models.DecimalField(max_digits=10, decimal_places=0, primary_key=True)
    NOMBRE = models.CharField(max_length=70)
    ID_TIPO_DEPENDENCIA = models.ForeignKey(Tipo_Dependencia, on_delete=models.CASCADE)
    ID_DEPENDENCIA = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NOMBRE
    
class Municipio(models.Model):
    ID_ENTIDAD = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    ID_MUNICIPIO = models.DecimalField(max_digits=10, decimal_places=0)
    MUNICIPIO = models.CharField(max_length=70)
    
    def __str__(self):
        return self.MUNICIPIO
    
    class Meta:
        unique_together = ('ID_ENTIDAD', 'ID_MUNICIPIO')
        
class TipoFuncinamiento(models.Model):
    ID = models.AutoField(primary_key=True)
    TipoFuncionamiento = models.TextField(max_length=20)
    Status = models.IntegerField(choices=[(0, 'Deshabilitado'), (1, 'Habilitado')])
