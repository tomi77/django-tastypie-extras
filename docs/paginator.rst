Paginator
=========

``SmartPaginator``
------------------

A paginator, that does not perform ``SELECT COUNT(*)`` when ``limit`` is 0.

Usage
::

   from tastypie_extras.paginator import SmartPaginator


   class TestResource(ModelResource):

       class Meta(object):
           resource_name = 'test'
           paginator_class = SmartPaginator
