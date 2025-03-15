from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarRecuperacion, RestablecerContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
    path('confirmar/', ConfirmarRecuperacion.as_view(), name='confirmar_recuperacion'),
    path('restablecer/', RestablecerContraseña.as_view(), name='restablecer_contraseña'),
]

  