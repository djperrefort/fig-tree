"""
The ``handlers`` module defines custom HTTP error handlers.
Request handlers are used to process the routing of HTTP errors to the correct
HTML template. Dedicated handler objects are provided for each HTTP error
supported by Django.
"""

from typing import Optional

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

app_name = 'error_pages'


def error_render(error_code: int, request: HttpRequest) -> HttpResponse:
    """Render the appropriate error template for the given error code

    Args:
        error_code: The HTTP error code to render a response for
        request: The incoming HTTP request

    Returns:
        A rendered HTTP response
    """

    try:
        template = f'{app_name}/http_{error_code}.html'
        get_template(template)

    except TemplateDoesNotExist:
        template = f'{app_name}/default.html'

    context = {
        'error_code': error_code,
        'description': settings.ERROR_CODE_DESCRIPTIONS[error_code],
        'description_long': settings.ERROR_CODE_DESCRIPTIONS_LONG[error_code]
    }

    return render(request, template, status=error_code, context=context)


def handler400(request: HttpRequest, exception: Optional[int] = None) -> HttpResponse:
    """Render a response to a 400 error"""

    return error_render(400, request)


def handler403(request: HttpRequest, exception: Optional[int] = None) -> HttpResponse:
    """Render a response to a 403 error"""

    return error_render(403, request)


def handler404(request: HttpRequest, exception: Optional[int] = None) -> HttpResponse:
    """Render a response to a 404 error"""

    return error_render(404, request)


def handler500(request: HttpRequest) -> HttpResponse:
    """Render a response to a 500 error"""

    return error_render(500, request)
