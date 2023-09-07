from django.apps import AppConfig


class ImagenesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imagenes'

    def ready(self):
        import imagenes.signals  # Importa el archivo de señales