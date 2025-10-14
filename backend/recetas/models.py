from autoslug import AutoSlugField
from django.db import models

from categorias.models import Categoria


# Create your models here.
class Receta(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    titulo_receta = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='titulo_receta', max_length=100)
    tiempo = models.CharField(max_length=100, null=True)
    foto = models.CharField(max_length=100, null=True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.titulo_receta
    
    class Meta:
        db_table = 'recetas'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
    