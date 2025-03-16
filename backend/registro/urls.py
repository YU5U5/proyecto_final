from django.urls import path
from .views import registro

urlpatterns = [
    path('api/register/',registro, name='registro'),  # Ruta para el registro
]
