"""Function tests for the logout confirmation page."""

from time import sleep

from django.test import LiveServerTestCase
from django.urls import reverse

from ..utils import PageTitleTest, CustomTestBase

URL_REVERSE = 'auth:logout'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Logout Successful'


class RedirectOnSuccess(CustomTestBase, LiveServerTestCase):
    """Test the user is redirected after a delay"""

    url_reverse = URL_REVERSE
    url_reverse_end = 'home'
    redirect_delay = 4

    def runTest(self):
        """Test the user is redirected"""

        sleep(self.redirect_delay)  # Wait for client to be redirected
        end_url = self.live_server_url + reverse(self.url_reverse_end)
        self.assertEqual(end_url, self.webdriver.current_url)
