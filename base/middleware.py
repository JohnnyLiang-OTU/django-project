class Test500Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/test-500/':
            raise Exception("Test 500 error")
        return self.get_response(request)