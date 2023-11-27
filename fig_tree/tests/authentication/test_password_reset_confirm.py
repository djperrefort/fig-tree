"""Function tests for users specifying a new password using a password reset link."""

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.test import LiveServerTestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from selenium.webdriver.common.by import By

from ..utils import CustomTestBase

URL_REVERSE = 'auth:password-reset-confirm'
URL_REVERSE_KWARGS = dict(uidb64='MQ', token='b0eoao-12ccb812deafbe6e742fdd536108ee53')


class InvalidOrExpiredLink(CustomTestBase, LiveServerTestCase):
    """Test page behavior for an invalid or expired password reset link"""

    url_reverse = URL_REVERSE
    url_reverse_kwargs = URL_REVERSE_KWARGS

    def test_page_title(self) -> None:
        """Test the page title"""

        self.assertEqual('Reset Password', self.webdriver.title)

    def test_try_again_link(self):
        """Test the "try again" link leads to the password reset page"""

        self.webdriver.find_element(By.ID, 'id_try_again').click()
        expected_url = self.live_server_url + reverse('auth:password-reset')
        self.assertEqual(expected_url, self.webdriver.current_url)


class ValidResetLink(CustomTestBase, LiveServerTestCase):
    """Test page behavior for a valid password reset link"""

    url_reverse = URL_REVERSE

    def setUp(self) -> None:
        """Render the webpage and identify key page elements"""

        # Update render arguments so the webdriver has a valid password reset token
        token, uidb64 = self.create_temporary_reset_token()
        self.url_reverse_kwargs['uidb64'] = uidb64
        self.url_reverse_kwargs['token'] = token
        super().setUp()

        self.new_password1 = self.webdriver.find_element(By.ID, 'id_new_password1')
        self.new_password2 = self.webdriver.find_element(By.ID, 'id_new_password2')
        self.submit_btn = self.webdriver.find_element(By.ID, 'id_submit_btn')

    @staticmethod
    def create_temporary_reset_token() -> tuple[str, str]:
        """Create a temporary password reset token used to build the page url

        Token is valid for only a single call from the webdriver and cannot
        be reused between tests.

        Return:
            The base64 encoded ID of a mock user
            The reset token for the mock user
        """

        test_username = 'test_user'
        test_password = 'fooBAR123!'
        user = get_user_model().objects.create_user(
            username=test_username,
            email='test@user.com',
            password=test_password)

        generator = PasswordResetTokenGenerator()
        uidb64 = urlsafe_base64_encode(force_bytes(str(user.pk)))
        token = generator.make_token(user)
        return token, uidb64

    def test_page_title(self) -> None:
        """Test the page title"""

        self.assertEqual('Reset Password', self.webdriver.title)

    def test_csrf_protection(self) -> None:
        """Test CSRF middleware token is included in the form"""

        self.webdriver.find_element(By.NAME, 'csrfmiddlewaretoken')

    def test_form_content(self) -> None:
        """Test form elements are populated on the webpage"""

        self.assertEqual('password', self.new_password1.get_property('type'))
        self.assertEqual('password', self.new_password2.get_property('type'))
        self.assertEqual('submit', self.submit_btn.get_property('type'))

    def test_error_on_common_password(self) -> None:
        """Test an error message is displayed for a common password"""

        self.new_password1.send_keys('password1234')
        self.new_password2.send_keys('password1234')
        self.submit_btn.click()

        error = self.webdriver.find_element(By.ID, 'id_password_error')
        self.assertEqual('This password is too common.', error.text)

    def test_error_on_short_password(self) -> None:
        """Test an error message is displayed for a short password"""

        self.new_password1.send_keys('a7d4ht!sdf')
        self.new_password2.send_keys('a7d4ht!sdf')
        self.submit_btn.click()

        error = self.webdriver.find_element(By.ID, 'id_password_error')
        self.assertRegex(error.text, r'This password is too short. It must contain at least \d* characters.')

    def test_error_message_on_mismatch_password(self) -> None:
        """Test an error message is displayed for mismatching passwords"""

        self.new_password1.send_keys('password_foo')
        self.new_password2.send_keys('password_bar')
        self.submit_btn.click()

        error = self.webdriver.find_element(By.ID, 'id_password_error')
        self.assertEqual(error.text, "The two password fields didn't match.")

    def test_redirect_on_valid_password(self) -> None:
        """Test page redirect on valid password"""

        valid_password = 'abcdABCD1234!@#$'
        self.new_password1.send_keys(valid_password)
        self.new_password2.send_keys(valid_password)
        self.submit_btn.click()

        expected_url = self.live_server_url + reverse('auth:password-reset-complete')
        self.assertEqual(expected_url, self.webdriver.current_url)
