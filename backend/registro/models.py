from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, celular, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre=nombre, celular=celular, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, nombre, password, **extra_fields)

class Usuario(AbstractBaseUser):
    ESTADO = [
        ('activo', 'Activo'),
        ('pendiente_verificacion', 'Pendiente de Verificación'),
    ]

    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=30, choices=ESTADO, default='activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Usuario'
        managed = True