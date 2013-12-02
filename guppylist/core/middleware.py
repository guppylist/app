class RequestMiddleware(object):
    def process_request(self, request):
        request.scripts = {}
        return None