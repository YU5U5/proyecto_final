from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarCodigo, RestablecerContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
    path('confirmar/', ConfirmarCodigo.as_view(), name='confirmar_codigo'),
    path('restablecer/', RestablecerContraseña.as_view(), name='restablecer_contraseña'),
]
