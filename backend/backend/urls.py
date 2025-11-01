from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('api/v1/', include('ejemplo.urls'), name='ejemplo'),
    path('api/v1/', include('categorias.urls'), name='categoria'),
    path('api/v1/', include('recetas.urls'),name='recetas'),
    path('api/v1/', include('seguridad.urls'),name='seguridad'),
    path('api/v1/', include('contacto.urls'),name='contacto'),
    path('api/v1/', include('recetas_helper.urls'),name='recetas_herlpers')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
