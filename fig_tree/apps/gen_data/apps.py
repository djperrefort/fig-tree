"""
The ``apps`` module defines application level settings and post-initialization
setup tasks. This includes configuring the application name, database
initialization, and signal handling.
"""

from django.apps import AppConfig


class Config(AppConfig):
    """Application settings and configuration"""

    name = 'apps.gen_data'
    verbose_name = "Genealogical Data"
