"""Function tests for the confirmation page indicating a successful password reset."""

from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

from ..utils import CustomTestBase, PageTitleTest

URL_REVERSE = 'auth:password-reset-complete'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Reset Password'


class LoginLink(CustomTestBase, LiveServerTestCase):
    """Test the direction of users to login page via the login link"""

    url_reverse = URL_REVERSE

    def test_link_target(self):
        """Test the login button links to the login page"""

        self.webdriver.find_element(By.ID, 'id_login').click()
        expected_url = self.live_server_url + reverse('auth:login')
        self.assertEqual(expected_url, self.webdriver.current_url)


class HomepageLink(CustomTestBase, LiveServerTestCase):
    """Test the direction of users to login page via the login link"""

    url_reverse = URL_REVERSE

    def test_link_target(self):
        """Test the homepage button links to the home page"""

        self.webdriver.find_element(By.ID, 'id_home').click()
        expected_url = self.live_server_url + reverse('home')
        self.assertEqual(expected_url, self.webdriver.current_url)
