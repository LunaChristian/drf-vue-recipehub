from rest_framework import serializers
from .models import Receta

class RecetaSerializer(serializers.ModelSerializer):
    
    categoria = serializers.ReadOnlyField(source='categoria.titulo')
    fecha = serializers.DateTimeField(format="%d/%m/%Y")
    
    class Meta:
        model = Receta
        fields = ('id', 'titulo_receta', 'slug', 'tiempo', 'descripcion', 'fecha', 'categoria', 'categoria_id')
        #fields = '__all__'