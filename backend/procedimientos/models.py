from django.db import models
from fish_management.models import Fish
from registro.models import Usuario

# Create your models here.

class Procedimientos(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    tipo_concentrado_actual = models.CharField(max_length=100)
    nombre_procedimiento = models.CharField(max_length=100)
    descripcion_procedimiento = models.TimeField()
    observaciones = models.TimeField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    
   