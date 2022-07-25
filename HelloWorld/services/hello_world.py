class HelloWorld():

    def get(self):
        return "HelloWorld"

    def post(self, **request_body):
        return f"Hello {request_body.get('name')}"