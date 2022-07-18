
from halo.controllers.view import HaloView
from halo.services.hello_world import HelloWorld


@HaloView._app_routes.view('/api/v2/halo/helloworld')
class HelloWorldView(HaloView):
    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
        self._service = HelloWorld()

    async def get(self):
        message = await self._service.get()
        return {"message" : message}