from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import ProcedimientosSerializerInput, ProcedimientosSerializerOutput
from rest_framework import status
from .models import Procedimientos

# Create your views here.

class CreateProcedimiento(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = ProcedimientosSerializerInput(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(ProcedimientosSerializerOutput(serializer.data).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateProcedimiento(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, pk=None):  
        try: 
            estanque = Procedimientos.objects.get(pk=pk)
            serializer = ProcedimientosSerializerInput(data=request.data, instance=estanque, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(ProcedimientosSerializerOutput(serializer.data).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
class List(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = ProcedimientosSerializerOutput(Procedimientos.objects.all(), many=True)
        return Response(serializer.data)

class Details(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        serializer = ProcedimientosSerializerOutput(Procedimientos.objects.get(pk=pk))        
        return Response(serializer.data)    