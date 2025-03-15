from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

from registro.models import Usuario

from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from registro.models import Usuario
from .serializers import SolicitarRecuperacionSerializer, RecuperarContraseñaSerializer
from django.urls import reverse

class SolicitarRecuperacion(APIView):
    def post(self, request):
        serializer = SolicitarRecuperacionSerializer(data=request.data)
        if serializer.is_valid():
            correo_electronico = serializer.validated_data['correo_electronico']
            try:
                usuario = Usuario.objects.get(correo_electronico=correo_electronico)

                # Generar token firmado
                signer = TimestampSigner()
                token = signer.sign(usuario.id)  # Cifra el ID del usuario

                # Enviar solo el token al frontend
                return Response({"token": token}, status=status.HTTP_200_OK)

            except Usuario.DoesNotExist:
                return Response({'mensaje': 'Si el correo está registrado, recibirás un enlace de recuperación.'}, status=status.HTTP_200_OK)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmarRecuperacion(APIView):
    def post(self, request):
        token = request.data.get("token")  # El frontend solo envía el token

        if not token:
            return Response({'error': 'Token no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)

        signer = TimestampSigner()
        try:
            usuario_id = signer.unsign(token, max_age=600)  # Desencripta el token
            return Response({"mensaje": "Token válido."}, status=status.HTTP_200_OK)

        except (BadSignature, SignatureExpired):
            return Response({'error': 'El enlace es inválido o ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class RestablecerContraseña(APIView):
    def post(self, request):
        token = request.data.get("token")
        serializer = RecuperarContraseñaSerializer(data=request.data)

        if not token:
            return Response({'error': 'Token no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            signer = TimestampSigner()
            try:
                usuario_id = signer.unsign(token, max_age=600)
                usuario = Usuario.objects.get(id=usuario_id)

                # Guardar la nueva contraseña
                usuario.set_password(serializer.validated_data['nueva_contraseña'])
                usuario.save()

                return Response({'mensaje': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)

            except (BadSignature, SignatureExpired):
                return Response({'error': 'El enlace es inválido o ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)
            except Usuario.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ConfirmarRecuperacion(APIView):
    def post(self, request, token):
        signer = TimestampSigner() 
        
        try:
            # Verificar y desencriptar el token
            usuario_id = signer.unsign(token, max_age=600)  # Expira en 600 segundos (10 minutos)

            # Buscar al usuario en la base de datos
            usuario = Usuario.objects.get(id=usuario_id)

            nueva_contraseña = request.data['nueva_contraseña']
            confirmar_contraseña = request.data['confirmar_contraseña']
            
            if not nueva_contraseña or not confirmar_contraseña:
                return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)
            
            if nueva_contraseña != confirmar_contraseña:
                return Response({'mensaje': 'Las contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Actualizar la contraseña
            usuario.set_password(nueva_contraseña)
            usuario.save()
            
            send_mail(
                'contraseña cambiada',
                'Tu contraseña ha sido cambiada.',
                settings.EMAIL_HOST_USER,
                [usuario.correo_electronico],
                fail_silently=False,
            )
            
            return Response({'mensaje': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)
        
        except(BadSignature, SignatureExpired):
            return Response({'error':'el enlace es invalido o ha expirado'},status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
        
    


