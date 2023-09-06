from django.db.models.signals import post_save
from django.dispatch import receiver
from portadores.models import Portador, PortadorLog
import os, shutil

@receiver(post_save, sender=Portador)
def mi_funcion_despues_de_insert(sender, instance, created, **kwargs):
    if created:
        estado = "Creación"
    else:
        estado = "Modificación"
    
    # Carpeta de destino donde deseas guardar la imagen
    carpeta_destino = 'C:/RNAE_V1/media/respaldo/portadores/'
    
    if instance.IMAGEN:
        # Genera una ruta única para la imagen en la carpeta de destino
        nombre_archivo = os.path.basename(instance.IMAGEN.path)
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
        
        # Verifica si el archivo ya existe en la carpeta de destino
        if not os.path.exists(ruta_destino):
            # Copia la imagen a la carpeta de destino
            shutil.copy(instance.IMAGEN.path, ruta_destino)
            
    PortadorLog.objects.create(
        id_portador = instance.CUIP,
        estado = estado,
        usuario = instance.usuario.username,
        nombre = instance.NOMBRE,
        apellido_paterno = instance.APELLIDO_PATERNO,
        apellido_materno = instance.APELLIDO_MATERNO,
        correo = instance.CORREO,
        telefono = instance.TELEFONO,
        imagen = ruta_destino if instance.IMAGEN else None,
        ultima_modificacion = instance.ultima_modificacion
    )
    print("Copia creada...")