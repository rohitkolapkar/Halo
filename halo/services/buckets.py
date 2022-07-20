from minio import Minio
from minio.error import S3Error, ServerError
from halo.commons import const
from halo.plugins.minio import HaloMinio


class BucketsService():

    def __init__(self):
        self._plugin: Minio=  HaloMinio()

    def get(self):
        return "HelloWorld"

    def make_bucket(self, **request_body):
        request_body.get(const.BUCKET_NAME)
        request_body.get(const.LOCATION)
        request_body.get(const.OBJECT_LOCK)
        try:
            self._plugin.make_bucket()
        except S3Error as err:
            return {
                "error_code":"halo",
                "message_id":err.code,
                "message":err.message,
                "http_response":err.response.status
            }
        except ServerError as err:
            return {
                "error_code":"halo",
                "http_response":err.status_code
            }
        return {
            "message":f"bucket created: {const.BUCKET_NAME}"
        }