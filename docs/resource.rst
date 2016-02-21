Resource
========

``MultipartResourceMixin``
--------------------------

Extends Tastypie Resource with upload image possibility.

Usage::

    class ImageResource(MultipartResourceMixin, ModelResource):
        image = FileField()

        class Meta(object):
            resource_name = 'image'
