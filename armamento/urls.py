from django.urls import path
from . import views
urlpatterns = [
    path('', views.armamento, name='armamento'),
    path('crear_armamento/',views.crear_armamento, name='crear_armamento'),
    path('editar_armamento/<int:id>',views.editar_armamento, name='editar_armamento'),
    path('eliminar_armamento/<int:id>',views.eliminar_armamento, name='eliminar_armamento'),
    path('obtener_municipios/<int:entidad_id>/', views.obtener_municipios, name='obtener_municipios'),
    path('obtener_instituciones/<int:dependencia_id>/', views.obtener_instituciones, name='obtener_instituciones'),
    ]