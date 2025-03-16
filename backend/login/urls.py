from django.urls import path
from .views import LoginView
from django.urls import path
from .views import LoginView  # Asegúrate de importar correctamente la vista
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/login/", LoginView.as_view(), name="login"),  # ✅ Ruta correcta
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
