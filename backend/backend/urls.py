from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Curso Fullstack... ejemplo de titulo",
        default_version='v1',
        description="Api desarrollada para implementación de Backend de sistema de recetas, para curso Fullstack",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="email@email.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('api/v1/', include('ejemplo.urls'), name='ejemplo'),
    path('api/v1/', include('categorias.urls'), name='categoria'),
    path('api/v1/', include('recetas.urls'),name='recetas'),
    path('api/v1/', include('seguridad.urls'),name='seguridad'),
    path('api/v1/', include('contacto.urls'),name='contacto'),
    path('api/v1/', include('recetas_helper.urls'),name='recetas_herlpers'),
    path('documentation<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
