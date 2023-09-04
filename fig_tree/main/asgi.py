"""The ``asgi`` module exposes an ASGI callable named ``application`` as a
module-level variable. The callable object acts as an interface between the
external web server and the internal Python application. Unlike the older
WSGI standard, the ASGI interface supports asynchronous event handling.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fig_tree.main.settings')

application = get_asgi_application()
