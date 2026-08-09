class RequestLoggerMiddleware():

    def __init__(self, get_response):

        self.get_response=get_response
        pass

    def __call__(self, requets):

        print("="*50)
        print("incoming request")
        print("path:",requets.path)
        print("method:", requets.method)

        response=self.get_response(requets)
        print("response satus: " ,response.status_code)
        print("="*50)

        return response
        pass