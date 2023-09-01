"""Tests for the ``ActivateAccountView`` class"""

from django.test import Client, TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.signup import models, urls, views


class TokenHandling(TestCase):
    """Test the handling of (in)valid tokens"""

    url_name = f'{urls.app_name}:activate'
    invalid_token_template = 'signup/invalid_activation_link.html'
    valid_token_template = 'signup/activation_success.html'

    def setUp(self) -> None:
        """Generate a test user and a corresponding authentication token"""

        # Create client and test user
        self.client = Client()
        self.test_user = models.AuthUser(pk=1)
        self.test_user.save()

        # Create activation token for custom user
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.test_user.pk))
        self.test_token = views.activation_token_generator.make_token(self.test_user)

    def test_invalid_token_template(self) -> None:
        """Test get request with invalid token redirects to invalid token page"""

        bad_signup_token = {'uidb64': 'AB', 'token': 'CDE-FGHIJK'}
        url = reverse(self.url_name, kwargs=bad_signup_token)
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.invalid_token_template)

    def test_valid_token_template(self) -> None:
        """Test get request with invalid token redirects to success page"""

        good_signup_token = {'uidb64': self.uidb64, 'token': self.test_token}
        url = reverse(self.url_name, kwargs=good_signup_token)
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.valid_token_template)
