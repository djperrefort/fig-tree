"""
A simple management command for quickly migrating/deploying a development server.

## Arguments

| Argument   | Description                                                      |
|------------|------------------------------------------------------------------|
| --static   | Collect static files                                             |
| --migrate  | Run database migrations                                          |
| --celery   | Launch a Celery worker with a Redis backend                      |
| --gunicorn | Run a web server using Gunicorn                                  |
| --host     | The web server port [default: 0.0.0.0]                           |
| --port     | The web server port [default: 8000]                              |
| --no-input | Do not prompt for user input of any kind                         |
"""

import subprocess
from argparse import ArgumentParser

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """A helper utility that wraps common Django deployment tasks"""

    help = 'A helper utility for common deployment tasks'

    def add_arguments(self, parser: ArgumentParser) -> None:
        """Define command-line arguments

        Args:
          parser: The parser instance to add arguments under
        """

        parser.add_argument('--static', action='store_true', help='Collect static files.')
        parser.add_argument('--migrate', action='store_true', help='Run database migrations.')
        parser.add_argument('--uvicorn', action='store_true', help='Run a web server using Uvicorn.')
        parser.add_argument('--host', default='0.0.0.0', help='The web server host [default: 0.0.0.0].')
        parser.add_argument('--port', default=8000, type=int, help='The web server port [default: 8000].')
        parser.add_argument('--no-input', action='store_true', help='Do not prompt for user input of any kind.')

    def handle(self, *args, **options) -> None:
        """Handle the command execution.

        Args:
          *args: Additional positional arguments.
          **options: Additional keyword arguments.
        """

        if options['static']:
            self.stdout.write(self.style.SUCCESS('Collecting static files...'))
            call_command('collectstatic', no_input=not options['no_input'])

        if options['migrate']:
            self.stdout.write(self.style.SUCCESS('Running database migrations...'))
            call_command('migrate', no_input=not options['no_input'])

        if options['uvicorn']:
            self.stdout.write(self.style.SUCCESS('Starting Uvicorn server...'))
            self.run_uvicorn(host=options['host'], port=options['port'])

        else:
            self.stdout.write(self.style.SUCCESS('Starting default server...'))
            call_command('runserver', addrport=f'{options["host"]}:{options["port"]}')

    @staticmethod
    def run_uvicorn(host: str, port: int) -> None:
        """Start a Uvicorn server.

        Args:
          host: The host to bind to
          port: The port to bind to
        """

        command = ['uvicorn', 'fig_tree.main.asgi:application', '--host', host, '--port', str(port)]
        subprocess.run(command, check=True)
