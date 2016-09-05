"""
Tastypie resource mixins
"""
from django.core.exceptions import MultipleObjectsReturned
from tastypie import http
from tastypie.exceptions import NotFound, BadRequest
from tastypie.utils.dict import dict_strip_unicode_keys


class MultipartResourceMixin(object):
    """
    Resource with upload image possibility
    """
    def deserialize(self, request, data, format=None):  # pylint: disable=I0011,W0622
        """
        Given a request, data and a format, deserializes the given data.

        If content type is `multipart` then new behaviour, else old behaviour.
        """
        content_type = format or request.META.get('CONTENT_TYPE',
                                                  'application/json')

        if content_type == 'application/x-www-form-urlencoded':
            deserialized = request.POST
        elif content_type.startswith('multipart'):
            deserialized = request.POST.copy()
            deserialized.update(request.FILES)
        else:
            deserialized = super(MultipartResourceMixin, self) \
                .deserialize(request, data, format)

        return deserialized

    def put_detail(self, request, **kwargs):
        """
        Either updates an existing resource or creates a new one with the
        provided data.
        """
        try:
            body = request.body
        except Exception:  # pylint: disable=I0011,W0703
            body = None
        deserialized = self.deserialize(request, body,
                                        format=request.META.get('CONTENT_TYPE',
                                                                'application/json'))
        deserialized = self.alter_deserialized_detail_data(request,
                                                           deserialized)
        bundle = self.build_bundle(data=dict_strip_unicode_keys(deserialized),
                                   request=request)

        try:
            updated_bundle = self.obj_update(bundle=bundle,
                                             **self.remove_api_resource_names(kwargs))

            if not self._meta.always_return_data:
                return http.HttpNoContent()
            else:
                updated_bundle = self.full_dehydrate(updated_bundle)
                updated_bundle = self.alter_detail_data_to_serialize(request,
                                                                     updated_bundle)
                return self.create_response(request, updated_bundle)
        except (NotFound, MultipleObjectsReturned):
            updated_bundle = self.obj_create(bundle=bundle,
                                             **self.remove_api_resource_names(kwargs))
            location = self.get_resource_uri(updated_bundle)

            if not self._meta.always_return_data:
                return http.HttpCreated(location=location)
            else:
                updated_bundle = self.full_dehydrate(updated_bundle)
                updated_bundle = self.alter_detail_data_to_serialize(request,
                                                                     updated_bundle)
                return self.create_response(request, updated_bundle,
                                            response_class=http.HttpCreated,
                                            location=location)

    def post_list(self, request, **kwargs):
        """
        Creates a new resource/object with the provided data.
        """
        try:
            body = request.body
        except Exception:  # pylint: disable=I0011,W0703
            body = None
        deserialized = self.deserialize(request, body,
                                        format=request.META.get('CONTENT_TYPE',
                                                                'application/json'))
        deserialized = self.alter_deserialized_detail_data(request,
                                                           deserialized)
        bundle = self.build_bundle(data=dict_strip_unicode_keys(deserialized),
                                   request=request)

        updated_bundle = self.obj_create(bundle,
                                         **self.remove_api_resource_names(kwargs))
        location = self.get_resource_uri(updated_bundle)

        if not self._meta.always_return_data:
            return http.HttpCreated(location=location)
        else:
            updated_bundle = self.full_dehydrate(updated_bundle)
            updated_bundle = self.alter_detail_data_to_serialize(request,
                                                                 updated_bundle)
            return self.create_response(request, updated_bundle,
                                        response_class=http.HttpCreated,
                                        location=location)



class ReadOnlyResourceMixin(object):
    def obj_update(self, bundle, **kwargs):
        raise BadRequest("Operation not permitted")

    def obj_create(self, bundle, **kwargs):
        raise BadRequest("Operation not permitted")

    def rollback(self, bundles):
        raise BadRequest("Operation not permitted")

    def obj_delete(self, bundle, **kwargs):
        raise BadRequest("Operation not permitted")

    def obj_delete_list(self, bundle, **kwargs):
        raise BadRequest("Operation not permitted")

    def obj_delete_list_for_update(self, bundle, **kwargs):
        raise BadRequest("Operation not permitted")
