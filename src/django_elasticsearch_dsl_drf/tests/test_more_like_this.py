# coding: utf-8
"""
Test more-like-this functionality.
"""

from __future__ import absolute_import, unicode_literals

import unittest
import logging

from django.core.management import call_command

from nine.versions import DJANGO_GTE_1_10

import pytest

from rest_framework import status

import factories

from .base import BaseRestFrameworkTestCase

if DJANGO_GTE_1_10:
    from django.urls import reverse
else:
    from django.core.urlresolvers import reverse

__title__ = 'django_elasticsearch_dsl_drf.tests.test_suggesters'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2017-2018 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TestMoreLikeThis',
)

LOGGER = logging.getLogger(__name__)


@pytest.mark.django_db
class TestMoreLikeThis(BaseRestFrameworkTestCase):
    """Test suggesters."""

    pytestmark = pytest.mark.django_db

    @classmethod
    def setUpClass(cls):
        """Set up class."""
        cls.books = []

        for book_data in factories.constants.NON_FAKER_BOOK_CONTENT:
            cls.books.append(
                factories.BookChapterFactory(
                    title=book_data['title'],
                    summary=book_data['summary'],
                    description=book_data['description'],
                )
            )

        for book_data in factories.constants.NON_FAKER_BOOK_CONTENT_OTHER:
            cls.books.append(
                factories.BookNovelFactory(
                    title=book_data['title'],
                    summary=book_data['summary'],
                    description=book_data['description'],
                )
            )

        # Alice book
        cls.books_url_1 = reverse(
            'bookdocument_more_like_this-more-like-this',
            kwargs={'id': cls.books[0].id}
        )
        # Shekley book
        cls.books_url_2 = reverse(
            'bookdocument_more_like_this-more-like-this',
            kwargs={'id': cls.books[-1].id}
        )

        call_command('search_index', '--rebuild', '-f')

    def _test_more_like_this(self, test_data, url):
        """Test more-like-this."""
        self.authenticate()
        data = {}
        response = self.client.get(
            url,
            data
        )

        # for _suggester_field, _test_cases in test_data.items():
        #
        #     for _test_case, _expected_results in _test_cases.items():
        #         # Check if response now is valid
        #         response = self.client.get(
        #             url + '?' + _suggester_field + '=' + _test_case,
        #             data
        #         )
        #         self.assertEqual(response.status_code, status.HTTP_200_OK)
        #         self.assertIn(_suggester_field, response.data)
        #         _unique_options = list(set([
        #             __o['text']
        #             for __o
        #             in response.data[_suggester_field][0]['options']
        #         ]))
        #         self.assertEqual(
        #             len(_unique_options),
        #             len(_expected_results),
        #             (_test_case, _expected_results)
        #         )
        #         self.assertEqual(
        #             sorted(_unique_options),
        #             sorted(_expected_results),
        #             (_test_case, _expected_results)
        #         )

    def test_more_like_this(self):
        """Test more-like-this."""
        # Testing publishers
        test_data = {
            'name_suggest__completion': {
                'Ad': ['Addison–Wesley', 'Adis International'],
                'Atl': ['Atlantic Books', 'Atlas Press'],
                'Boo': ['Book League of America', 'Book Works', 'Booktrope'],
            },
            'country_suggest__completion': {
                'Arm': ['Armenia'],
                'Ar': ['Armenia', 'Argentina'],
                'Bel': ['Belgium', 'Belarus'],
                'Bur': ['Burkina Faso', 'Burundi'],
                'Net': ['Netherlands'],
                'Fra': [],
            }
        }
        self._test_more_like_this(test_data, self.books_url_1)

        # Testing books
        test_data = {
            'title_suggest__completion': {
                'Aaa': ['Aaaaa Bbbb', 'Aaaaa Cccc', 'Aaaaa Dddd'],
                'Bbb': [],
            },
        }
        self._test_more_like_this(test_data, self.books_url_2)


if __name__ == '__main__':
    unittest.main()
