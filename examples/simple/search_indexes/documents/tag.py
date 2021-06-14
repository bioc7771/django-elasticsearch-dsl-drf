from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from books.models import Tag
from .analyzers import html_strip


__all__ = ('TagDocument',
           'NoKeywordTagDocument')

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1,
    blocks={'read_only_allow_delete': None}
)


@INDEX.doc_type
class TagDocument(Document):
    """Elasticsearch document for a Tag."""

    # Set unique title as the document id.
    id = fields.KeywordField(attr='title')
    title = fields.KeywordField()

    class Django(object):
        """Django Elasticsearch DSL ORM Meta."""

        model = Tag

    class Meta:
        """Meta options."""

        parellel_indexing = True


@registry.register_document
class NoKeywordTagDocument(Document):
    """Elasticsearch document for a Tag."""

    id = fields.IntegerField()
    title = fields.TextField()

    class Index:
        name = "test_no_keyword_tag"
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django(object):
        """Django Elasticsearch DSL ORM Meta."""

        model = Tag

    class Meta:
        """Meta options."""

        parellel_indexing = True
