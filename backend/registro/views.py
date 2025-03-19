from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer
from .models import Usuario

@api_view(['POST'])
@permission_classes([AllowAny])
def registro(request):
    if request.method == 'POST':
        try:
            data = request.data
            print("🔍 Datos recibidos en Django:", data)  # 🔥 Para depuración

            # Validar que se envían todos los datos requeridos
            required_fields = ['nombre', 'celular', 'email', 'password', 'confirmPassword']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Falta el campo {field}'}, status=400)

            # Validar que las contraseñas coincidan
            if data['password'] != data['confirmPassword']:
                return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

            # Validar el formato de los datos con el serializador
            serializer = UsuarioSerializer(data=data)
            if not serializer.is_valid():
                return JsonResponse({'error': 'Datos inválidos', 'details': serializer.errors}, status=400)

            # Crear el usuario manualmente y encriptar la contraseña
            user = Usuario(
                nombre=data['nombre'],
                celular=data['celular'],
                email=data['email'],
                estado='Activo'  # Se establece automáticamente
            )
            user.set_password(data['password'])  # 🔒 Encriptar contraseña
            user.save()

            return JsonResponse({'mensaje': 'Usuario registrado correctamente', 'usuario_id': user.id}, status=201)

        except Exception as e:
            print("❌ Error en el registro:", str(e))  # 🔥 Para depuración
            return JsonResponse({'error': 'Error en el servidor', 'details': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
