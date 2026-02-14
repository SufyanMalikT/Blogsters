"""
WSGI config for Blogsters project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

import os
import sys

# 1. Add your project directory to the sys.path
path = '/home/sufyanmalik123/Blogsters'
if path not in sys.path:
    sys.path.insert(0, path)

# 2. Tell Django where your settings are
# Make sure 'Blogsters' matches the folder name containing your settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'Blogsters.settings'

# 3. Import the Django WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
