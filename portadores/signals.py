from django.db.models.signals import post_save
from django.dispatch import receiver
from portadores.models import Portador, PortadorLog

@receiver(post_save, sender=Portador)
def mi_funcion_despues_de_insert(sender, instance, created, **kwargs):
    if created:
        print("Portador creado...")
        PortadorLog.objects.create(
           id_portador = instance.CUIP,
           estado = "Creación",
           usuario = instance.usuario.username,
           ultima_modificacion = instance.ultima_modificacion
        )
        print("Copia creada...")
        pass