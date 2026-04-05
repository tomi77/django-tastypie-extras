import re
from datetime import timedelta

from t77_date.constants import INTERVAL_REGEX_STR
from tastypie.exceptions import ApiFieldError
from tastypie.fields import ApiField

INTERVAL_REGEX = re.compile(INTERVAL_REGEX_STR)


class DurationField(ApiField):
    """
    An duration field.

    Covers ``models.DurationField``.
    """
    dehydrated_type = 'timedelta'
    help_text = 'Time interval'

    def _parse(self, value):
        if isinstance(value, str):
            match = INTERVAL_REGEX.search(value)

            if match:
                data = match.groupdict()
                return timedelta(**dict((key, int(data[key] or 0)) for key in data))

        return value

    def convert(self, value):
        if value is None:
            return None

        if isinstance(value, str):
            match = INTERVAL_REGEX.search(value)

            if match:
                data = match.groupdict()
                value = timedelta(**dict((key, int(data[key] or 0)) for key in data))
            else:
                raise ApiFieldError(f"Timedelta provided to '{self.instance_name}' field doesn't appear to be a valid timedelta string: '{value}'")

        if isinstance(value, timedelta):
            hours, remainder = divmod(value.seconds, 3600)
            hours += value.days * 24
            minutes, seconds = divmod(remainder, 60)
            return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        return value

    def hydrate(self, bundle):
        value = super().hydrate(bundle)

        if value and not hasattr(value, 'days'):
            value = self._parse(value)

        return value
