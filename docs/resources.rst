Resources
=========

``MultipartResourceMixin``
--------------------------

Extends Tastypie Resource with upload image possibility.

Usage
::

    class ImageResource(MultipartResourceMixin, ModelResource):
        image = FileField()

        class Meta(object):
            resource_name = 'image'

``ReadOnlyResourceMixin``
-------------------------

Raise `BadRequest` on `update`, `create` or `delete` request.

Usage
::

    class MyResource(ReadOnlyResourceMixin, ModelResource):
      class Meta(object):
          resource_name = 'my_resource'
