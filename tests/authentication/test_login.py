"""Function tests for the login page."""

from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

from ..test_utils import CustomTestBase, PageTitleTest

URL_REVERSE = 'auth:login'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Login'


class LoginFormBehavior(CustomTestBase, LiveServerTestCase):
    """Test the contents and behavior of the login form"""

    url_reverse = URL_REVERSE

    def setUp(self) -> None:
        """Render the page and identify form content for use in tests"""

        super().setUp()
        self.username_field = self.webdriver.find_element(By.ID, 'id_username')
        self.password_field = self.webdriver.find_element(By.ID, 'id_password')
        self.submit_btn = self.webdriver.find_element(By.ID, 'id_submit')
        self.remember_me_chkbx = self.webdriver.find_element(By.ID, 'id_remember_me')

    def test_form_fields(self) -> None:
        """Test login form fields are present on the page"""

        self.assertEqual('text', self.username_field.get_property('type'))
        self.assertEqual('password', self.password_field.get_property('type'))
        self.assertEqual('submit', self.submit_btn.get_property('type'))
        self.assertFalse(self.remember_me_chkbx.is_selected())

    def test_csrf_protection(self) -> None:
        """Test CSRF middleware token is included in the form"""

        self.webdriver.find_element(By.NAME, 'csrfmiddlewaretoken')

    def test_error_message_on_bad_login(self) -> None:
        """Test for displayed error messages on incorrect credentials"""

        self.username_field.send_keys('fake_username')
        self.password_field.send_keys('fake_password')
        self.submit_btn.click()

        alert_msg = self.webdriver.find_element(By.CSS_SELECTOR, 'div.alert strong')
        self.assertEqual('Incorrect username or password.', alert_msg.text)

    def test_redirect_on_good_login(self) -> None:
        """Test the user is redirected to the home page on correct credentials"""

        test_username = 'test_user'
        test_password = 'fooBAR123!'
        get_user_model().objects.create_user(
            username=test_username,
            email='test@user.com',
            password=test_password)

        self.username_field.send_keys(test_username)
        self.password_field.send_keys(test_password)
        self.submit_btn.click()

        home_url = self.live_server_url + reverse('home')
        self.assertEqual(home_url, self.webdriver.current_url)


class PasswordResetLinks(CustomTestBase, LiveServerTestCase):
    """Tests for the forgot/reset password links"""

    url_reverse = URL_REVERSE

    def test_forgot_password_link_target(self) -> None:
        """Test the forgot password link leads to the forgot password page"""

        forgot_password_link = self.webdriver.find_element(By.ID, 'id_forgot_password')
        forgot_password_link.click()

        expected_url = self.live_server_url + reverse('auth:password-reset')
        self.assertEqual(expected_url, self.webdriver.current_url)

    def test_signup_link_target(self) -> None:
        """Test the signup link leads to the signup page"""

        forgot_password_link = self.webdriver.find_element(By.ID, 'id_signup')
        forgot_password_link.click()

        expected_url = self.live_server_url + reverse('signup:new-user')
        self.assertEqual(expected_url, self.webdriver.current_url)
