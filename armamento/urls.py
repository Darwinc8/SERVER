from django.urls import path
from . import views
urlpatterns = [
    path('', views.panel_armamento, name='panel_armamento'),
    path('todo/',views.armamento, name='armamento'),
    path('activos/',views.armamento_activos, name='armamento_activos'),
    path('inactivos/',views.armamento_inactivos, name='armamento_inactivos'),
    path('movimientos/',views.movimientos_armamento, name='movimientos_armamento'),
    path('movimientos/<int:id>/',views.ver_movimiento, name='ver_movimiento'),
    path('crear_armamento/',views.crear_armamento, name='crear_armamento'),
    path('crear_armamento/excel',views.crear_armamento_excel, name='armamento_excel'),
    path('crear_armamento/excel/descargar_excel/', views.descargar_plantilla_excel, name='descargar_plantilla_excel'),
     path('ver_armamento/<int:id>/', views.ver_armamento, name='ver_armamento'),
    path('editar_armamento/<int:id>/', views.editar_armamento, name='editar_armamento'),
    path('baja_armamento/<int:id>',views.baja_armamento, name='baja_armamento'),
    path('reactivar_armamento/<int:id>',views.reactivar_armamento, name='reactivar_armamento'),
    path('eliminar_armamento/<int:id>',views.eliminar_armamento, name='eliminar_armamento'),
    path('obtener_municipios/<int:entidad_id>/', views.obtener_municipios, name='obtener_municipios'),
    path('obtener_instituciones/<int:dependencia_id>/', views.obtener_instituciones, name='obtener_instituciones'),
    ]