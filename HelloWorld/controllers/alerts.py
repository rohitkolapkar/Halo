from HelloWorld.controllers.view import HelloWorldView


@HelloWorldView._app_routes.view('/api/halo/alerts')
class AlertsView(HelloWorldView):
    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
        pass

    async def get(self):
        return {}
