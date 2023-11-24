from django.contrib import admin
from .models import Emisor, Entidad, Edo_conservacion, Calibre, Marca, Modelo,  Estatus_Arma, Tipo_Alta, Tipo_Dependencia,  Tipo_Imagen, Dependencia, LOC, Tipo, Institucion, Municipio, TipoFuncinamiento, Propiedad

# Registro de los modelos para que aparezcan en el panel de administrador
admin.site.register(Emisor)
admin.site.register(Entidad)
admin.site.register(Edo_conservacion)
admin.site.register(Calibre)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Estatus_Arma)
admin.site.register(Tipo_Alta)
admin.site.register(Tipo_Dependencia)
admin.site.register(Tipo_Imagen)
admin.site.register(Dependencia)
admin.site.register(LOC)
admin.site.register(Tipo)
admin.site.register(Institucion)
admin.site.register(Municipio)
admin.site.register(TipoFuncinamiento)
admin.site.register(Propiedad)



