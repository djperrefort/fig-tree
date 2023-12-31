"""
The `urls` module maps URL endpoints to django views defined in the parent
application. For root level URL routing, see the project level `urls` module.
View objects can be found in the `views` module.

# URL Routing Configuration

| URL Pattern                | View Class                  | Registered Name           |
|----------------------------|-----------------------------|---------------------------|
| `login/`                   | `LoginView`                 | `login`                   |
| `logout/`                  | `LogoutView`                | `logout`                  |
| `password_reset/`          | `PasswordResetView`         | `password-reset`          |
| `password_reset/done/`     | `PasswordResetDoneView`     | `password-reset-done`     |
| `'reset/<uidb64>/<token>/` | `PasswordResetConfirmView`  | `password-reset-confirm`  |
| `reset/done/`              | `PasswordResetCompleteView` | `password-reset-complete` |
"""

from django.urls import path

from .views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
]
