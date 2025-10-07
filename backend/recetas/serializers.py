from rest_framework import serializers
from .models import Receta
import os

class RecetaSerializer(serializers.ModelSerializer):
    
    categoria = serializers.ReadOnlyField(source='categoria.titulo')
    fecha = serializers.DateTimeField(format="%d/%m/%Y")
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = Receta
        fields = ('id', 'titulo_receta', 'slug', 'tiempo', 'descripcion', 'fecha', 'categoria', 'categoria_id', 'imagen')
    
    def get_imagen(sefl, obj):
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"