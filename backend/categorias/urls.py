from django.urls import path
from .views import Class_Categoria_View, Class_Categoria_View2

urlpatterns = [
    path('categorias', Class_Categoria_View.as_view()),
    path('categorias/<int:id>', Class_Categoria_View2.as_view()),
]
