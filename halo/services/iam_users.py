from minio import Minio
from minio.error import S3Error, ServerError
from minio.minioadmin import MinioAdmin
from halo.commons import const
from halo.plugins.minio_s3 import HaloMinio


class IAMUsersService():

    def __init__(self):
        self._plugin =  HaloMinio()
