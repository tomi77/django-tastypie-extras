from django.core.exceptions import MultipleObjectsReturned
from tastypie import http
from tastypie.exceptions import NotFound
from tastypie.utils.dict import dict_strip_unicode_keys


class MultipartResource(object):
    def deserialize(self, request, data, format=None):
        content_type = format or request.META.get('CONTENT_TYPE', 'application/json')

        if content_type == 'application/x-www-form-urlencoded':
            deserialized = request.POST
        elif content_type.startswith('multipart'):
            deserialized = request.POST.copy()
            deserialized.update(request.FILES)
        else:
            deserialized = super(MultipartResource, self).deserialize(request, data, format)

        return deserialized

    def put_detail(self, request, **kwargs):
        try:
            body = request.body
        except Exception:
            body = None
        deserialized = self.deserialize(request, body, format=request.META.get('CONTENT_TYPE', 'application/json'))
        deserialized = self.alter_deserialized_detail_data(request, deserialized)
        bundle = self.build_bundle(data=dict_strip_unicode_keys(deserialized), request=request)

        try:
            updated_bundle = self.obj_update(bundle=bundle, **self.remove_api_resource_names(kwargs))

            if not self._meta.always_return_data:
                return http.HttpNoContent()
            else:
                updated_bundle = self.full_dehydrate(updated_bundle)
                updated_bundle = self.alter_detail_data_to_serialize(request, updated_bundle)
                return self.create_response(request, updated_bundle)
        except (NotFound, MultipleObjectsReturned):
            updated_bundle = self.obj_create(bundle=bundle, **self.remove_api_resource_names(kwargs))
            location = self.get_resource_uri(updated_bundle)

            if not self._meta.always_return_data:
                return http.HttpCreated(location=location)
            else:
                updated_bundle = self.full_dehydrate(updated_bundle)
                updated_bundle = self.alter_detail_data_to_serialize(request, updated_bundle)
                return self.create_response(request, updated_bundle, response_class=http.HttpCreated, location=location)

    def post_list(self, request, **kwargs):
        deserialized = self.deserialize(request, None, format=request.META.get('CONTENT_TYPE', 'application/json'))
        deserialized = self.alter_deserialized_detail_data(request, deserialized)
        bundle = self.build_bundle(data=dict_strip_unicode_keys(deserialized), request=request)

        updated_bundle = self.obj_create(bundle, **self.remove_api_resource_names(kwargs))
        location = self.get_resource_uri(updated_bundle)

        if not self._meta.always_return_data:
            return http.HttpCreated(location=location)
        else:
            updated_bundle = self.full_dehydrate(updated_bundle)
            updated_bundle = self.alter_detail_data_to_serialize(request, updated_bundle)
            return self.create_response(request, updated_bundle, response_class=http.HttpCreated, location=location)