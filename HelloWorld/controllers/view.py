from aiohttp import web

class HelloWorldView(web.View):

    # derived class will provide service
    _service = None

    # common routes to used by subclass
    _app_routes = web.RouteTableDef()

    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
