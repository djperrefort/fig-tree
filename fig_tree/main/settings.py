"""Top level Django application settings."""

import sys
from datetime import timedelta
from pathlib import Path

import environ
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup runtime environment

env = environ.Env()
sys.path.insert(0, str(BASE_DIR))

# Debug

DEBUG = env.bool('DEBUG', default=False)
if DEBUG:
    # If running in debug mode, save emails to disk instead of sending them
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = env.path('EMAIL_FILE_PATH', default=BASE_DIR.parent / 'email')

# Security and TLS

SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=False)
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=False)

SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = SECURE_HSTS_SECONDS > 0

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
    'apps.admin_utils',
    'apps.authentication',
    'apps.error_pages',
    'apps.gen_data',
    'apps.signup',
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
    'hide_apps': ['sites'],
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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if env.str('POSTGRES_DB', False):
    _ENGINE = 'django.db.backends.postgresql'

else:
    _ENGINE = 'django.db.backends.sqlite3'

DATABASES = {
    'default': {
        "ENGINE": _ENGINE,
        "NAME": env.str('POSTGRES_DB', BASE_DIR / 'fig_tree.db'),
        "USER": env.str('POSTGRES_USER', ''),
        "PASSWORD": env.str('POSTGRES_PASSWORD', ''),
        "HOST": env.str('POSTGRES_HOST', 'localhost'),
        "PORT": env.str('POSTGRES_PORT', '5432'),
    }
}

# Password validation

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_URL = env.str('STATIC_URL', default='static/')
STATIC_ROOT = env.path('STATIC_ROOT', default=BASE_DIR / 'static_root')
