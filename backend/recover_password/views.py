from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.core.signing import TimestampSigner, BadSignature
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registro.models import Usuario

class SolicitarRecuperacion(APIView):
    def post(self, request):
        email = request.data.get('correo_electronico')
        try:
            usuario = Usuario.objects.get(email=email)
            signer = TimestampSigner()
            token = signer.sign(usuario.id)

            send_mail(
                "Recuperación de contraseña",
                f"Tu código de recuperación es: {token}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return Response({"mensaje": "Código enviado", "token": token}, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response({"error": "Correo no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

class ConfirmarCodigo(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            signer = TimestampSigner()
            usuario_id = signer.unsign(token)
            usuario = Usuario.objects.get(id=usuario_id)
            return Response({"mensaje": "Código válido"}, status=status.HTTP_200_OK)

        except (BadSignature, Usuario.DoesNotExist):
            return Response({"error": "Código inválido"}, status=status.HTTP_400_BAD_REQUEST)

class RestablecerContraseña(APIView):
    def post(self, request):
        token = request.data.get('token')
        nueva_contraseña = request.data.get('nueva_contraseña')
        confirmar_contraseña = request.data.get('confirmar_contraseña')

        if nueva_contraseña != confirmar_contraseña:
            return Response({"error": "Las contraseñas no coinciden"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            signer = TimestampSigner()
            usuario_id = signer.unsign(token)
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.set_password(nueva_contraseña)
            usuario.save()
            return Response({"mensaje": "Contraseña cambiada con éxito"}, status=status.HTTP_200_OK)

        except (BadSignature, Usuario.DoesNotExist):
            return Response({"error": "Código inválido"}, status=status.HTTP_400_BAD_REQUEST)


