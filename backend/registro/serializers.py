from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['nombre', 'celular', 'email', 'password', 'confirmPassword']
        
    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')  # ✅ Eliminar confirmPassword antes de guardar
        user = Usuario.objects.create(**validated_data)
        user.set_password(validated_data['password'])  # ✅ Hashear la contraseña
        user.save()
        return user
