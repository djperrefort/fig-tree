"""Function tests for the logout confirmation page."""

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from ..test_utils import PageTitleTest, RedirectOnSuccessTest

URL_REVERSE = 'auth:logout'


class PageTitle(PageTitleTest, StaticLiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Logout Successful'


class RedirectOnSuccess(RedirectOnSuccessTest, StaticLiveServerTestCase):
    """Test the user is redirected after a delay"""

    url_reverse = URL_REVERSE
    url_reverse_end = 'home'
    redirect_delay = 4
