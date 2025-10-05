from django.urls import path
from .views import Class_Categoria_View

urlpatterns = [
    path('categorias', Class_Categoria_View.as_view()),
]
