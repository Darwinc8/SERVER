from django.urls import path
from . import views

urlpatterns = [
    path('', views.portadores, name='portadores'),
    path('crear_portador/', views.crear_portador, name='crear_portador'),
    path('editar_portador/<str:id>', views.editar_portador, name='editar_portador'),
    path('eliminar_portador/<str:id>', views.eliminar_portador, name='eliminar_portador')
]