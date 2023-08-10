from django.urls import path
from . import views
from django.views.i18n import set_language
urlpatterns = [
    path('registrarse/',views.registrarse, name='registrarse'),
    path('iniciar_sesion/',views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/',views.cerrar_sesion, name='cerrar_sesion'),
    path('set_language/', set_language, name='set_language'),
    path('change_language/<str:lang_code>/', views.cambiar_lenguaje, name='change_language'),
]