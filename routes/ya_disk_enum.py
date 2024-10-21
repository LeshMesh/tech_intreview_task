from enum import Enum


class RoutesYaDisk(str, Enum):
    BASE_URL = "https://cloud-api.yandex.net"
    RESOURCES = "/v1/disk/resources"
    RESOURCES_UPLOAD = "/v1/disk/resources/upload"

    def __str__(self) -> str:
        return self.value
