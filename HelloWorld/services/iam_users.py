from minio import Minio
from minio.error import S3Error, ServerError
from minio.minioadmin import MinioAdmin
from HelloWorld.commons import const
from HelloWorld.plugins.minio_s3 import HaloMinio


class IAMUsersService():

    def __init__(self):
        self._plugin =  HaloMinio()
