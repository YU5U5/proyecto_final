from rest_framework import serializers
from .models import Fish
from registro.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre']

class FishSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fiels = ['id_user','tipo_estanque', 'profundidad_agua', 'largo', 'ancho', 'species', 'cantidad_peces', 'etapa', 'tipo_concentrado', 'temperatura_estanque', 'estado']
        
class FishSerializerOutput(serializers.ModelSerializer):
    id_user = UsuarioSerializer(read_only=True)
    class Meta:
        model = Fish
        fields = ['id_user','tipo_estanque', 'profundidad_agua', 'largo', 'ancho', 'species', 'cantidad_peces', 'etapa', 'tipo_concentrado', 'temperatura_estanque', 'estado']
        
       