from django.db.models.signals import post_save
from django.dispatch import receiver
from imagenes.models import Imagenes, ImagenesLog
import os, shutil

@receiver(post_save, sender=Imagenes)
def mi_funcion_despues_de_insert(sender, instance, created, **kwargs):
    if created:
        estado = "Creación"
    else:
        estado = "Modificación"
    
    # Carpeta de destino donde deseas guardar la imagen
    carpeta_destino = 'C:/RNAE_V1/media/respaldo/imagenes/'
    
    if instance.IMAGEN:
        # Genera una ruta única para la imagen en la carpeta de destino
        nombre_archivo = os.path.basename(instance.IMAGEN.path)
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
        
        # Verifica si el archivo ya existe en la carpeta de destino
        if not os.path.exists(ruta_destino):
            # Copia la imagen a la carpeta de destino
            shutil.copy(instance.IMAGEN.path, ruta_destino)
            
    ImagenesLog.objects.create(
        id_alterna = instance,
        id_arma = instance.ID_ARMA,
        estado = estado,
        institucion = instance.INSTITUCION,
        entidad = instance.ENTIDAD,
        dependencia = instance.DEPENDENCIA,
        imakey = instance.IMAKEY,
        desima = instance.DESIMA,
        tipo = instance.TIPO,
        folio = instance.FOLIO,
        grupo = instance.GRUPO,
        imagen = ruta_destino if instance.IMAGEN else None,
        usuario = instance.usuario.username,
        ultima_modificacion = instance.ultima_modificacion
    )
    print("Copia creada...")