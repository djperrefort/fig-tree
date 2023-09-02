"""Views for handling incoming HTTP requests.

The ``views`` module defines classes for handling incoming HTTP requests.
Each view class is responsible for processing of form/request data, interacting
with database models/serializers, managing application business logic, and
returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from datetime import timedelta

from django.conf import settings
from django.contrib.auth import login, views
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import AuthenticationForm

DEFAULT_REMEMBER_ME_DURATION = timedelta(days=7)


class LoginView(views.LoginView):
    """View for handling existing user authentication"""

    template_name = 'authentication/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""

        login(self.request, form.get_user())
        if form.cleaned_data['remember_me']:
            duration = getattr(settings, 'REMEMBER_ME_DURATION', DEFAULT_REMEMBER_ME_DURATION)
            self.request.session.set_expiry(duration)

        else:
            self.request.session.set_expiry(0)

        return HttpResponseRedirect(self.get_success_url())


class LogoutView(views.LogoutView):
    """View for logging out users"""

    template_name = 'authentication/logged_out.html'


class PasswordResetView(views.PasswordResetView):
    """View for requesting a reset password link via email"""

    template_name = 'authentication/password_reset_form.html'
    email_template_name = 'authentication/password_reset_email.html'
    success_url = reverse_lazy('auth:password-reset-done')


class PasswordResetDoneView(views.PasswordResetDoneView):
    """View for confirming that a reset password link has been sent via email"""

    template_name = 'authentication/password_reset_done.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    """View for resetting an existing user's password"""

    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('auth:password-reset-complete')


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    """View for confirming a user's password has been reset"""

    template_name = 'authentication/password_reset_complete.html'
