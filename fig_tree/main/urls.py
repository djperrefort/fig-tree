"""The primary website URL configuration. This module defines how different
URL patterns are routed to different backend applications. Further traffic
routing is handled internally by each application to route specific URLs to
individual pages.

URL Routing Configuration
-------------------------

+----------------------+----------------------------+-------------------------+
| URL Pattern          | Application                | Namespace               |
+======================+============================+=========================+
| ``admin/``           | ``apps.admin``             | ``admin``               |
+----------------------+----------------------------+-------------------------+
| ``api/``             | ``apps.data_api``          | ``data_api``            |
+----------------------+----------------------------+-------------------------+
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.data_api.urls', namespace='data_api')),
    path('signup/', include('apps.signup.urls', namespace='signup')),
]
