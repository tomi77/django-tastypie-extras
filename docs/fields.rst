Fields
======

``DurationField``
-----------------

A field covering ``models.DurationField``. Serializes ``timedelta`` values to ``HH:MM:SS`` format.
Accepts interval strings on input and returns a ``timedelta`` object.

Usage
::

    from tastypie_extras.fields import DurationField

    class MyResource(ModelResource):
        duration = DurationField(attribute='duration')
