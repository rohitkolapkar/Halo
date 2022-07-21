from marshmallow import Schema, fields
from halo.controllers.view import HaloView
from halo.services.buckets import BucketsService
from halo.commons import const

class MakeBucketSchema(Schema):
    bucket_name  = fields.Str(data_key=const.BUCKET_NAME, required=True)
    location = fields.Str(data_key=const.LOCATION, allow_none=False)
    object_lock = fields.Bool(data_key=const.OBJECT_LOCK, allow_none=False)

@HaloView._app_routes.view('/api/halo/buckets')
class BucketsView(HaloView):
    def __init__(self, request):
        super(BucketsView, self).__init__(request)
        self._service = BucketsService()

    async def get(self):
        response = self._service.list_buckets()
        return response
    
    async def post(self):
        schema = MakeBucketSchema()
        request_body = schema.load(await self.request.json(), unknown='EXCLUDE')
        # NOTE: Unable to call CSM errors outside of CSM
        # Error Handling using CSM common erros is not possible.
        # try:
        #     schema = HelloWorldPostSchema()
        #     request_body = schema.load(await self.request.json(), unknown='EXCLUDE')
        # except json.decoder.JSONDecodeError:
        #     raise InvalidRequest(const.JSON_ERROR)
        # except ValidationError as val_err:
        #     raise InvalidRequest(f"Invalid request body: {val_err}")
        response = self._service.make_bucket(**request_body)
        return response