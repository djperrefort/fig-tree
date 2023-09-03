"""Function tests for the logout confirmation page."""

from django.test import LiveServerTestCase

from ..test_utils import PageTitleTest, RedirectOnSuccessTest

URL_REVERSE = 'auth:logout'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Logout Successful'


class RedirectOnSuccess(RedirectOnSuccessTest, LiveServerTestCase):
    """Test the user is redirected after a delay"""

    url_reverse = URL_REVERSE
    url_reverse_end = 'home'
    redirect_delay = 4
