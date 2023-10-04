"""Function tests for the user signup page"""

from django.contrib.auth import get_user_model
from django.core import mail
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

from ..utils import CustomTestBase, PageTitleTest

URL_REVERSE = 'signup:new-user'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Sign Up'


class SignupFormBehavior(CustomTestBase, LiveServerTestCase):
    """Test the contents and behavior of the signup form"""

    url_reverse = URL_REVERSE

    def setUp(self) -> None:
        """Render the page and identify form content for use in tests"""

        super().setUp()
        self.username_field = self.webdriver.find_element(By.ID, 'id_username')
        self.email_field = self.webdriver.find_element(By.ID, 'id_email')
        self.password_field = self.webdriver.find_element(By.ID, 'id_password1')
        self.password_confirm_field = self.webdriver.find_element(By.ID, 'id_password2')
        self.submit_btn = self.webdriver.find_element(By.ID, 'id_submit')

    def submit_valid_form(self):
        """Helper function for submitting valid form content"""

        self.username_field.send_keys('this_is_my_username')
        self.email_field.send_keys('user@test.com')
        self.password_field.send_keys('asd!u93o28u@')
        self.password_confirm_field.send_keys('asd!u93o28u@')
        self.submit_btn.click()

    def test_csrf_protection(self) -> None:
        """Test CSRF middleware token is included in the form"""

        self.webdriver.find_element(By.NAME, 'csrfmiddlewaretoken')

    def test_field_types(self) -> None:
        """Test form fields are the correct types"""

        # Make sure fields are the correct type
        self.assertEqual('text', self.username_field.get_property('type'))
        self.assertEqual('email', self.email_field.get_property('type'))
        self.assertEqual('password', self.password_field.get_property('type'))
        self.assertEqual('password', self.password_confirm_field.get_property('type'))

    def test_error_message_on_bad_email(self) -> None:
        """Test for displayed error messages on an invalid email"""

        raise NotImplementedError()

    def test_error_message_on_bad_password(self) -> None:
        """Test for displayed error messages on an invalid password"""

        raise NotImplementedError()

    def test_error_message_on_existing_user(self) -> None:
        """Test for displayed error messages on an invalid email"""

        raise NotImplementedError()

    def test_user_redirect(self) -> None:
        """Test the user is redirected to the confirmation page"""

        self.submit_valid_form()
        expected_url = self.live_server_url + reverse('signup:activation-sent')
        self.assertEqual(expected_url, self.webdriver.current_url)

    def test_user_is_created(self) -> None:
        """Test a new user account is created following a valid form submission"""

        self.submit_valid_form()
        user = get_user_model().objects.get(username='this_is_my_username')
        self.assertFalse(user.is_active)


class SignUpEmail(CustomTestBase, LiveServerTestCase):
    """Test the contents of sign up validation emails"""

    url_reverse = URL_REVERSE

    def setUp(self) -> None:
        super().setUp()
        self.webdriver.find_element(By.ID, 'id_username').send_keys('this_is_my_username')
        self.webdriver.find_element(By.ID, 'id_email').send_keys('user@test.com')
        self.webdriver.find_element(By.ID, 'id_password1').send_keys('asd!u93o28u@')
        self.webdriver.find_element(By.ID, 'id_password2').send_keys('asd!u93o28u@')
        self.webdriver.find_element(By.ID, 'id_submit').click()

    def test_email_subject(self) -> None:
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New account activation')

    def test_email_link(self) -> None:
        raise NotImplementedError
