======================
Django Tastypie extras
======================

.. image:: https://codeclimate.com/github/tomi77/django-tastypie-extras/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-tastypie-extras
   :alt: Code Climate


A set of Django Tastypie extras.

Resources
=========

MultipartResourceMixin
----------------------

Resource with upload image possibility

Paginator
=========

SmartPaginator
--------------

``SmartPaginator`` does not perform ``SELECT COUNT(*)`` when ``limit`` is 0 and ``offset`` is 0.
