"""Top level Django application settings."""

import os
import sys
from datetime import timedelta
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup runtime environment
sys.path.insert(0, str(BASE_DIR))
load_dotenv()

# Security and authentication settings
DEBUG = os.environ.get('DEBUG', default='0') != '0'
SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="localhost 127.0.0.1").split(" ")

# If running in debug mode, save emails to disk instead of sending them
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = Path(os.environ.get('EMAIL_FILE_PATH', BASE_DIR.parent / 'email'))

# Application Configuration

ROOT_URLCONF = 'main.urls'
SITE_ID = 1

AUTH_USER_MODEL = 'signup.AuthUser'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'auth:login'
REMEMBER_ME_DURATION = timedelta(days=7)

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_bootstrap5',
    'rest_framework',
    'widget_tweaks',
    'apps.family_trees',
    'apps.authentication',
    'apps.gen_data',
    'apps.signup',
    'apps.error_pages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Base settings for the Admin UI theme

JAZZMIN_SETTINGS = {
    'site_title': 'Fig-Tree Admin',
    'site_header': 'Fig Tree',
    'site_brand': 'Fig Tree',
    'related_modal_active': True,
    'order_with_respect_to': [
        'signup',
        'family_trees',
        'gen_data',
    ],
    'icons': {
        'sites.Site': 'fa fa-globe'
    },
    'hide_apps' : ['sites'],
    "changeform_format": "single",
    "changeform_format_overrides": dict(),
}

# Global REST API Settings

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


_driver = os.environ.get('DB_DRIVER', 'sqlite3')
_name = BASE_DIR / 'fig_tree.sqlite3' if _driver == 'sqlite3' else 'fig_tree'
DATABASES = {
    'default': {
        "ENGINE": f'django.db.backends.{_driver}',
        "NAME": os.environ.get('DB_NAME', _name),
        "USER": os.environ.get('DB_USER', ''),
        "PASSWORD": os.environ.get('DB_PASSWORD', ''),
        "HOST": os.environ.get('DB_HOST', 'localhost'),
        "PORT": os.environ.get('DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 12, }
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = os.environ.get('STATIC_URL', 'static/')
STATIC_ROOT = Path(os.environ.get('STATIC_ROOT', Path.cwd() / 'static_root'))
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
