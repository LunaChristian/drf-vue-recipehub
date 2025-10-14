from django.urls import path

from .views import Class_Receta_View, Class_Receta_View2

urlpatterns = [
    path('recetas', Class_Receta_View.as_view()),
    path('recetas/<int:id>', Class_Receta_View2.as_view()),
]
