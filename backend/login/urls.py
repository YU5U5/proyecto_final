from django.urls import path
from .views import LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),  # Ruta para el login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar el token
]