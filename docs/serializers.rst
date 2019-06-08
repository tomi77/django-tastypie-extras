Serializers
===========

``Serializer``
--------------

Extend Tastypie Serializer to support new formats.

Usage
::

    from tastypie_extras.serializers import Serializer

    class MyResource(ModelResource):
        class Meta(object):
            resource_name = 'test'
            serializer = Serializer()

And use ``format=csv`` to get CSV file.

``CSVSerizlizerMixin``
----------------------

The Mixin, which extend Tastypie Serializer to support CSV.