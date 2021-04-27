"""
Integrate Elasticsearch DSL with Django REST framework.
"""

__title__ = 'django-elasticsearch-dsl-drf'
__version__ = '0.22'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2017-2020 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('default_app_config',)

if django.VERSION < (3, 2):
    default_app_config = 'django_elasticsearch_dsl_drf.apps.Config'
