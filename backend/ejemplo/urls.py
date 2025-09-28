from django.urls import path
from .views import Class_Ejemplo_View, Class_Ejemplo_View_Parametros, Class_Ejemplo_Upload

urlpatterns = [
    path('ejemplo', Class_Ejemplo_View.as_view()),
    path('ejemplo/<int:id>', Class_Ejemplo_View_Parametros.as_view(), name="ejemplo_parametros"),
    path('ejemplo-upload', Class_Ejemplo_Upload.as_view(), name="ejemplo_uploads"),
]
