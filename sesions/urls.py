from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('registrarse/',views.registrarse, name='registrarse'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/',views.cerrar_sesion, name='cerrar_sesion'),
    path('cambiar_lenguaje/<str:language_code>/', views.cambiar_lenguaje, name='cambiar_lenguaje')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)