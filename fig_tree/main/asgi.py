"""
Fig-Tree exclusively supports the ASGI standard and does not provide a WSGI entrypoint.
In keeping with standard practice, the ASGI callable object is exposed as `main.asgi.application`.

## What is ASGI

Server gateways provide a standardized interface between web servers and Python applications.
The Asynchronous Server Gateway Interface (ASGI) is one such specification.
Unlike the older Web Server Gateway Interface (WSGI), ASGI natively supports asynchronous operation.

ASGI support is built directly into the Django framework used to build Fig-Tree.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fig_tree.main.settings')

application = get_asgi_application()
