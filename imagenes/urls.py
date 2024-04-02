from django.urls import path
from . import views

urlpatterns = [
    path('', views.imagenes, name='imagenes'),
    path('crear_imagen/', views.crear_imagen, name='crear_imagen'),
    path('eliminar_imagen/<int:id>', views.eliminar_imagen, name='eliminar_imagen'),
    path('editar_imagen/<int:id>', views.editar_imagen, name='editar_imagen'),
    path('obtener_instituciones/<int:dependencia_id>/', views.obtener_instituciones, name='obtener_instituciones')
]