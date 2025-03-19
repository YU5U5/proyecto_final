"""
Django settings for ProyectoFinal_F_N project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n@r%-_laj)b+64%3j7*n#izgor9sqcm0#y=5ww!_&h7e%29%i4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [

    "proyecto-final-m1eb.onrender.com",
    "6fe7-179-1-210-205.ngrok-free.app",

]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'registro',
    'login',
    'fish_management',
    'procedimientos',
    'rest_framework',
    'rest_framework_simplejwt',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP
EMAIL_PORT = 587  # Puerto para TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER='fishnexus5@gmail.com'
EMAIL_HOST_PASSWORD='vvje psnn bwbb eybt'# Tu contraseña de correo electrónico

DEFAULT_FROM_EMAIL = 'fishnexus5@gmail.com'

TOKEN_RECUPERACION_EXPIRA_MINUTOS = 10

# Configuraciones de seguridad 

SESSION_COOKIE_SECURE = True  # Solo enviar cookies de sesión sobre HTTPS
SESSION_COOKIE_HTTPONLY = True  # Evitar acceso a cookies desde JavaScript
CSRF_COOKIE_SECURE = True  # Solo enviar cookies CSRF sobre HTTPS
CSRF_COOKIE_HTTPONLY = True  # Evitar acceso a cookies CSRF desde JavaScript

# Configuración de expiración de la sesión
SESSION_COOKIE_AGE = 1800  # La sesión expira después de 30 minutos (en segundos)
SESSION_SAVE_EVERY_REQUEST = True  # Renovar la sesión en cada solicitud

# Configuración de seguridad adicional
SECURE_BROWSER_XSS_FILTER = True  # Habilitar filtro XSS en el navegador
SECURE_CONTENT_TYPE_NOSNIFF = True  # Evitar sniffing de tipos MIME
X_FRAME_OPTIONS = 'DENY'  # Evitar que la página se incruste en un iframe

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:5500",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "https://6fe7-179-1-210-205.ngrok-free.app",
    

]


CORS_ALLOW_CREDENTIALS = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # ✅ Permite el frontend local

    "https://6fe7-179-1-210-205.ngrok-free.app",  # ✅ Permite el frontend con Ngrok

]


CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "ngrok-skip-browser-warning",  # 🔥 Agregar este encabezado
]


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://6fe7-179-1-210-205.ngrok-free.app",

]

CORS_ALLOW_CREDENTIALS = True  # ✅ Permitir envío de cookies o credenciales

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Permitir el login sin autenticación previa
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Duración del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Duración del refresh token
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

AUTH_USER_MODEL = 'registro.Usuario'
# Cambia 'registro' por el nombre de la app donde está el modelo Usuario

ROOT_URLCONF = 'ProyectoFinal_F_N.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoFinal_F_N.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fish',  # Nombre de tu base de datos
        'USER': 'avnadmin',  # Tu usuario de MySQL
        'PASSWORD': 'AVNS_HWIjUZsf6b-yPGrOQXu',  # No tiene contraseña
        'HOST': 'dbproyectofinal-samuelosoriogaspar-8cec.j.aivencloud.com',  # Dirección del servidor MySQL
        'PORT': '16159',  # Puerto de MySQL
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
