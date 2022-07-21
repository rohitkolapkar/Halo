from minio import Minio

class HaloMinio():
    __endpoint = "ssc-vm-g2-rhev4-3394.colo.seagate.com:30869"
    __access_key = "demouser1"
    __secret_key = "demouser1"
    def __init__(self):
        self.client = Minio(HaloMinio.__endpoint,
            HaloMinio.__access_key,
            HaloMinio.__secret_key,
            secure=False)
