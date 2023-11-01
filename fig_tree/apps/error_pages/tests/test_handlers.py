"""Tests for the `handlers` module."""

import inspect
from unittest import TestCase

from django.test import RequestFactory

from fig_tree.apps.error_pages import handlers
from fig_tree.apps.error_pages.handlers import error_render


class TestErrorRender(TestCase):
    """Test responses rendered by the `error_render` function"""

    def assert_returned_status_code(self, http_code: int) -> None:
        """Assert the returned page has the given error code

        Args:
            http_code: Error code to render and test for
        """

        request = RequestFactory().request()
        response = error_render(http_code, request)
        self.assertEqual(http_code, response.status_code)

    def test_400_status_code(self) -> None:
        """Test the rendered view returns a 400 status"""

        self.assert_returned_status_code(400)

    def test_403_status_code(self) -> None:
        """Test the rendered view returns a 403 status"""

        self.assert_returned_status_code(403)

    def test_404_status_code(self) -> None:
        """Test the rendered view returns a 404 status"""

        self.assert_returned_status_code(404)

    def test_500_status_code(self) -> None:
        """Test the rendered view returns a 500 status"""

        self.assert_returned_status_code(500)


class HandlerSignatures(TestCase):
    """Test handlers have compatible signatures with django"""

    @staticmethod
    def get_argument_names(func: callable) -> tuple:
        """Return a tuple of argument names taken by the given callable"""

        signature = inspect.signature(func)
        arg_names = tuple(signature.parameters.keys())
        return arg_names

    def test_4xx_errors(self) -> None:
        """Test errors 400, 403, and 404"""

        for error_code in (400, 403, 404):
            handler = getattr(handlers, f'handler{error_code}')
            arg_names = self.get_argument_names(handler)
            self.assertEqual(('request', 'exception'), arg_names)

    def test_500_error(self) -> None:
        """Test error 500"""

        handler = getattr(handlers, 'handler500')
        arg_names = self.get_argument_names(handler)
        self.assertEqual(('request',), arg_names)
