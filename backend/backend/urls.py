from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('api/v1/', include('ejemplo.urls'), name='ejemplo'),
    path('api/v1/', include('categorias.urls'), name='categorias'),    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
