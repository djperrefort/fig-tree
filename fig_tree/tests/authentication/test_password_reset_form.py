"""Function tests for users requesting a password reset link."""

from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

from ..utils import CustomTestBase, PageTitleTest

URL_REVERSE = 'auth:password-reset'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Reset Password'


class PasswordResetForm(CustomTestBase, LiveServerTestCase):
    """Test the page is populated with the password reset request form"""

    url_reverse = URL_REVERSE

    def setUp(self) -> None:
        """Locate form elements in the webpage"""

        super().setUp()
        self.email_field = self.webdriver.find_element(By.ID, 'id_email')
        self.submit_btn = self.webdriver.find_element(By.ID, 'id_submit')

    def test_csrf_protection(self) -> None:
        """Test CSRF middleware token is included in the form"""

        self.webdriver.find_element(By.NAME, 'csrfmiddlewaretoken')

    def test_form_fields(self) -> None:
        """Test form fields are present on the page"""

        self.assertEqual('email', self.email_field.get_property('type'))
        self.assertEqual('name@domain.com', self.email_field.get_property('placeholder'))

        self.assertEqual('submit', self.submit_btn.get_property('type'))

    def test_form_submit_blank(self) -> None:
        """Test form behavior on a blank entry"""

        # Check there is no redirect for empty form
        self.submit_btn.click()
        self.assertEqual(self.initial_url, self.webdriver.current_url)

        alert_msg = self.webdriver.find_element(By.CLASS_NAME, 'alert')
        self.assertEqual('This field is required.', alert_msg.text)

    def test_form_submit_invalid_email(self) -> None:
        """Test form behavior on an invalid email address"""

        # Check there is no redirect for invalid email
        self.email_field.send_keys('notanemail')
        self.submit_btn.click()
        self.assertEqual(self.initial_url, self.webdriver.current_url)

        alert_msg = self.webdriver.find_element(By.CLASS_NAME, 'alert')
        self.assertEqual('Enter a valid email address.', alert_msg.text)

    def test_form_submit_valid(self) -> None:
        """Test form behavior on a valid email address"""

        self.email_field.send_keys('fake@email.com')
        self.submit_btn.click()

        target_url = self.live_server_url + reverse('auth:password-reset-done')
        self.assertEqual(target_url, self.webdriver.current_url)
