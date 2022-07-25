from minio.error import S3Error, ServerError
from HelloWorld.commons import const
from HelloWorld.plugins.minio_s3 import HaloMinio


class BucketsService():

    def __init__(self):
        self._plugin =  HaloMinio()

    def list_buckets(self):
        buckets = self._plugin.client.list_buckets()
        return {
            "buckets":buckets
        }

    def make_bucket(self, **request_body):
        bucket_name = request_body.get(const.BUCKET_NAME)
        location  = request_body.get(const.LOCATION)
        object_lock = request_body.get(const.OBJECT_LOCK)
        try:
            self._plugin.client.make_bucket(bucket_name, location, object_lock)
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
            "message":f"bucket created: {bucket_name}"
        }