from django.urls import path

from .views import Seguridad, Verificacion

urlpatterns = [
    path('seguridad/registro', Seguridad.as_view()),
    path('seguridad/verificacion/<str:token>', Verificacion.as_view())
]
