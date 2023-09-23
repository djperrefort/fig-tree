"""Tests for HTTP error pages."""

from django.test import LiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By

from ..test_utils import CustomTestBase


class ErrorPageTestBase(CustomTestBase):
    """Common tests for all HTTP error pages"""

    url_reverse: str  # Reverse lookup name for the error page
    page_title: str  # Expected page title

    def test_home_button(self) -> None:
        """Test the home button takes users to the home page"""

        self.webdriver.find_element(By.ID, 'id_home').click()
        expected_url = self.live_server_url + reverse('home')
        self.assertEqual(expected_url, self.webdriver.current_url)

    def test_page_title(self) -> None:
        """Test the page title matches the expected value"""

        self.assertEqual(self.page_title, self.webdriver.title)


class Test400(ErrorPageTestBase, LiveServerTestCase):
    """Test the HTTP 400 error page"""

    url_reverse = 'test-400'
    page_title = '400 Error'


class Test403(ErrorPageTestBase, LiveServerTestCase):
    """Test the HTTP 403 error page"""

    url_reverse = 'test-403'
    page_title = '403 Error'


class Test404(ErrorPageTestBase, LiveServerTestCase):
    """Test the HTTP 404 error page"""

    url_reverse = 'test-404'
    page_title = '404 Error'


class Test500(ErrorPageTestBase, LiveServerTestCase):
    """Test the HTTP 500 error page"""

    url_reverse = 'test-500'
    page_title = '500 Error'
