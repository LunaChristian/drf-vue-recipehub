from django.urls import path

from .views import Contacto_View

urlpatterns = [
    path('contacto', Contacto_View.as_view()),
]
