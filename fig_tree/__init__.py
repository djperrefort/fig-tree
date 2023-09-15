"""
Fig-Tree is Python based web application built using the [Django web framework](https://www.djangoproject.com/).
At a high level, the application comprises the following core components:

1. A `main` module used to define high level application settings.
2. A suite of custom applications, each implementing a particular feature or functionality.
3. A collection of templates and static files used to define the front end presentation layer.

The main module defines high-level application settings, including top level URL routing.
When a user submits an HTTP request, the request is routed to the appropriate application using the settings defined in `main`.
The application then routes the traffic to the appropriate view/template to render.
"""