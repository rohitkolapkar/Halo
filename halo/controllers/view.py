import asyncio
from aiohttp import web


class HaloView(web.View):

    # derived class will provide service amd service_disatch  details
    _service = None

    # common routes to used by subclass
    _app_routes = web.RouteTableDef()

    def __init__(self, request):
        super(HaloView, self).__init__(request)
