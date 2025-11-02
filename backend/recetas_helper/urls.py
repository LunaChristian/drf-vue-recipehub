from django.urls import path
from .views import RecetaHelperView, ImgEditorHelperView, RecetaDetailView, RecetasHome, RecetaSearchView

#Usar sustantivos (plural) para los nombres de las rutas y no verbos
urlpatterns = [
    path('recetas-helper/home', RecetasHome.as_view()),
    path('recetas-helper/<int:id>', RecetaHelperView.as_view()),
    path('recetas-helper/editar-foto', ImgEditorHelperView.as_view()),
    path('recetas-helper/slug/<str:slug>', RecetaDetailView.as_view()),
    path('recetas-helper/buscador', RecetaSearchView.as_view())
]