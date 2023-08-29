from django.db.models.signals import post_save
from django.dispatch import receiver
from portadores.models import Portador, LogPortador

@receiver(post_save, sender=Portador)
def after_insert(sender, instance, created, **kwargs):
    if created:
        print(f"Portador {instance.NOMBRE} creado...")