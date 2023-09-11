from django.apps import AppConfig


class ArmamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'armamento'
    
    def ready(self):
        import armamento.signals  # Importa el archivo de señales
       