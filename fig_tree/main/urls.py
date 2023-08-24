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
| ``auth/``            | ``apps.authentication``    | ``auth``                |
+----------------------+----------------------------+-------------------------+
| ``api/``             | ``apps.data_api``          | ``data_api``            |
+----------------------+----------------------------+-------------------------+
| ``signup/``          | ``apps.signup``            | ``signup``              |
+----------------------+----------------------------+-------------------------+
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('api/', include('apps.data_api.urls', namespace='data_api')),
    path('signup/', include('apps.signup.urls', namespace='signup')),
]
