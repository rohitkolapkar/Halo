from marshmallow import Schema, fields
from HelloWorld.controllers.view import HelloWorldView
from HelloWorld.services.hello_world import HelloWorld

class HelloWorldPostSchema(Schema):
    name  = fields.Str(data_key='name', required=True)

@HelloWorldView._app_routes.view('/api/helloworld')
class HelloWorldDemo(HelloWorldView):
    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
        self._service = HelloWorld()

    async def get(self):
        message = self._service.get()
        return {"message" : message}

    async def post(self):
        schema = HelloWorldPostSchema()
        request_body = schema.load(await self.request.json(), unknown='EXCLUDE')
        message = self._service.post(**request_body)
        return {"message" : message}
