import mimetypes

from tastypie.fields import CharField

mimetypes.init()


class MimeTypeField(CharField):
    """
    Read only Mime type.

    Covers ``models.ImageField`` and ``models.FileField``.
    """
    help_text = 'Mime type. Ex: "image/png"'

    def __init__(self, *args, **kwargs):
        kwargs.pop('readonly', None)
        kwargs.pop('null', None)
        super(MimeTypeField, self).__init__(*args, readonly=True, null=True, **kwargs)

    def convert(self, value):
        if value is None:
            return None

        try:
            return mimetypes.guess_type(value.path)[0]
        except AttributeError:
            return None
