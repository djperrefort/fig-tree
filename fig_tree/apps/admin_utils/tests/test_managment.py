"""Tests for custom management commands."""

from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase


class Quickstart(TestCase):
    """Test the `quickstart` command"""

    def test_uvicorn_command(self):
        """Test the `--uvicorn` option deploys a Uvicorn server"""

        with patch('subprocess.run') as mock_run:
            call_command('quickstart', '--uvicorn', '--no-input')
            mock_run.assert_called_with(
                ['uvicorn', 'fig_tree.main.asgi:application', '--host', '0.0.0.0', '--port', '8000'], check=True)
