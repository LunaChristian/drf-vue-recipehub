from django.urls import path

from .views import RecetaHelperView

urlpatterns = [
    path('categorias', RecetaHelperView.as_view()),
]
