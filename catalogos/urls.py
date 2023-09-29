from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogos, name='catalogos'),
    path('emisores/', views.emisores, name='emisores'),
    path('entidades/', views.entidades, name='entidades'),
    path('dependencias/', views.dependencias, name='dependencias'),
    path('locs/', views.locs, name='locs'),
    path('edo_conservacion/', views.edo_conservacion, name='edo_conservacion'),
    path('instituciones/', views.instituciones, name='instituciones'),
    path('tipos/', views.tipos, name='tipos'),
    path('calibres/', views.calibres, name='calibres'),
    path('marcas/', views.marcas, name='marcas'),
    path('modelos/', views.modelos, name='modelos'),
    path('estatus_arma/', views.estatus_arma, name='estatus_arma'),
    path('tipo_alta/', views.tipo_alta, name='tipo_alta'),
    path('tipo_dependencia/', views.tipo_dependencia, name='tipo_dependencia'),
    path('tipo_imagen/', views.tipo_imagen, name='tipo_imagen'),
    path('municipios/', views.municipios, name='municipios')
    ]