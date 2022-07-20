from minio import Minio

class HaloMinio():
    __endpoint = "ssc-vm-g2-rhev4-3394.colo.seagate.com:30042"
    __access_key = "SuGMg2cgoZqK6Bol"
    __secret_key = "bPTHBMjcyB2zWU7VcEXpWbVHJv3oTypH"
    def __init__(self):
        self.client = Minio(HaloMinio.__endpoint,
            access_key=HaloMinio.__access_key,
            secret_key=HaloMinio.__secret_key,
            secure=True)
    