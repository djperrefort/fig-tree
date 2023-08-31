"""Tests for the ``LoginView`` class"""

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import RequestFactory

from apps.authentication.forms import AuthenticationForm
from apps.authentication.views import LoginView


class FormValid(TestCase):
    """Test the handling of a valid form submission"""

    def generic_setup(self, remember_me: bool) -> tuple[AuthenticationForm, LoginView]:
        """Create instances of the login form and view"""

        # Create a mock user
        username = 'test_user'
        password = 'fooBAR123!'
        user = get_user_model().objects.create_user(
            username=username, email='test@user.com', password=password)

        # Create a mock get request
        request = RequestFactory().get('')
        request.session = self.client.session
        request.user = user

        form = AuthenticationForm(data=dict(username=username, password=password, remember_me=remember_me))
        self.assertTrue(form.is_valid())  # If the form is invalid, the tests will be inaccurate

        view = LoginView()
        view.request = request
        return form, view

    def test_session_duration_remember_me_true(self) -> None:
        """Test the setting of the session duration when ``remember_me`` is set to ``True``"""

        form, view = self.generic_setup(remember_me=True)
        response = view.form_valid(form)
        session = view.request.session

        self.assertEqual(view.get_success_url(), response.url)
        self.assertFalse(session.get_expire_at_browser_close())
        self.assertAlmostEqual(settings.REMEMBER_ME_DURATION.total_seconds(), session.get_expiry_age(), places=-1)

    def test_session_duration_remember_me_false(self) -> None:
        """Test the setting of the session duration when ``remember_me`` is set to ``False``"""

        form, view = self.generic_setup(remember_me=False)
        response = view.form_valid(form)
        session = view.request.session

        self.assertEqual(view.get_success_url(), response.url)
        self.assertTrue(session.get_expire_at_browser_close())
