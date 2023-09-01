"""Configurable function tests that can be reused for multiple pages.

Tests provided by this module evaluate the behavior of rendered page content
using a webdriver.
"""

from time import sleep

from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class CustomTestBase:
    """Extends the UnitTest/Django testing framework with common setup tasks

    This class automatically sets up a unique webdriver instance for each test.
    The attributes below are used to instantiate the web driver.
    Set the ``url_reverse`` class attribute to configure the URL used when
    instantiating the web driver.
    """

    driver_class = webdriver.Firefox
    """The driver class (browser type) to use when testing"""

    show_webdriver = False
    """Optionally show the webdriver page in real time"""

    url_reverse: str = None
    """Initial Django URL to start the webdriver at"""

    url_reverse_kwargs: dict
    """Optional arguments to use when rendering the Django URL"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up a webdriver"""

        super().setUpClass()
        if cls.url_reverse is None:
            raise ValueError('Class attribute ``url_reverse`` cannot be None')

        if not hasattr(cls, 'url_reverse_kwargs'):
            cls.url_reverse_kwargs = dict()

        driver_class = cls.driver_class
        options = Options()
        options.headless = not cls.show_webdriver
        cls.webdriver = driver_class(options=options)

    @classmethod
    def tearDownClass(cls):
        """Tear down testing webdriver"""

        super().tearDownClass()
        cls.webdriver.close()

    def setUp(self) -> None:
        """Navigate webdriver to test url"""

        super().setUp()
        self.initial_url = self.live_server_url + reverse(self.url_reverse, kwargs=self.url_reverse_kwargs)
        self.webdriver.get(self.initial_url)


class PageTitleTest(CustomTestBase):
    """Test a page title is set to the given value"""

    page_title: str
    """The title of the page to test for"""

    def runTest(self) -> None:
        """Test the page title is set correctly"""

        self.assertEqual(self.page_title, self.webdriver.title)


class RedirectOnSuccessTest(CustomTestBase):
    """Test the user is redirected to a different page after a delay"""

    url_reverse_end: str
    """The URL a user should be redirected to"""

    redirect_delay: int
    """Wait the given number of seconds before checking the redirected URL"""

    def runTest(self):
        sleep(self.redirect_delay)  # Wait for client to be redirected
        end_url = self.live_server_url + reverse(self.url_reverse_end)
        self.assertEqual(end_url, self.webdriver.current_url)


class CorrectTemplateTest(CustomTestBase):
    """Test a URL corresponds to a given template"""

    url_name: str
    """The Django URL to test"""

    template: str
    """The path of the expected rendered template"""

    def test_get_returns_correct_template(self) -> None:
        """Test the view returns correct template"""

        url = reverse(self.url_name)
        response = self.client.get(url)

        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, self.template)
