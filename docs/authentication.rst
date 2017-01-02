Authentication
==============

``SwaggerApiKeyAuthentication``
-------------------------------

`SwaggerUI` provides request authentication only through ``api_key`` parameter.
``SwaggerApiKeyAuthentication`` reads `username` and `api_key` from ``api_key`` request parameter.

Usage
::

    from tastypie_extras.authentication import SwaggerApiKeyAuthentication

    class MyResource(ModelResource):
        class Meta(object):
            resource_name = 'test'
            authentication = SwaggerApiKeyAuthentication()
