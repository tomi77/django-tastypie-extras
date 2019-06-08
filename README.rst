======================
Django Tastypie extras
======================

.. image:: https://codeclimate.com/github/tomi77/django-tastypie-extras/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-tastypie-extras
   :alt: Code Climate


A set of Django Tastypie extras.

Table of contents
=================

* `Resources`_

  * `MultipartResourceMixin`_
  * `ReadOnlyResourceMixin`_

* `Paginator`_

  * `SmartPaginator`_

* `Authentication`_

  * `SwaggerApiKeyAuthentication`_

* `Fields`_

  * `MimeTypeField`_

Resources
=========

MultipartResourceMixin
----------------------

Resource with upload image possibility

ReadOnlyResourceMixin
---------------------

Raise `BadRequest` on `update`, `create` or `delete` request.

Paginator
=========

SmartPaginator
--------------

``SmartPaginator`` does not perform ``SELECT COUNT(*)`` when ``limit`` is 0 and ``offset`` is 0.

Authentication
==============

SwaggerApiKeyAuthentication
---------------------------

`SwaggerUI` provides request authentication only through ``api_key`` parameter.
``SwaggerApiKeyAuthentication`` reads `username` and `api_key` from ``api_key`` request parameter.

Fields
======

MimeTypeField
-------------

ReadOnly field

