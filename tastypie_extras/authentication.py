from tastypie.authentication import ApiKeyAuthentication


class SwaggerApiKeyAuthentication(ApiKeyAuthentication):
    def extract_credentials(self, request):
        username, api_key = super(SwaggerApiKeyAuthentication, self) \
            .extract_credentials(request)

        if username is None:
            data = request.GET.get('api_key') or request.POST.get('api_key')
            username, api_key = data.split(':', 1)

        return username, api_key
