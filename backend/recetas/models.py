from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Receta(models.Model):
    titulo_receta = models.CharField(max_length=100, null=False)
    
    
    def __str__(self):
        return self.titulo_receta
    
    class Meta:
        db_table = 'recetas'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
    