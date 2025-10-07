from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        #fields = ('id', 'titulo', 'slug')
        fields = ('__all__')