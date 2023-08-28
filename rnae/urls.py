
from django.contrib import admin
from django.urls import path, include
from catalogos import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('catalogos/', include('catalogos.urls')),
    path('', include('sesions.urls')),
    path('armamento/', include('armamento.urls')),
    path('portadores/', include('portadores.urls')),
    path('imagenes/', include('imagenes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'utilidades.views.error_404_view'