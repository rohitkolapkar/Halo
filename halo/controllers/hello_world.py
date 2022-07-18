from marshmallow import Schema, fields
from halo.controllers.view import HaloView
from halo.services.hello_world import HelloWorld

class HelloWorldPostSchema(Schema):
    name  = fields.Str(data_key='name', required=True)

@HaloView._app_routes.view('/api/v2/halo/helloworld')
class HelloWorldView(HaloView):
    def __init__(self, request):
        super(HelloWorldView, self).__init__(request)
        self._service = HelloWorld()

    async def get(self):
        message = self._service.get()
        return {"message" : message}
    
    async def post(self):
        schema = HelloWorldPostSchema()
        request_body = schema.load(await self.request.json(), unknown='EXCLUDE')
        # try:
        #     schema = HelloWorldPostSchema()
        #     request_bod = schema.load(await self.request.json(), unknown='EXCLUDE')
        # except json.decoder.JSONDecodeError:
        #     raise InvalidRequest(const.JSON_ERROR)
        # except ValidationError as val_err:
        #     raise InvalidRequest(f"Invalid request body: {val_err}")
        message = self._service.post(**request_body)
        return {"message" : message}