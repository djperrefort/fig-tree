"""Views for handling incoming HTTP requests.

The ``views`` module defines classes for handling incoming HTTP requests.
Each view class is responsible for processing of form/request data, interacting
with database models/serializers, managing application business logic, and
returning rendered HTTP responses.

Whenever possible, generic base classes are used to implement common behavior
for HTTP request handling.
"""

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import CreateView, TemplateView, View

from .forms import UserCreationForm
from .models import AuthUser

activation_token_generator = PasswordResetTokenGenerator()


class SignUpView(CreateView):
    """View for handling new user creation requests"""

    form_class = UserCreationForm
    template_name = 'signup/create_new_user.html'
    success_url = reverse_lazy('signup:activation-sent')

    def form_valid(self, form: UserCreationForm) -> bool:
        """Creates a new user account and sends an email confirming user contact information

        This method is automatically called on POST requests after successfully
        validating data submitted in the ``form_class`` form.

        Args:
            form: The form to validate

        Return:
            Whether the form is valid
        """

        user = form.save(commit=False)
        user.save()

        current_site = Site.objects.get_current()

        email_subject = 'New account activation'
        message = render_to_string('signup/activate_account_email.html', {
            'user': user,
            'site_name': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': activation_token_generator.make_token(user)
        })

        email_address = form.cleaned_data.get('email')
        EmailMessage(email_subject, message, to=[email_address]).send()

        # The parent ``form_valid`` method redirects requests to ``self.success_url``
        return super().form_valid(form)


class ActivationSentView(TemplateView):
    """View for telling user's to check hir email for a confirmation notice"""

    template_name = "signup/activation_sent.html"


class ActivateAccountView(View):
    """View for marking accounts as active and finalizing account creation"""

    def get(self, request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
        """Handle an incoming HTTP request

        Args:
            request: Incoming HTTP request
            uidb64: Base 64 encoded user id
            token: Account authentication token

        Return:
            The outgoing HTTPResponse
        """

        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = AuthUser.objects.get(id=uid)

        # Catch all errors but explicitly list the expected ones
        except(TypeError, ValueError, OverflowError, AuthUser.DoesNotExist, Exception):
            user = None

        if user is not None and activation_token_generator.check_token(user, token):
            user.email_validated = True
            user.save()
            return render(request, 'signup/activation_success.html')

        return render(request, 'signup/invalid_activation_link.html')
