import os

from django.utils.dateformat import DateFormat
from rest_framework import serializers

from .models import Receta


class RecetaSerializer(serializers.ModelSerializer):
    
    categoria = serializers.ReadOnlyField(source='categoria.titulo')
    #fecha = serializers.DateTimeField(format="%d/%m/%Y")
    fecha = serializers.SerializerMethodField()
    imagen = serializers.SerializerMethodField()
    
    class Meta:
        model = Receta
        fields = ('id', 'titulo_receta', 'slug', 'tiempo', 'descripcion', 'fecha', 'categoria', 'categoria_id', 'imagen')
        
    def get_fecha(self, obj):
        return DateFormat(obj.fecha).format('d/m/Y')
    
    def get_imagen(self, obj):
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"