"""Function tests for the signup success page."""

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.test import LiveServerTestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from selenium.webdriver.common.by import By

from ..utils import CustomTestBase

URL_REVERSE = 'signup:activate'


class InvalidLink(CustomTestBase, LiveServerTestCase):
    """Test page behavior for an invalid activation link"""

    url_reverse = URL_REVERSE

    # A syntactically correct but invalid token that is not tied to an existing user/session
    url_reverse_kwargs = dict(uidb64='MQ', token='b0eoao-12ccb812deafbe6e742fdd536108ee53')

    def test_page_title(self) -> None:
        """Test the page title"""

        self.assertEqual('Invalid Link', self.webdriver.title)

    def test_go_home_button(self) -> None:
        """Test the ``Go Home`` button takes users to the home page"""

        self.webdriver.find_element(By.ID, 'id_home').click()
        expected_url = self.live_server_url + reverse('home')
        self.assertEqual(expected_url, self.webdriver.current_url)


class ValidLink(CustomTestBase, LiveServerTestCase):
    """Test page behavior for a valid activation link"""

    url_reverse = URL_REVERSE

    # Mock user account data
    mock_username = 'test_user'
    mock_password = 'fooBAR123!'
    mock_email = 'test@user.com'

    def setUp(self) -> None:
        """Set up the webdriver using a valid activation link"""

        token, uidb64 = self.create_temporary_reset_token()
        self.url_reverse_kwargs.update(uidb64=uidb64, token=token)
        super().setUp()

    def create_temporary_reset_token(self) -> tuple[str, str]:
        """Create a temporary signup token used to build the page url

        Token is only valid for a single call from the webdriver and cannot
        be reused between tests.

        Return:
            The base64 encoded ID of a mock user
            The reset token for the mock user
        """

        user = get_user_model().objects.create_user(
            username=self.mock_username,
            email=self.mock_email,
            password=self.mock_password)

        generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(str(user.pk)))
        token = generator.make_token(user)
        return token, uidb64

    def test_page_title(self) -> None:
        """Test the page title"""

        self.assertEqual('Validation Successful', self.webdriver.title)

    def test_login_button(self) -> None:
        """Test the ``Login`` button takes users to the login page"""

        self.webdriver.find_element(By.ID, 'id_login').click()
        expected_url = self.live_server_url + reverse('auth:login')
        self.assertEqual(expected_url, self.webdriver.current_url)

    def test_user_is_activated(self) -> None:
        """Test the user account is activated after visiting the link"""

        user = get_user_model().objects.get(username=self.mock_username)
        self.assertTrue(user.is_active)
