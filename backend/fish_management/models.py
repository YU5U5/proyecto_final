from django.db import models
from registro.models import Usuario

# Create your models here.

class Fish(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo_estanque  = models.CharField(max_length=100)
    profundidad_agua = models.FloatField()
    largo = models.FloatField()
    ancho = models.FloatField()
    species = models.CharField(max_length=100)
    cantidad_peces = models.IntegerField()
    etapa = models.CharField(max_length=100)
    tipo_concentrado = models.CharField(max_length=100)
    temperatura_estanque = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name