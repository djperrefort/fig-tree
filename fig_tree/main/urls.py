"""
The `main.urls` module defines the primary website URL configuration.
The table below outlines routing patterns different URL endpoints.
Further traffic routing is handled internally by each application to
route specific URLs to individual pages.

| URL Pattern | Application                | Namespace      |
|-------------|----------------------------|----------------|
| `admin/`    | `apps.admin`               | `admin`        |
| `auth/`     | `apps.authentication`      | `auth`         |
| `api/`      | `apps.gen_rest_api`        | `gen_rest_api` |
| `signup/`   | `apps.signup`              | `signup`       |

The following pages are included to support testing and development.

| URL Pattern | Description                    | Registered Name |
|-------------|--------------------------------|-----------------|
| `tests/400` | Renders a 400 HTTP error code. | `test-400`      |
| `tests/403` | Renders a 403 HTTP error code. | `test-403`      |
| `tests/404` | Renders a 404 HTTP error code. | `test-404`      |
| `tests/500` | Renders a 500 HTTP error code. | `test-500`      |
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from apps.error_pages import handlers

# Enable custom error code handling
# See the `error_pages` app for more information
handler400 = handlers.handler400
handler403 = handlers.handler403
handler404 = handlers.handler404
handler500 = handlers.handler500

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),

    # Add urls from plugins and applications
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls', namespace='auth')),
    path('api/', include('apps.gen_rest_api.urls', namespace='gen_rest_api')),
    path('signup/', include('apps.signup.urls', namespace='signup')),

    # Add dedicated error pages for testing purposes
    path('err/400', handler400, name='test-400'),
    path('err/403', handler403, name='test-403'),
    path('err/404', handler404, name='test-404'),
    path('err/500', handler500, name='test-500'),
]
