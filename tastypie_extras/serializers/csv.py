from collections import OrderedDict
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import smart_str
from django.utils.text import get_valid_filename
from django_extras.http import HttpResponseGetFile
try:
    from unicodecsv import DictReader, DictWriter
except ImportError:
    UnicodeReader, UnicodeWriter = None, None


class CSVSerializerMixin(object):
    formats = ['csv']

    content_types = {'csv': 'text/csv'}

    def to_csv(self, data, options=None):
        if UnicodeWriter is None:
            raise ImproperlyConfigured(
                "Usage of the CSV aspects requires unicodecsv.")

        options = options or {}
        data = self.to_simple(data, options)
        filename = smart_str(get_valid_filename(options.get('filename',
                                                            'data.csv')))
        response = HttpResponseGetFile(filename=filename,
                                       mimetype='application/octet-stream')

        if data.get('objects') and len(data.get('objects')) > 0:
            header = dict([(x, x) for x in data.get('objects')[0].keys()])
            field_names = header.keys()
            writer = DictWriter(response, fieldnames=field_names,
                                delimiter=';')

            writer.writerow(header)

            for item in data.get('objects'):
                row = OrderedDict()
                for field_name in field_names:
                    row.update({field_name: item.get(field_name)})
                writer.writerow(row)

        return response

    def from_csv(self, content):
        if UnicodeReader is None:
            raise ImproperlyConfigured(
                "Usage of the CSV aspects requires unicodecsv.")

        # Untested, so this might not work exactly right.
        data = [item for item in DictReader(StringIO(content))]

        return data
