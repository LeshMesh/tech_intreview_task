from enum import Enum


class RoutesDocCeo(str, Enum):
    BASE_URL = "https://dog.ceo"
    LIST_BREED = "/api/breed/{}/list"
    RANDOM_SUB_BREED = "/api/breed/{}/{}/images/random"
    RANDOM_BREED = "/api/breed/{}/images/random"

    def __str__(self) -> str:
        return self.value
