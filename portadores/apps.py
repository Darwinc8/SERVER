from django.apps import AppConfig


class PortadoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portadores'
   
    def ready(self):
        import portadores.signals  # Importa el archivo de señales