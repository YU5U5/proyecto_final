from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from registro.models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        print("🔍 Datos recibidos en el backend:", request.data) 

        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            print("❌ Errores de validación:", serializer.errors) 
            return Response({
                'mensaje': 'Error en el inicio de sesión',
                'errores': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            print("❌ Usuario no encontrado con email:", email) 
            return Response({'mensaje': 'Correo o contraseña inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

        if usuario.estado != 'Activo':
            print("⚠ Usuario no está activo:", usuario.estado)
            return Response({'mensaje': 'El usuario no está activo.'}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, usuario.password):
            print("❌ Contraseña incorrecta para:", email) 
            return Response({'mensaje': 'Correo o contraseña inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario.last_login = now()
        usuario.save(update_fields=['last_login'])

        refresh = RefreshToken.for_user(usuario)

        print("✅ Login exitoso para:", email)

        return Response({
            'mensaje': 'Inicio de sesión exitoso',
            'email': usuario.email,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)
        

