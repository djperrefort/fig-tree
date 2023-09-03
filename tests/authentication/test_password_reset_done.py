"""Function tests for the confirmation page indicating a password reset
link has been sent via email.
"""

from django.test import LiveServerTestCase

from ..test_utils import PageTitleTest

URL_REVERSE = 'auth:password-reset-done'


class PageTitle(PageTitleTest, LiveServerTestCase):
    """Test the page title is correctly set"""

    url_reverse = URL_REVERSE
    page_title = 'Reset Password'
