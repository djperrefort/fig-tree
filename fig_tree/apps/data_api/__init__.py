"""The `data_api` application provides a comprehensive REST API for managing
genealogical data. The API is designed to facilitate the creation, retrieval,
updating, and deletion of genealogical data in a flexible manner.

Features:
  - Create, read, update, and delete individual persons, families, events, locations, and more.
  - Associate individuals with families and events to establish genealogical relationships.
  - Utilize query parameters and filters to search and retrieve specific genealogical records.
  - Support paginated responses to efficiently manage large datasets.
  - Manage event details uch as births, deaths, baptisms, and other customizable life events.
  - Implement robust validation when creating/updating records to ensure data integrity.

Installation
------------

Add the application to the ``installed_apps`` list in the package settings:

.. doctest:: python

   >>> INSTALLED_APPS = [
   ...    'apps.data_api',
   ... ]
"""
