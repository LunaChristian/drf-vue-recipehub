from django.urls import path
from .views import Class_Ejemplo_View, Class_Ejemplo_View_Parametros

urlpatterns = [
    path('ejemplo', Class_Ejemplo_View.as_view()),
    path('ejemplo/<int:id>', Class_Ejemplo_View_Parametros.as_view(), name="ejemplo_parametros")
]
