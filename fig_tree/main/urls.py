"""
The `main.urls` module defines the primary website URL configuration.
The table below outlines routing patterns different URL endpoints.
Further traffic routing is handled internally by each application to route specific URLs to individual pages.

| URL Pattern  | Application                  | Namespace       |
|--------------|------------------------------|-----------------|
| ``admin/``   | ``apps.admin``               | ``admin``       |
| ``auth/``    | ``apps.authentication``      | ``auth``        |
| ``api/``     | ``apps.gen_rest_api``        | ``gen_rest_api``|
| ``signup/``  | ``apps.signup``              | ``signup``      |

"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('api/', include('apps.gen_rest_api.urls', namespace='gen_rest_api')),
    path('signup/', include('apps.signup.urls', namespace='signup')),
]