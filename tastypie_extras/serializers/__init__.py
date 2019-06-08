"""
Tastypie serializer
"""
from tastypie.serializers import Serializer as BaseSerializer

from .csv import CSVSerializerMixin


class Serializer(BaseSerializer, CSVSerializerMixin):
    """
    Tastypie serializer with new formats
    """
    formats = BaseSerializer.formats + CSVSerializerMixin.formats

    content_types = dict(BaseSerializer.content_types.items() +
                         CSVSerializerMixin.content_types.items())
