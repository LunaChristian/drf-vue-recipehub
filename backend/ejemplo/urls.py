from django.urls import path
from .views import Class_Ejemplo_View

urlpatterns = [
    path('ejemplo', Class_Ejemplo_View.as_view()),
]
