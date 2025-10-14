from autoslug import AutoSlugField
from django.db import models


# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    slug = AutoSlugField(populate_from='titulo')
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    