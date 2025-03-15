"""
WSGI config for ProyectoFinal_F_N project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

os.environ["DJANGO_ALLOWED_HOSTS"] = "proyecto-final-m1eb.onrender.com"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.ProyectoFinal_F_N.settings")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoFinal_F_N.settings')

application = get_wsgi_application()
