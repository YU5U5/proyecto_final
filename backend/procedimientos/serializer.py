from rest_framework import serializers
from .models import Procedimientos
from registro.models import Usuario
from fish_management.models import Fish

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre']

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ['id', 'profundidad_agua', 'species', 'cantidad_peces', 'etapa', 'tipo_concentrado', 'temperatura_estanque']
        
class ProcedimientosSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = Procedimientos
        fields = ['id_user', 'id_fish', 'tipo_concentrado_actual', 'nombre_procedimiento', 'descripcion_procedimiento', 'observaciones', 'fecha']
        
class ProcedimientosSerializerOutput(serializers.ModelSerializer):
    id_user = UsuarioSerializer(read_only=True)
    id_fish = FishSerializer(read_only=True)
    class Meta:
        model = Procedimientos
        fields = ['id_user', 'id_fish', 'tipo_concentrado_actual', 'nombre_procedimiento', 'descripcion_procedimiento', 'observaciones', 'fecha']