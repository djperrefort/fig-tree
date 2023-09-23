from django.test import LiveServerTestCase

from ..test_utils import PageTitleTest


class Test400(PageTitleTest, LiveServerTestCase):
    url_reverse = 'test-400'
    page_title = '400 Error'


class Test403(PageTitleTest, LiveServerTestCase):
    url_reverse = 'test-403'
    page_title = '403 Error'


class Test404(PageTitleTest, LiveServerTestCase):
    url_reverse = 'test-404'
    page_title = '404 Error'


class Test500(PageTitleTest, LiveServerTestCase):
    url_reverse = 'test-500'
    page_title = '500 Error'
