"""
WSGI config for v_books project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Añade la ruta de tu proyecto al path
path = '/home/victorceronl/v_books' 
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v_books.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
