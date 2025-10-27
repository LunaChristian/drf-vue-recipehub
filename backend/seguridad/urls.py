from django.urls import path

from .views import Clase_1
urlpatterns = [
    path('seguridad/registro', Clase_1.as_view())
]
