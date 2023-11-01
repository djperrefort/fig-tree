"""
The `urls` module maps URL endpoints to django views defined in the parent
application. For root level URL routing, see the project level `urls` module.
View objects can be found in the `views` module.

# URL Routing Configuration

| URL                      | View                   | Name              |
|--------------------------|------------------------|-------------------|
| `/`                      | `SignUpView`           | `new-user`        |
| `act_sent/`              | `activation_sent_view` | `activation-sent` |
| `[AUTHENTICATION-TOKEN]` | `ActivateAccountView`  | `activate`        |
"""

from django.urls import path, re_path

from .views import *

app_name = 'signup'

token_regex = r'(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,50})'

urlpatterns = [
    path('', SignUpView.as_view(), name='new-user'),
    path('sent', ActivationSentView.as_view(), name='activation-sent'),
    re_path(token_regex, ActivateAccountView.as_view(), name='activate'),
]
