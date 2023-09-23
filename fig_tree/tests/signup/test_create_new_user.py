"""Function tests for the user signup page"""

from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By

from ..test_utils import CustomTestBase, PageTitleTest

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

    def test_field_types(self) -> None:
        """Test form fields are the correct types"""

        # Make sure fields are the correct type
        self.assertEqual('text', self.username_field.get_property('type'))
        self.assertEqual('email', self.email_field.get_property('type'))
        self.assertEqual('password', self.password_field.get_property('type'))
        self.assertEqual('password', self.password_confirm_field.get_property('type'))

    def test_csrf_protection(self) -> None:
        """Test CSRF middleware token is included in the form"""

        self.webdriver.find_element(By.NAME, 'csrfmiddlewaretoken')

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

        raise NotImplementedError()

    def test_user_notified(self) -> None:
        """Test the new user is sent a confirmation email"""

        raise NotImplementedError()

    def test_user_is_created(self) -> None:
        """Test a new user account is created for a valid form submission"""

        raise NotImplementedError()
