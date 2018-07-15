from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AddressDocumentViewSet,
    AuthorDocumentViewSet,
    BookDocumentViewSet,
    BookOrderingByScoreDocumentViewSet,
    BookCompoundSearchBackendDocumentViewSet,
    BookFunctionalSuggesterDocumentViewSet,
    BookMoreLikeThisDocumentViewSet,
    BookDefaultFilterLookupDocumentViewSet,
    CityDocumentViewSet,
    CityCompoundSearchBackendDocumentViewSet,
    PublisherDocumentViewSet,
)

__all__ = ('urlpatterns',)

router = DefaultRouter()

addresses = router.register(
    r'addresses',
    AddressDocumentViewSet,
    base_name='addressdocument'
)

authors = router.register(
    r'authors',
    AuthorDocumentViewSet,
    base_name='authordocument'
)

books = router.register(
    r'books',
    BookDocumentViewSet,
    base_name='bookdocument'
)

books_ordered_by_score = router.register(
    r'books-ordered-by-score',
    BookOrderingByScoreDocumentViewSet,
    base_name='bookdocument_ordered_by_score'
)

books_functional_suggester = router.register(
    r'books-functional-suggester',
    BookFunctionalSuggesterDocumentViewSet,
    base_name='bookdocument_functional_suggester'
)

books_more_like_this = router.register(
    r'books-more-like-this',
    BookMoreLikeThisDocumentViewSet,
    base_name='bookdocument_more_like_this'
)

books_default_filter_lookup = router.register(
    r'books-default-filter-lookup',
    BookDefaultFilterLookupDocumentViewSet,
    base_name='bookdocument_default_filter_lookup'
)

books_compound_search_backend = router.register(
    r'books-compound-search-backend',
    BookCompoundSearchBackendDocumentViewSet,
    base_name='bookdocument_compound_search_backend'
)

cities = router.register(
    r'cities',
    CityDocumentViewSet,
    base_name='citydocument'
)

cities_compound_search_backend = router.register(
    r'cities-compound-search-backend',
    CityCompoundSearchBackendDocumentViewSet,
    base_name='citydocument_compound_search_backend'
)

publishers = router.register(
    r'publishers',
    PublisherDocumentViewSet,
    base_name='publisherdocument'
)

urlpatterns = [
    url(r'^', include(router.urls)),
]
