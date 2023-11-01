"""Tests for the `SignUpView` class"""

from django.core import mail
from django.test import TestCase

from apps.signup.forms import UserCreationForm
from apps.signup.views import SignUpView


class FormValid(TestCase):
    """Test the handling of valid form submissions"""

    def test_email_sent_on_valid_form(self) -> None:
        """Test a user activation email is sent when a valid form is submitted"""

        user_email = 'test@domain.com'
        form = UserCreationForm(data=dict(
            username='username',
            email=user_email,
            password1='dummy_pass12',
            password2='dummy_pass12'
        ))
        SignUpView().form_valid(form)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [user_email])
        self.assertEqual(mail.outbox[0].subject, 'New account activation')
