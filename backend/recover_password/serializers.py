from rest_framework import serializers
from registro.models import Usuario
from django.contrib.auth.password_validation import validate_password



class SolicitarRecuperacionSerializer(serializers.Serializer):
    correo_electronico = serializers.EmailField()

class ConfirmarTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

class RecuperarContraseñaSerializer(serializers.Serializer):
    nueva_contraseña = serializers.CharField(write_only=True)
    confirmar_contraseña = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validar que ambas contraseñas coincidan y cumplan con las reglas de seguridad.
        """
        if data['nueva_contraseña'] != data['confirmar_contraseña']:
            raise serializers.ValidationError({"error": "Las contraseñas no coinciden."})

        # Validar seguridad de la contraseña
        validate_password(data['nueva_contraseña'])

        return data