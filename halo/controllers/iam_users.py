from marshmallow import Schema, fields
from halo.controllers.view import HaloView
from halo.services.iam_users import IAMUsersService
from halo.commons import const

class MakeBucketSchema(Schema):
    bucket_name  = fields.Str(data_key=const.BUCKET_NAME, required=True)
    location = fields.Str(data_key=const.LOCATION, allow_none=False)
    object_lock = fields.Bool(data_key=const.OBJECT_LOCK, allow_none=False)

@HaloView._app_routes.view('/api/halo/iam/users')
class IAMUsersView(HaloView):
    def __init__(self, request):
        super(IAMUsersView, self).__init__(request)
        self._service = IAMUsersService()

    async def get(self):
        response = {"users":[]}
        return response
    
    async def post(self):
        response = {"message":"User created"}
        return response